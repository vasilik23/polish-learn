from django.test import TestCase
from polskiflow.learning.models import Flashcard, Question


class C2ResearchSynthesisEditorialTests(TestCase):
    def test_examples_are_natural_research_contexts(self):
        cards = Flashcard.objects.filter(id__regex=r"^c28-").order_by("position")
        self.assertEqual(cards.count(), 15)
        for card in cards:
            with self.subTest(card=card.id):
                self.assertIn(card.polish.lower(), card.example.lower())
                self.assertNotIn("W analizie świadomie stosujemy", card.example)
                self.assertGreaterEqual(len(card.example.split()), 10)

    def test_explanations_teach_evidence_or_cite_text(self):
        questions = Question.objects.filter(lesson__topic_id="c2-research-synthesis")
        self.assertEqual(questions.count(), 22)
        for question in questions:
            with self.subTest(lesson=question.lesson_id, position=question.position):
                self.assertGreaterEqual(len(question.explanation.split()), 12)
                self.assertNotIn("oznacza:", question.explanation)
