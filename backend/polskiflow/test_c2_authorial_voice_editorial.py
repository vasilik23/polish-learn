from django.test import TestCase
from polskiflow.learning.models import Question
class C2AuthorialVoiceEditorialTests(TestCase):
 def test_quiz_explanations_teach_style(self):
  qs=Question.objects.filter(lesson_id='c29-quiz');self.assertEqual(qs.count(),10)
  for q in qs:self.assertNotIn('oznacza:',q.explanation);self.assertGreaterEqual(len(q.explanation.split()),12)
