from django.test import TestCase
from polskiflow.learning.models import Question
class B1EcologyEditorialTests(TestCase):
 def test_explanations_teach_rules_and_evidence(self):
  qs=Question.objects.filter(lesson__topic_id='b1-ecology');self.assertEqual(qs.count(),22)
  for q in qs:self.assertGreaterEqual(len(q.explanation.split()),9)
