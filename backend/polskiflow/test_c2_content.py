from unittest.mock import patch

from django.test import TestCase

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser
from polskiflow.learning.models import Course, Lesson, LessonFlashcard, Question, ReadingText, Topic


class C2ContentTests(TestCase):
    topic_expectations = (
        ("c2-semantic-precision", "c21", 0, 57),
        ("c2-rhetorical-strategy", "c22", 1, 58),
        ("c2-critical-polemics", "c23", 2, 59),
        ("c2-professional-editing", "c24", 3, 60),
    )

    def test_course_is_a_curriculum_target_with_four_vertical_topics(self):
        course = Course.objects.get(id="c2-mastery")
        self.assertEqual(course.level, "C2")
        self.assertIn("Целевая программа", course.description)
        self.assertEqual(Topic.objects.filter(course=course, is_active=True).count(), 4)
        for topic_id, prefix, position, _reading_position in self.topic_expectations:
            with self.subTest(topic_id=topic_id):
                topic = Topic.objects.get(id=topic_id)
                self.assertEqual(topic.position, position)
                self.assertEqual(Lesson.objects.filter(topic=topic, is_active=True).count(), 5)
                self.assertEqual(LessonFlashcard.objects.filter(lesson_id=f"{prefix}-words").count(), 8)
                self.assertEqual(LessonFlashcard.objects.filter(lesson_id=f"{prefix}-review").count(), 7)
                self.assertEqual(Question.objects.filter(lesson_id=f"{prefix}-grammar").count(), 6)
                self.assertEqual(Question.objects.filter(lesson_id=f"{prefix}-quiz").count(), 10)
                self.assertEqual(Question.objects.filter(lesson_id=f"{prefix}-reading-check").count(), 6)

    def test_grammar_has_explanations_and_sentence_builders(self):
        for _topic_id, prefix, _position, _reading_position in self.topic_expectations:
            questions = Question.objects.filter(lesson_id=f"{prefix}-grammar")
            self.assertGreaterEqual(sum(question.prompt.startswith("Составьте:") for question in questions), 2)
            self.assertTrue(all(question.explanation for question in questions))
            self.assertTrue(all(len(question.options[question.correct].split()) >= 4 for question in questions[:2]))

    def test_readings_are_original_and_glossaries_are_lemma_aware(self):
        for topic_id, prefix, _position, reading_position in self.topic_expectations:
            with self.subTest(topic_id=topic_id):
                reading = ReadingText.objects.get(topic_id=topic_id)
                self.assertEqual(reading.id, f"{prefix}-tekst")
                self.assertEqual(reading.level, "C2")
                self.assertEqual(reading.position, reading_position)
                self.assertEqual(len(reading.paragraphs), 5)
                self.assertGreaterEqual(len(reading.glossary), 18)
                self.assertEqual(reading.source_metadata["origin"], "original")
                self.assertEqual(reading.source_metadata["created_for"], "PolskiFlow")
                self.assertEqual(reading.source_metadata["level_status"], "curriculum_target")
                self.assertEqual(reading.source_metadata["comprehension_lesson_id"], f"{prefix}-reading-check")
                for entry in reading.glossary.values():
                    self.assertTrue(entry["lemma"])
                    self.assertTrue(entry["translation"])
                    self.assertTrue(entry["part_of_speech"])


class C2ReadingRoutesTests(TestCase):
    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        auth_patch = patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser("00000000-0000-0000-0000-000000000123", "reader@example.com"),
        )
        auth_patch.start()
        self.addCleanup(auth_patch.stop)

    def test_readings_link_to_their_comprehension_lessons(self):
        for prefix in ("c21", "c22", "c23", "c24"):
            with self.subTest(prefix=prefix):
                response = self.client.get(f"/reading/{prefix}-tekst/")
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, f'href="/lesson/{prefix}-reading-check/"')
                self.assertContains(response, "Добавить в словарь")

    def test_reading_catalog_offers_c2_tab_and_filters_c2_texts(self):
        with patch("polskiflow.reading_views.select_cefr_level", return_value="C2"):
            response = self.client.get("/reading/?level=C2")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="?level=C2#texts-title"')
        self.assertContains(response, "Смысловая точность")
        self.assertContains(response, "Риторическая стратегия")
        self.assertContains(response, "Критическая полемика")
        self.assertContains(response, "Профессиональная редактура")
