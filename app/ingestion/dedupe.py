"""Content-hash deduplication."""
from collections.abc import Iterable

from app.ingestion.clean import content_hash


def deduplicate(documents: Iterable[dict]) -> list[dict]:
    """Drop documents with identical cleaned content within the same product and version.

    Each document is a dict with at least ``product``, ``version`` and ``text``.
    The first occurrence wins; a ``content_hash`` key is added to survivors.
    """
    seen: set[tuple[str, str, str]] = set()
    unique: list[dict] = []
    for doc in documents:
        digest = content_hash(doc["text"])
        key = (doc["product"], doc["version"], digest)
        if key in seen:
            continue
        seen.add(key)
        unique.append({**doc, "content_hash": digest})
    return unique
