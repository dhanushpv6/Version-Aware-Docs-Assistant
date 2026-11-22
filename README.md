# Version-Aware Docs Assistant

**Author:** Dhanush

A documentation assistant that answers for the software version you use, cites document,
section and version, and says it does not know when evidence is missing.

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
pytest
uvicorn app.main:app --reload
```

## Docs
- [Data licensing](docs/data-licensing.md)

## License
MIT - see [LICENSE](LICENSE).
