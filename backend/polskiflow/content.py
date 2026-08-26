"""Database-backed lesson content queries."""

from django.db.models import Prefetch

from polskiflow.learning.models import Flashcard, Lesson, ReadingText, Topic


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


def course_topics() -> list[dict]:
    active_lessons = Lesson.objects.filter(is_active=True).order_by("position", "id")
    topics = Topic.objects.filter(
        is_active=True, course__is_active=True
    ).select_related("course").prefetch_related(
        Prefetch("lessons", queryset=active_lessons, to_attr="active_lessons")
    )
    return [
        {
            "id": topic.id,
            "title": topic.title,
            "description": topic.description,
            "emoji": topic.emoji,
            "level": topic.course.level,
            "lessons": [
                {
                    "id": lesson.id,
                    "title": lesson.title,
                    "description": lesson.description,
                    "minutes": lesson.minutes,
                    "emoji": lesson.emoji,
                }
                for lesson in topic.active_lessons
            ],
        }
        for topic in topics
        if topic.active_lessons
    ]


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
