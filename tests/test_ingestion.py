import json

import pytest

from app.ingestion.chunk import chunk_text
from app.ingestion.clean import clean_text, content_hash
from app.ingestion.dedupe import deduplicate
from app.ingestion.sources import load_sources


def test_clean_normalises_line_endings_and_blank_lines():
    assert clean_text(" a\r\n\r\n\r\n\r\nb ") == "a\n\nb"
    assert clean_text("x\ry") == "x\ny"


def test_hash_is_stable_and_ignores_formatting_noise():
    assert content_hash("same") == content_hash("same")
    assert content_hash("a\r\nb") == content_hash("a\nb")
    assert content_hash("a") != content_hash("b")


def test_chunk_overlap_contract():
    chunks = chunk_text("x" * 2000, size=500, overlap=50)
    assert len(chunks) > 1
    assert chunks[0].text[-50:] == chunks[1].text[:50]


def test_chunk_rejects_bad_size():
    with pytest.raises(ValueError):
        chunk_text("abc", size=10, overlap=10)


def test_chunks_carry_version_metadata():
    chunks = chunk_text(
        "hello world " * 200, size=300, overlap=30,
        product="postgres", version="16", document="runtime-config", section="Memory",
    )
    assert all(c.version == "16" and c.product == "postgres" for c in chunks)
    assert chunks[0].chunk_id == "postgres:16:runtime-config:0"
    assert len({c.chunk_id for c in chunks}) == len(chunks)


def test_dedupe_is_scoped_to_product_and_version():
    docs = [
        {"product": "p", "version": "1", "text": "same text"},
        {"product": "p", "version": "1", "text": "same text\r\n"},
        {"product": "p", "version": "2", "text": "same text"},
    ]
    unique = deduplicate(docs)
    assert [d["version"] for d in unique] == ["1", "2"]
    assert all("content_hash" in d for d in unique)


def test_sources_require_licence(tmp_path):
    good = tmp_path / "good.json"
    good.write_text(json.dumps([{"product": "p", "version": "1", "url": "u", "licence": "MIT"}]))
    assert load_sources(good)[0].licence == "MIT"
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps([{"product": "p", "version": "1", "url": "u", "licence": " "}]))
    with pytest.raises(ValueError):
        load_sources(bad)
