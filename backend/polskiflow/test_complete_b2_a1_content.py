from django.test import TestCase

from polskiflow.learning.models import Course, Lesson, ReadingText, Topic


class CompleteB2AndA1ContentTests(TestCase):
    def test_complete_c1_catalog_has_vertical_blocks(self):
        course = Course.objects.get(id="c1-proficiency")
        self.assertEqual(course.level, "C1")
        self.assertEqual(Topic.objects.filter(course=course, is_active=True).count(), 10)
        for topic in Topic.objects.filter(course=course):
            self.assertEqual(topic.lessons.filter(is_active=True).count(), 5)
            reading = ReadingText.objects.get(topic=topic, is_active=True)
            self.assertGreaterEqual(len(reading.glossary), 15)
            self.assertTrue(reading.source_metadata["comprehension_lesson_id"])

    def test_b2_catalog_is_complete_and_each_new_topic_has_full_path(self):
        course = Course.objects.get(id="b2-advanced")
        self.assertEqual(Topic.objects.filter(course=course, is_active=True).count(), 12)
        for topic_id in (
            "b2-public-discussion",
            "b2-intercultural-communication",
            "b2-academic-skills",
            "b2-final-project",
        ):
            topic = Topic.objects.get(id=topic_id)
            self.assertEqual(topic.lessons.filter(is_active=True).count(), 5)
            reading = ReadingText.objects.get(topic=topic, is_active=True)
            self.assertEqual(reading.level, "B2")
            self.assertGreaterEqual(len(reading.glossary), 18)
            self.assertTrue(reading.source_metadata["comprehension_lesson_id"])

    def test_every_active_a1_reading_has_a_comprehension_lesson(self):
        readings = ReadingText.objects.filter(level="A1", is_active=True)
        self.assertEqual(readings.count(), 14)
        for reading in readings:
            lesson_id = reading.source_metadata.get("comprehension_lesson_id")
            self.assertTrue(lesson_id, reading.id)
            lesson = Lesson.objects.get(id=lesson_id)
            self.assertEqual(lesson.kind, "quiz")
            self.assertGreaterEqual(lesson.questions.count(), 3)
