from django.test import TestCase

from polskiflow.learning.models import Flashcard, Question


class C2RhetoricalStrategyEditorialTests(TestCase):
    def test_flashcards_use_terms_in_natural_rhetorical_contexts(self):
        cards = Flashcard.objects.filter(id__regex=r"^c22-").order_by("position")
        self.assertEqual(cards.count(), 15)

        for card in cards:
            with self.subTest(card_id=card.id):
                self.assertIn(card.polish.lower(), card.example.lower())
                self.assertNotIn("W analizie świadomie stosujemy", card.example)
                self.assertGreaterEqual(len(card.example.split()), 10)

    def test_all_explanations_teach_rhetoric_or_cite_reading_evidence(self):
        questions = Question.objects.filter(lesson__topic_id="c2-rhetorical-strategy")
        self.assertEqual(questions.count(), 22)

        weak_templates = (
            "oznacza tutaj:",
            "Ответ прямо следует из текста.",
            "Первый вариант точно передаёт содержание абзаца.",
        )
        for question in questions:
            with self.subTest(lesson_id=question.lesson_id, position=question.position):
                self.assertGreaterEqual(len(question.explanation.split()), 12)
                for template in weak_templates:
                    self.assertNotIn(template, question.explanation)

        dilemma = questions.get(lesson_id="c22-grammar", position=5)
        self.assertIn("pozorny dylemat", dilemma.explanation)
        evidence = questions.get(lesson_id="c22-reading-check", position=3)
        self.assertIn("Trzeci akapit", evidence.explanation)
