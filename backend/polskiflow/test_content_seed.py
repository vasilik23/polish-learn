from django.test import TestCase

from polskiflow.learning.models import (
    Flashcard,
    Lesson,
    LessonFlashcard,
    Question,
    ReadingText,
    Topic,
)


class IntroductionsContentTests(TestCase):
    def test_introductions_topic_is_first(self):
        topic = Topic.objects.get(id="introductions")

        self.assertEqual(topic.position, 0)
        self.assertEqual(topic.title, "Знакомство")
        self.assertEqual(topic.course_id, "a1-foundations")

    def test_daily_plan_contains_complete_introductions_block(self):
        lessons = Lesson.objects.filter(topic_id="introductions")

        self.assertEqual(lessons.count(), 4)
        self.assertEqual(Question.objects.filter(lesson_id="grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="quiz").count(), 8)
        self.assertEqual(
            LessonFlashcard.objects.filter(lesson_id="words").count(), 8
        )
        self.assertEqual(
            LessonFlashcard.objects.filter(lesson_id="review").count(), 7
        )

    def test_original_content_has_source_metadata(self):
        expected_origin = "original"

        self.assertEqual(
            Lesson.objects.get(id="words").source_metadata["origin"],
            expected_origin,
        )
        self.assertEqual(
            Flashcard.objects.get(id="mam-na-imie").source_metadata["origin"],
            expected_origin,
        )
        self.assertEqual(
            ReadingText.objects.get(
                id="pierwszy-dzien-na-kursie"
            ).source_metadata["origin"],
            expected_origin,
        )

    def test_introductions_reading_has_glossary(self):
        reading = ReadingText.objects.get(id="pierwszy-dzien-na-kursie")

        self.assertEqual(reading.level, "A1")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertIn("przedstawia", reading.glossary)
