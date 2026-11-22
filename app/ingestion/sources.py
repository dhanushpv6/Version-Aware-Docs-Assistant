"""Source registry: which documentation, which versions, which licence."""
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Source:
    product: str
    version: str
    url: str
    licence: str
    retrieved_on: str = ""


def load_sources(path: str | Path) -> list[Source]:
    """Load sources and refuse any entry that lacks a licence."""
    entries = json.loads(Path(path).read_text(encoding="utf-8"))
    sources = [Source(**entry) for entry in entries]
    missing = [s for s in sources if not s.licence.strip()]
    if missing:
        raise ValueError(
            f"{len(missing)} source(s) have no licence recorded; refusing to load"
        )
    return sources
