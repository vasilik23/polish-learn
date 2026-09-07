from django.test import TestCase

from polskiflow.learning.models import Flashcard, Question


class C1FinalProjectEditorialTests(TestCase):
    def test_flashcards_use_terms_in_natural_project_contexts(self):
        cards = Flashcard.objects.filter(id__regex=r"^c110-").order_by("position")
        self.assertEqual(cards.count(), 15)

        for card in cards:
            with self.subTest(card_id=card.id):
                self.assertIn(card.polish.lower(), card.example.lower())
                self.assertNotIn("W tej wypowiedzi ważne", card.example)
                self.assertGreaterEqual(len(card.example.split()), 10)

    def test_all_explanations_teach_project_concepts_or_reading_evidence(self):
        questions = Question.objects.filter(lesson__topic_id="c1-final-project")
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

        triangulation = questions.get(lesson_id="c110-grammar", position=2)
        self.assertIn("różnych rodzajów dowodów", triangulation.explanation)
        evidence = questions.get(lesson_id="c110-reading-check", position=0)
        self.assertIn("Trzeci akapit", evidence.explanation)
