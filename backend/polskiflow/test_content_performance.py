from django.test import TestCase
from polskiflow.content import course_topics

class CatalogPerformanceTests(TestCase):
    def test_catalog_has_fixed_two_query_budget(self):
        with self.assertNumQueries(2):
            course_topics()
