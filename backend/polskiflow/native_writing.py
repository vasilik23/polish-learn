"""Bounded, non-persistent writing practice for separate clients."""

import re

from polskiflow.auth_views import WRITING_PROMPTS


class NativeWritingError(ValueError):
    pass


PROMPTS_BY_ID = {
    prompt["id"]: {**prompt, "level": level}
    for level, prompts in WRITING_PROMPTS.items()
    for prompt in prompts
}


def build_native_writing() -> dict:
    return {
        "levels": list(WRITING_PROMPTS),
        "prompts": [
            {
                "id": prompt["id"],
                "level": level,
                "title": prompt["title"],
                "task": prompt["task"],
                "hint": prompt["hint"],
                "minimum_words": prompt["min_words"],
                "minimum_paragraphs": prompt["min_paragraphs"],
                "required_markers": list(prompt["markers"]),
                "checklist": list(prompt["checklist"]),
            }
            for level, prompts in WRITING_PROMPTS.items()
            for prompt in prompts
        ],
        "prompt_count": sum(len(prompts) for prompts in WRITING_PROMPTS.values()),
        "persistence": "none",
        "assessment": "observable_structure_only",
    }


def evaluate_native_writing(prompt_id: str, text: object) -> dict:
    prompt = PROMPTS_BY_ID.get(prompt_id)
    if prompt is None:
        raise NativeWritingError("prompt_not_found")
    if not isinstance(text, str):
        raise NativeWritingError("text must be a string")
    if not text.strip():
        raise NativeWritingError("text must not be empty")
    if len(text) > 16000:
        raise NativeWritingError("text must contain at most 16000 characters")

    words = len(re.findall(r"\S+", text.strip(), flags=re.UNICODE))
    paragraphs = len(
        [part for part in re.split(r"\n\s*\n", text.strip()) if part.strip()]
    )
    normalized = text.casefold()
    markers = tuple(prompt["markers"])
    found_markers = [marker for marker in markers if marker.casefold() in normalized]
    checks = [
        {
            "id": "minimum_words",
            "passed": words >= prompt["min_words"],
            "observed": words,
            "required": prompt["min_words"],
        },
        {
            "id": "minimum_paragraphs",
            "passed": paragraphs >= prompt["min_paragraphs"],
            "observed": paragraphs,
            "required": prompt["min_paragraphs"],
        },
        {
            "id": "required_markers",
            "passed": len(found_markers) == len(markers),
            "found": found_markers,
            "required": list(markers),
        },
    ]
    return {
        "prompt_id": prompt_id,
        "level": prompt["level"],
        "checks": checks,
        "all_observable_checks_passed": all(check["passed"] for check in checks),
        "limitations": (
            "Проверены только объём, абзацы и заданные маркеры. Результат не "
            "оценивает грамматику, смысл, стиль или уровень CEFR."
        ),
        "persisted": False,
    }
