"""Pure selection logic for a learner's daily plan."""

from datetime import date


DAILY_TASK_LIMIT = 4


def build_daily_plan(
    lessons: list[dict],
    *,
    level: str,
    completed_all_time: frozenset[str],
    completed_today: frozenset[str],
    personal_words: list[dict] | None,
    today: date,
) -> list[dict]:
    """Choose the next lessons and, when useful, an SM-2 review."""

    level_lessons = [lesson for lesson in lessons if lesson.get("level") == level]
    candidates = level_lessons or lessons
    unfinished = [
        lesson for lesson in candidates if lesson["id"] not in completed_all_time
    ]
    ordered = unfinished + [
        lesson for lesson in candidates if lesson["id"] in completed_all_time
    ]

    due_count = _due_word_count(personal_words, today)
    can_review = personal_words is not None and len(personal_words) >= 4 and due_count > 0
    lesson_limit = DAILY_TASK_LIMIT - int(can_review)
    plan = [dict(lesson) for lesson in ordered[:lesson_limit]]

    if can_review:
        plan.append(
            {
                "id": "dictionary-practice",
                "kind": "dictionary-review",
                "title": "Повторение словаря",
                "description": (
                    f"{due_count} {_russian_word_label(due_count)} по расписанию SM-2"
                ),
                "minutes": min(10, max(3, due_count)),
                "emoji": "🧠",
                "level": level,
            }
        )

    for task in plan:
        task["completed"] = task["id"] in completed_today
    return plan


def _due_word_count(words: list[dict] | None, today: date) -> int:
    count = 0
    for word in words or []:
        value = word.get("next_review_date")
        if value in (None, ""):
            count += 1
            continue
        try:
            if not isinstance(value, str) or date.fromisoformat(value) <= today:
                count += 1
        except ValueError:
            count += 1
    return count


def _russian_word_label(count: int) -> str:
    if count % 10 == 1 and count % 100 != 11:
        return "слово"
    if count % 10 in (2, 3, 4) and count % 100 not in (12, 13, 14):
        return "слова"
    return "слов"
