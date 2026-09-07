from django.test import TestCase

from polskiflow.learning.models import Flashcard, Question


class C2ExpertMediationEditorialTests(TestCase):
    def test_flashcards_use_terms_in_natural_mediation_contexts(self):
        cards = Flashcard.objects.filter(id__regex=r"^c27-").order_by("position")
        self.assertEqual(cards.count(), 15)
        for card in cards:
            with self.subTest(card_id=card.id):
                self.assertIn(card.polish.lower(), card.example.lower())
                self.assertNotIn("W analizie świadomie stosujemy", card.example)
                self.assertGreaterEqual(len(card.example.split()), 10)

    def test_explanations_teach_mediation_or_cite_reading_evidence(self):
        questions = Question.objects.filter(lesson__topic_id="c2-expert-mediation")
        self.assertEqual(questions.count(), 22)
        for question in questions:
            with self.subTest(lesson_id=question.lesson_id, position=question.position):
                self.assertGreaterEqual(len(question.explanation.split()), 12)
                self.assertNotIn("oznacza:", question.explanation)
        self.assertIn("mandat decyzyjny", questions.get(lesson_id="c27-grammar", position=5).explanation)
        self.assertIn("pierwszym akapicie", questions.get(lesson_id="c27-reading-check", position=0).explanation)
