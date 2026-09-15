from unittest.mock import patch

from django.test import TestCase, override_settings

from polskiflow.auth import SupabaseUser
from polskiflow.progress_store import CompletionHistoryPage


@override_settings(SUPABASE_URL="https://example.supabase.co", SUPABASE_ANON_KEY="anon")
class LearnerHistoryApiTests(TestCase):
    headers = {"HTTP_AUTHORIZATION": "Bearer learner-token"}

    def auth(self):
        return patch("polskiflow.auth.authenticate_access_token", return_value=SupabaseUser("user-123", "ada@example.com"))

    def test_requires_explicit_bearer_even_with_browser_cookie(self):
        self.assertEqual(self.client.get("/api/v1/me/history/").status_code, 401)
        with self.auth():
            self.client.cookies["polskiflow_access_token"] = "learner-token"
            response = self.client.get("/api/v1/me/history/")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["error"]["code"], "bearer_required")

    @patch("polskiflow.api_views.load_completion_history")
    def test_returns_stable_private_owner_scoped_page(self, load):
        load.return_value = CompletionHistoryPage(({
            "lesson_id": "words", "plan_date": "2026-09-15", "cards_total": 8, "cards_known": 7,
        },), True, True, False, 2)
        with self.auth():
            response = self.client.get("/api/v1/me/history/?period=90&page=2", **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Cache-Control"], "private, no-store")
        self.assertEqual(response.json()["meta"]["contract"], "learner-history")
        self.assertEqual(response.json()["data"]["completions"][0]["lesson_id"], "words")
        self.assertNotIn("user-123", str(response.json()))
        load.assert_called_once_with("learner-token", "user-123", page=2, page_size=50, days=90)

    def test_rejects_invalid_query_without_store_call(self):
        with self.auth(), patch("polskiflow.api_views.load_completion_history") as load:
            response = self.client.get("/api/v1/me/history/?period=year&page=0", **self.headers)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"]["code"], "invalid_pagination")
        load.assert_not_called()

    @patch("polskiflow.api_views.load_completion_history", return_value=CompletionHistoryPage((), False, False, False, 1))
    def test_reports_upstream_failure_instead_of_empty_success(self, _load):
        with self.auth():
            response = self.client.get("/api/v1/me/history/", **self.headers)
        self.assertEqual(response.status_code, 503)
