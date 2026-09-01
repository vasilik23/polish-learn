from django.test import TestCase

from polskiflow.learning.models import Flashcard, Lesson, ReadingText, Topic


class EditorialSampleCoverageTests(TestCase):
    SAMPLE_TOPICS = {
        "A1": "health",
        "A2": "weather-nature",
        "B1": "b1-media-internet",
        "B2": "b2-news",
        "C1": "c1-style-register",
        "C2": "c2-semantic-precision",
    }

    def test_representative_topic_per_level_has_complete_learning_path(self):
        for level, topic_id in self.SAMPLE_TOPICS.items():
            with self.subTest(level=level, topic_id=topic_id):
                topic = Topic.objects.select_related("course").get(id=topic_id)
                self.assertTrue(topic.is_active)
                self.assertEqual(topic.course.level, level)

                lessons = topic.lessons.filter(is_active=True)
                self.assertGreaterEqual(lessons.count(), 5)
                self.assertGreaterEqual(
                    sum(lesson.flashcard_links.count() for lesson in lessons), 15
                )

                questions = [
                    question
                    for lesson in lessons
                    for question in lesson.questions.filter(is_active=True)
                ]
                self.assertGreaterEqual(len(questions), 16)
                for question in questions:
                    self.assertGreaterEqual(len(question.options), 2)
                    self.assertLess(question.correct, len(question.options))
                    self.assertTrue(question.explanation.strip())

                reading = ReadingText.objects.get(topic=topic, is_active=True)
                self.assertEqual(reading.level, level)
                self.assertGreaterEqual(len(reading.paragraphs), 3)
                self.assertTrue(reading.glossary)
                self.assertEqual(reading.source_metadata.get("origin"), "original")
                self.assertTrue(
                    reading.source_metadata.get("comprehension_lesson_id", "").strip()
                )

    def test_empty_legacy_topic_is_not_part_of_active_catalog(self):
        legacy_topic = Topic.objects.get(id="first-steps")
        self.assertFalse(legacy_topic.is_active)
        self.assertFalse(Lesson.objects.filter(topic=legacy_topic, is_active=True).exists())

    def test_sampled_c1_c2_cards_use_context_instead_of_seed_templates(self):
        cards = Flashcard.objects.filter(id__regex=r"^c(11|21)-")
        self.assertEqual(cards.count(), 30)
        for card in cards:
            with self.subTest(card_id=card.id):
                self.assertNotIn("W tej wypowiedzi ważne", card.example)
                self.assertNotIn("W analizie świadomie stosujemy", card.example)
                self.assertGreaterEqual(len(card.example.split()), 7)
