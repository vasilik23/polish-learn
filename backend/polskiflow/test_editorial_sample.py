from django.test import TestCase

from polskiflow.learning.models import Flashcard, Lesson, Question, ReadingText, Topic


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

    def test_sampled_c1_explanations_teach_instead_of_repeating_answers(self):
        questions = Question.objects.filter(lesson__topic_id="c1-style-register")
        self.assertEqual(questions.count(), 22)

        weak_templates = (
            "oznacza:",
            "Ответ прямо следует из текста.",
            "Первый вариант точно передаёт содержание абзаца.",
        )
        for question in questions:
            with self.subTest(lesson_id=question.lesson_id, position=question.position):
                self.assertGreaterEqual(len(question.explanation.split()), 10)
                for template in weak_templates:
                    self.assertNotIn(template, question.explanation)

        register = questions.get(lesson_id="c11-grammar", position=0)
        self.assertIn("ситуации, цели и отношений", register.explanation)
        conclusion = questions.get(lesson_id="c11-reading-check", position=5)
        self.assertIn("соответствием адресату", conclusion.explanation)

    def test_c1_analytical_reading_uses_contextual_examples_and_explanations(self):
        cards = Flashcard.objects.filter(id__regex=r"^c13-")
        self.assertEqual(cards.count(), 15)
        for card in cards:
            with self.subTest(card_id=card.id):
                self.assertNotIn("W tej wypowiedzi ważne", card.example)
                self.assertGreaterEqual(len(card.example.split()), 10)

        questions = Question.objects.filter(lesson__topic_id="c1-analytical-reading")
        self.assertEqual(questions.count(), 22)
        weak_templates = (
            "oznacza:",
            "Ответ прямо следует из текста.",
            "Первый вариант точно передаёт содержание абзаца.",
        )
        for question in questions:
            with self.subTest(lesson_id=question.lesson_id, position=question.position):
                self.assertGreaterEqual(len(question.explanation.split()), 12)
                for template in weak_templates:
                    self.assertNotIn(template, question.explanation)

        omission = questions.get(lesson_id="c13-grammar", position=3)
        self.assertIn("nieobecny fakt", omission.explanation)
        reading_method = questions.get(lesson_id="c13-reading-check", position=4)
        self.assertIn("przykłady, źródła i ramę tekstu", reading_method.explanation)

    def test_c1_mediation_uses_contextual_examples_and_teaching_explanations(self):
        cards = Flashcard.objects.filter(id__regex=r"^c14-")
        self.assertEqual(cards.count(), 15)
        for card in cards:
            with self.subTest(card_id=card.id):
                self.assertNotIn("W tej wypowiedzi ważne", card.example)
                self.assertGreaterEqual(len(card.example.split()), 10)

        questions = Question.objects.filter(lesson__topic_id="c1-mediation")
        self.assertEqual(questions.count(), 22)
        weak_templates = (
            "oznacza:",
            "Ответ прямо следует из текста.",
            "Первый вариант точно передаёт содержание абзаца.",
        )
        for question in questions:
            with self.subTest(lesson_id=question.lesson_id, position=question.position):
                self.assertGreaterEqual(len(question.explanation.split()), 12)
                for template in weak_templates:
                    self.assertNotIn(template, question.explanation)

        faithful_summary = questions.get(lesson_id="c14-grammar", position=5)
        self.assertIn("zakres prawdziwości", faithful_summary.explanation)
        analogy = questions.get(lesson_id="c14-reading-check", position=0)
        self.assertIn("granicę analogii", analogy.explanation)
