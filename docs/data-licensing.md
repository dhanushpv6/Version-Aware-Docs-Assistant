# Data and licensing

- Use openly licensed documentation only, and only where crawling is permitted.
- Record for every source: URL, licence, retrieval date, product and version
  (see `data/sources/sources.example.json`). `load_sources()` refuses entries without a licence.
- Respect `robots.txt` and the site's terms. Rate-limit requests.
- Do not redistribute crawled content unless its licence allows it. Raw and processed
  data are git-ignored (`data/raw/`, `data/processed/`).
- State in the README which documentation was used and under which licence.
