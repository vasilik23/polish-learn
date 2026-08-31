from django.test import TestCase

from polskiflow.learning.models import Lesson, LessonKind, ReadingText


class ReadingComprehensionCoverageTests(TestCase):
    minimum_questions_by_level = {
        "A1": 3,
        "A2": 5,
        "B1": 6,
        "B2": 6,
        "C1": 6,
        "C2": 6,
    }

    # Editorial debt: these early A1 texts share comprehension lessons with the
    # introductions topic. Keep the exception explicit so no new mismatch passes.
    legacy_topic_mismatches = {
        "poranek-anny": "introductions",
        "zakupy-na-targu": "introductions",
    }

    def test_every_active_reading_has_an_active_comprehension_quiz(self):
        readings = ReadingText.objects.filter(is_active=True).select_related("topic")

        self.assertTrue(readings.exists(), "The active reading catalog is empty")
        self.assertTrue(
            self.legacy_topic_mismatches.keys()
            <= set(readings.values_list("id", flat=True)),
            "Remove stale entries from the legacy reading-topic allowlist",
        )
        for reading in readings:
            with self.subTest(reading_id=reading.id, level=reading.level):
                minimum_questions = self.minimum_questions_by_level.get(reading.level)
                self.assertIsNotNone(
                    minimum_questions,
                    f"{reading.id}: unsupported reading level {reading.level!r}",
                )

                metadata = reading.source_metadata
                self.assertIsInstance(
                    metadata,
                    dict,
                    f"{reading.id}: source_metadata must be an object",
                )
                comprehension_lesson_id = metadata.get("comprehension_lesson_id")
                self.assertIsInstance(
                    comprehension_lesson_id,
                    str,
                    f"{reading.id}: comprehension_lesson_id must be a string",
                )
                self.assertTrue(
                    comprehension_lesson_id.strip(),
                    f"{reading.id}: comprehension_lesson_id is empty",
                )
                self.assertIsNotNone(
                    reading.topic_id,
                    f"{reading.id}: active reading must belong to a topic",
                )
                self.assertTrue(
                    reading.topic.is_active,
                    f"{reading.id}: reading topic {reading.topic_id!r} is inactive",
                )

                lesson = Lesson.objects.filter(id=comprehension_lesson_id).first()
                self.assertIsNotNone(
                    lesson,
                    f"{reading.id}: lesson {comprehension_lesson_id!r} does not exist",
                )
                self.assertTrue(
                    lesson.is_active,
                    f"{reading.id}: comprehension lesson {lesson.id!r} is inactive",
                )
                self.assertEqual(
                    lesson.kind,
                    LessonKind.QUIZ,
                    f"{reading.id}: comprehension lesson must be a quiz",
                )

                expected_topic_id = self.legacy_topic_mismatches.get(
                    reading.id, reading.topic_id
                )
                self.assertEqual(
                    lesson.topic_id,
                    expected_topic_id,
                    f"{reading.id}: comprehension lesson belongs to another topic",
                )
                self.assertGreaterEqual(
                    lesson.questions.filter(is_active=True).count(),
                    minimum_questions,
                    f"{reading.id}: too few active comprehension questions",
                )
