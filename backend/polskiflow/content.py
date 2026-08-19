"""Database-backed lesson content queries."""

from polskiflow.learning.models import Flashcard, Lesson


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
        "title": lesson.title,
        "plan_title": lesson.plan_title,
        "subtitle": lesson.subtitle,
        "description": lesson.description,
        "minutes": lesson.minutes,
        "emoji": lesson.emoji,
    }


def flashcards() -> list[dict]:
    return list(
        Flashcard.objects.filter(is_active=True).values(
            "id", "polish", "translation", "example"
        )
    )


def grammar() -> dict | None:
    lesson = Lesson.objects.filter(id="grammar", is_active=True).first()
    if lesson is None:
        return None
    return {
        "title": lesson.theory_title,
        "sections": lesson.theory_sections,
        "questions": _questions(lesson),
    }


def quiz() -> list[dict]:
    lesson = Lesson.objects.filter(id="quiz", is_active=True).first()
    return _questions(lesson) if lesson else []


def _questions(lesson: Lesson) -> list[dict]:
    return list(
        lesson.questions.filter(is_active=True).values(
            "prompt", "options", "correct", "explanation"
        )
    )
