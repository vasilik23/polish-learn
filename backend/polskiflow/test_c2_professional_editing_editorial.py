from django.test import TestCase
from polskiflow.learning.models import Flashcard,Question
class C2ProfessionalEditingEditorialTests(TestCase):
 def test_templates_are_replaced(self):
  cards=Flashcard.objects.filter(id__regex=r"^c24-");self.assertEqual(cards.count(),15)
  for card in cards:
   self.assertNotIn("W redagowanym tekście świadomie",card.example);self.assertGreaterEqual(len(card.example.split()),10)
  questions=Question.objects.filter(lesson_id="c24-quiz");self.assertEqual(questions.count(),10)
  for question in questions:
   self.assertNotIn("oznacza:",question.explanation);self.assertGreaterEqual(len(question.explanation.split()),12)
