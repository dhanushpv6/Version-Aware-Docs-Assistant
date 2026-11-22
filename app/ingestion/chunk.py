"""Chunking with version metadata."""
from dataclasses import dataclass


@dataclass
class Chunk:
    text: str
    chunk_index: int
    product: str = ""
    version: str = ""
    document: str = ""
    section: str = ""

    @property
    def chunk_id(self) -> str:
        return f"{self.product}:{self.version}:{self.document}:{self.chunk_index}"


def chunk_text(
    text: str,
    size: int = 900,
    overlap: int = 120,
    *,
    product: str = "",
    version: str = "",
    document: str = "",
    section: str = "",
) -> list[Chunk]:
    """Split text into overlapping chunks that carry version metadata."""
    if size <= overlap:
        raise ValueError("size must be greater than overlap")
    chunks: list[Chunk] = []
    start = 0
    while start < len(text):
        end = min(len(text), start + size)
        part = text[start:end].strip()
        if part:
            chunks.append(
                Chunk(part, len(chunks), product, version, document, section)
            )
        if end == len(text):
            break
        start = end - overlap
    return chunks
