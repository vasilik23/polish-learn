from django.test import TestCase
from polskiflow.learning.models import Question
class B1FinalEditorialTests(TestCase):
 def test_weakest_quiz_explanations_are_expanded(self):
  for q in Question.objects.filter(lesson_id='b1final-quiz',position__in=[0,3,5,6,7,8]):self.assertGreaterEqual(len(q.explanation.split()),10)
