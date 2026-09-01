"""Pure helpers for filtering the server-rendered reading catalog."""

from collections.abc import Iterable


READING_DURATION_FILTERS = {
    "short": (0, 5),
    "medium": (6, 10),
    "long": (11, None),
}


def filter_reading_texts(
    texts: Iterable[dict],
    *,
    query: str = "",
    topic_id: str = "",
    duration: str = "",
) -> list[dict]:
    """Return local learning texts matching validated catalog filters."""
    needle = query.strip().casefold()
    return [
        text
        for text in texts
        if (not topic_id or text.get("topic_id") == topic_id)
        and (not needle or needle in _search_text(
            text.get("title", ""), text.get("description", "")
        ))
        and _matches_duration(text.get("minutes", 0), duration)
    ]


def _search_text(*parts: str) -> str:
    return " ".join(parts).casefold()


def _matches_duration(minutes: int, duration: str) -> bool:
    if not duration:
        return True
    minimum, maximum = READING_DURATION_FILTERS[duration]
    return minutes >= minimum and (maximum is None or minutes <= maximum)
