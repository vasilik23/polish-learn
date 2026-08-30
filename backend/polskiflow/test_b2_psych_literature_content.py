from unittest.mock import patch

from django.test import TestCase

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser
from polskiflow.learning.models import Lesson, LessonFlashcard, Question, ReadingText, Topic


class B2PsychologyAndLiteratureContentTests(TestCase):
    def test_topics_have_complete_vertical_lesson_sets(self):
        expectations = (
            ("b2-psychology-relationships", 6, "b2psych"),
            ("b2-literature-cinema", 7, "b2lit"),
        )
        for topic_id, position, prefix in expectations:
            with self.subTest(topic_id=topic_id):
                topic = Topic.objects.get(id=topic_id)
                self.assertEqual(topic.course.level, "B2")
                self.assertEqual(topic.position, position)
                self.assertEqual(Lesson.objects.filter(topic=topic).count(), 5)
                self.assertEqual(Question.objects.filter(lesson_id=f"{prefix}-grammar").count(), 6)
                self.assertEqual(Question.objects.filter(lesson_id=f"{prefix}-quiz").count(), 10)
                self.assertEqual(Question.objects.filter(lesson_id=f"{prefix}-reading-check").count(), 6)
                self.assertEqual(LessonFlashcard.objects.filter(lesson_id=f"{prefix}-words").count(), 8)
                self.assertEqual(LessonFlashcard.objects.filter(lesson_id=f"{prefix}-review").count(), 7)

    def test_grammar_includes_sentence_building(self):
        for prefix in ("b2psych", "b2lit"):
            prompts = Question.objects.filter(lesson_id=f"{prefix}-grammar").values_list("prompt", flat=True)
            self.assertEqual(sum(prompt.startswith("Составьте:") for prompt in prompts), 2)

    def test_readings_are_original_and_lemma_aware(self):
        expectations = (
            ("b2psych-rozmowa-po-nieudanym-wyjezdzie", "b2psych-reading-check", 42),
            ("b2lit-recenzja-filmu-swiatlo-na-peronie", "b2lit-reading-check", 43),
        )
        for reading_id, lesson_id, position in expectations:
            with self.subTest(reading_id=reading_id):
                reading = ReadingText.objects.get(id=reading_id)
                self.assertEqual(reading.level, "B2")
                self.assertEqual(reading.position, position)
                self.assertEqual(reading.source_metadata["origin"], "original")
                self.assertEqual(reading.source_metadata["created_for"], "PolskiFlow")
                self.assertEqual(reading.source_metadata["comprehension_lesson_id"], lesson_id)
                self.assertEqual(len(reading.paragraphs), 5)
                self.assertGreaterEqual(len(reading.glossary), 18)
                for entry in reading.glossary.values():
                    self.assertTrue(entry["lemma"])
                    self.assertTrue(entry["translation"])
                    self.assertTrue(entry["part_of_speech"])


class B2PsychologyAndLiteratureReadingRouteTests(TestCase):
    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        self.auth_patch = patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser(
                "00000000-0000-0000-0000-000000000123", "reader@example.com"
            ),
        )
        self.auth_patch.start()
        self.addCleanup(self.auth_patch.stop)

    def test_readings_link_to_comprehension_lessons(self):
        expectations = (
            ("b2psych-rozmowa-po-nieudanym-wyjezdzie", "b2psych-reading-check"),
            ("b2lit-recenzja-filmu-swiatlo-na-peronie", "b2lit-reading-check"),
        )
        for reading_id, lesson_id in expectations:
            with self.subTest(reading_id=reading_id):
                response = self.client.get(f"/reading/{reading_id}/")
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, f'href="/lesson/{lesson_id}/"')
                self.assertContains(response, "Добавить в словарь")
