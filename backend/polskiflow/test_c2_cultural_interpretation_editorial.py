from django.test import TestCase
from polskiflow.learning.models import Question
class C2CulturalInterpretationEditorialTests(TestCase):
 def test_quiz_explanations_teach_concepts(self):
  qs=Question.objects.filter(lesson_id='c26-quiz');self.assertEqual(qs.count(),10)
  for q in qs:self.assertNotIn('oznacza:',q.explanation);self.assertGreaterEqual(len(q.explanation.split()),12)
