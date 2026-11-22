"""Text cleaning and content hashing."""
import hashlib
import re


def clean_text(text: str) -> str:
    """Normalise line endings and collapse runs of blank lines."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def content_hash(text: str) -> str:
    """SHA-256 of the cleaned text, used for deduplication."""
    return hashlib.sha256(clean_text(text).encode("utf-8")).hexdigest()
