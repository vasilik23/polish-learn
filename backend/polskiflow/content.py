"""Database-backed lesson content queries."""

from polskiflow.learning.models import Flashcard, Lesson, ReadingText


def tasks() -> list[dict]:
    return list(
        Lesson.objects.filter(is_active=True).values(
            "id", "title", "plan_title", "subtitle", "description", "minutes", "emoji"
        )
    )


def task(lesson_id: str) -> dict | None:
    lesson = Lesson.objects.filter(id=lesson_id, is_active=True).first()
    if lesson is None:
        return None
    return {
        "id": lesson.id,
        "kind": lesson.kind,
        "title": lesson.title,
        "plan_title": lesson.plan_title,
        "subtitle": lesson.subtitle,
        "description": lesson.description,
        "minutes": lesson.minutes,
        "emoji": lesson.emoji,
    }


def flashcards(lesson_id: str | None = None) -> list[dict]:
    queryset = Flashcard.objects.filter(is_active=True)
    if lesson_id is not None:
        queryset = queryset.filter(
            lesson_links__lesson_id=lesson_id,
            lesson_links__lesson__is_active=True,
        ).order_by("lesson_links__position", "id")
    return list(
        queryset.values(
            "id", "polish", "translation", "example"
        )
    )


def grammar(lesson_id: str = "grammar") -> dict | None:
    lesson = Lesson.objects.filter(id=lesson_id, is_active=True).first()
    if lesson is None:
        return None
    return {
        "title": lesson.theory_title,
        "sections": lesson.theory_sections,
        "questions": _questions(lesson),
    }


def quiz(lesson_id: str = "quiz") -> list[dict]:
    lesson = Lesson.objects.filter(id=lesson_id, is_active=True).first()
    return _questions(lesson) if lesson else []


def _questions(lesson: Lesson) -> list[dict]:
    return list(
        lesson.questions.filter(is_active=True).values(
            "prompt", "options", "correct", "explanation"
        )
    )


def reading_texts() -> list[dict]:
    return list(
        ReadingText.objects.filter(is_active=True).values(
            "id", "title", "description", "level", "minutes", "emoji"
        )
    )


def reading_text(text_id: str) -> ReadingText | None:
    return ReadingText.objects.filter(id=text_id, is_active=True).first()
