from unittest.mock import patch

from django.test import TestCase


class NewsApiTests(TestCase):
    @patch("polskiflow.api_views.latest_official_news")
    def test_public_news_api_returns_bounded_attributed_headlines(self, latest):
        latest.return_value = [{
            "title": "Wiadomość dnia", "url": "https://www.rmf24.pl/example",
            "source": "RMF24", "category": "politics",
            "category_label": "Polityka", "published": "17.09.2026",
            "published_sort": 123.0,
        }]
        response = self.client.get("/api/v1/news/?category=politics&limit=3")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertTrue(payload["meta"]["available"])
        self.assertTrue(payload["meta"]["external_content"])
        self.assertEqual(payload["data"]["category"], "politics")
        self.assertEqual(payload["data"]["headlines"][0]["source"], "RMF24")
        self.assertNotIn("published_sort", payload["data"]["headlines"][0])
        latest.assert_called_once_with(limit=3, category="politics")
        self.assertIn("public", response["Cache-Control"])

    @patch("polskiflow.api_views.latest_official_news", return_value=[])
    def test_empty_snapshot_is_honest_and_successful(self, _latest):
        response = self.client.get("/api/v1/news/")
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()["meta"]["available"])
        self.assertEqual(response.json()["data"]["headlines"], [])

    def test_invalid_filters_and_mutations_are_rejected(self):
        for query in ("category=unknown", "limit=0", "limit=13", "limit=nope"):
            with self.subTest(query=query):
                self.assertEqual(self.client.get(f"/api/v1/news/?{query}").status_code, 400)
        self.assertEqual(self.client.post("/api/v1/news/").status_code, 405)

    def test_openapi_describes_public_news_contract(self):
        operation = self.client.get("/api/v1/openapi.json").json()["paths"]["/api/v1/news/"]["get"]
        self.assertEqual(operation["operationId"], "getNewsHeadlines")
        self.assertNotIn("security", operation)
