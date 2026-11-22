"""Fetching documentation pages."""
import httpx

USER_AGENT = "version-aware-docs-assistant/0.1 (+research; author: Dhanush)"


async def fetch_text(url: str) -> str:
    """Fetch one page.

    Crawl only sources whose licence, terms and robots policy permit it
    (see docs/data-licensing.md and data/sources/sources.example.json).
    """
    async with httpx.AsyncClient(
        timeout=20, follow_redirects=True, headers={"User-Agent": USER_AGENT}
    ) as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.text
