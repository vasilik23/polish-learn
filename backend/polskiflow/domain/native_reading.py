"""Stable reading-library payloads for separate clients."""

READING_LEVELS = ("A1", "A2", "B1", "B2", "C1", "C2")
SOURCE_FIELDS = ("origin", "title", "url", "author", "license", "verified_at")


def filter_native_readings(texts: list[dict], *, level: str, query: str) -> list[dict]:
    needle = query.strip().casefold()
    return [
        text for text in texts
        if (not level or text.get("level") == level)
        and (not needle or needle in f"{text.get('title', '')} {text.get('description', '')}".casefold())
    ]


def serialize_reading_detail(text, *, saved: bool) -> dict:
    metadata = text.source_metadata if isinstance(text.source_metadata, dict) else {}
    comprehension_id = metadata.get("comprehension_lesson_id")
    return {
        "id": text.id,
        "title": text.title,
        "description": text.description,
        "level": text.level if text.level in READING_LEVELS else "A1",
        "minutes": text.minutes,
        "emoji": text.emoji,
        "topic_id": text.topic_id,
        "paragraphs": [item for item in text.paragraphs if isinstance(item, str)],
        "glossary": _serialize_glossary(text.glossary),
        "saved": saved,
        "comprehension_lesson_id": comprehension_id if isinstance(comprehension_id, str) and comprehension_id else None,
        "source": {key: metadata[key] for key in SOURCE_FIELDS if isinstance(metadata.get(key), str) and metadata[key]},
    }


def resolve_glossary_entry(glossary, surface: str) -> dict | None:
    """Resolve one surface form to canonical lemma and translation."""
    if not isinstance(surface, str):
        return None
    needle = surface.strip().casefold()
    if not needle:
        return None
    for item in _serialize_glossary(glossary):
        if item["surface"].strip().casefold() == needle:
            return item
    return None


def _serialize_glossary(glossary) -> list[dict]:
    if not isinstance(glossary, dict):
        return []
    result = []
    for surface, entry in glossary.items():
        if not isinstance(surface, str) or not surface:
            continue
        if isinstance(entry, str):
            result.append({"surface": surface, "lemma": surface, "translation": entry, "part_of_speech": ""})
        elif isinstance(entry, dict) and isinstance(entry.get("translation"), str):
            result.append({
                "surface": surface,
                "lemma": entry.get("lemma") if isinstance(entry.get("lemma"), str) and entry["lemma"] else surface,
                "translation": entry["translation"],
                "part_of_speech": entry.get("part_of_speech") if isinstance(entry.get("part_of_speech"), str) else "",
            })
    return result
