"""Small, fail-safe reader for explicitly published official Polish RSS feeds."""

from email.utils import parsedate_to_datetime
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from xml.etree import ElementTree

from django.core.cache import cache


FEEDS = (
    {
        "name": "Główny Urząd Statystyczny",
        "url": "https://stat.gov.pl/rss/pl/5438/8.xml",
        "host": "stat.gov.pl",
    },
)
CACHE_KEY = "polskiflow:official-news:v1"
MAX_RESPONSE_BYTES = 512_000


def latest_official_news(limit: int = 6) -> list[dict]:
    cached = cache.get(CACHE_KEY)
    if cached is not None:
        return cached[:limit]
    items = []
    for feed in FEEDS:
        items.extend(_load_feed(feed))
    items.sort(key=lambda item: item["published_sort"], reverse=True)
    result = items[: max(1, min(limit, 12))]
    cache.set(CACHE_KEY, result, 15 * 60)
    return result


def _load_feed(feed: dict) -> list[dict]:
    try:
        request = Request(feed["url"], headers={"User-Agent": "PolskiFlow/1.0 RSS reader"})
        with urlopen(request, timeout=4) as response:
            body = response.read(MAX_RESPONSE_BYTES + 1)
        if len(body) > MAX_RESPONSE_BYTES:
            return []
        root = ElementTree.fromstring(body)
    except (OSError, ValueError, ElementTree.ParseError):
        return []
    result = []
    for node in root.findall(".//item")[:12]:
        title = (node.findtext("title") or "").strip()
        link = (node.findtext("link") or "").strip()
        published = (node.findtext("pubDate") or "").strip()
        parsed = urlparse(link)
        if not title or parsed.scheme != "https" or parsed.hostname != feed["host"]:
            continue
        result.append(
            {
                "title": title[:240],
                "url": link,
                "source": feed["name"],
                "published": _display_date(published),
                "published_sort": _timestamp(published),
            }
        )
    return result


def _timestamp(value: str) -> float:
    try:
        return parsedate_to_datetime(value).timestamp()
    except (TypeError, ValueError, OverflowError):
        return 0


def _display_date(value: str) -> str:
    try:
        date = parsedate_to_datetime(value)
        return date.strftime("%d.%m.%Y")
    except (TypeError, ValueError, OverflowError):
        return ""
