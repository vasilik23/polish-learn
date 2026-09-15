import json
from unittest.mock import MagicMock, patch

from django.test import SimpleTestCase, TestCase, override_settings

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser
from polskiflow.progress_store import CompletionHistoryPage, load_completion_history


class CompletionHistoryStoreTests(SimpleTestCase):
    @override_settings(SUPABASE_URL="https://project.supabase.co", SUPABASE_ANON_KEY="public", SUPABASE_AUTH_TIMEOUT=2)
    @patch("polskiflow.progress_store.urlopen")
    def test_history_query_is_owner_scoped_paginated_and_bounded(self, urlopen):
        response = MagicMock()
        response.read.return_value = json.dumps([
            {"lesson_id": f"lesson-{index}", "plan_date": "2026-09-15"}
            for index in range(21)
        ]).encode()
        urlopen.return_value.__enter__.return_value = response

        result = load_completion_history("access", "user-1", page=2, days=30)

        self.assertEqual(len(result.rows), 20)
        self.assertTrue(result.has_previous)
        self.assertTrue(result.has_next)
        request = urlopen.call_args.args[0]
        self.assertEqual(request.headers["Authorization"], "Bearer access")
        self.assertIn("user_id=eq.user-1", request.full_url)
        self.assertIn("limit=21", request.full_url)
        self.assertIn("offset=20", request.full_url)
        self.assertIn("plan_date=gte.", request.full_url)


class LearningHistoryViewTests(TestCase):
    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        auth = patch("polskiflow.auth.authenticate_access_token", return_value=SupabaseUser("user-1", "a@example.com"))
        auth.start()
        self.addCleanup(auth.stop)

    @patch("polskiflow.history_views.tasks", return_value=[{"id": "words", "title": "Первые слова", "emoji": "💬", "level": "A1"}])
    @patch("polskiflow.history_views.load_completion_history")
    def test_history_renders_lesson_metadata_and_pagination(self, load, _tasks):
        load.return_value = CompletionHistoryPage(
            ({"lesson_id": "words", "plan_date": "2026-09-15", "cards_total": 8, "cards_known": 7},),
            True, False, True, 1,
        )

        response = self.client.get("/history/?period=30")

        self.assertContains(response, "История занятий")
        self.assertContains(response, "Первые слова")
        self.assertContains(response, "7 / 8")
        self.assertContains(response, "Старее")
        load.assert_called_once_with("access", "user-1", page=1, days=30)

    @patch("polskiflow.history_views.tasks", return_value=[])
    @patch("polskiflow.history_views.load_completion_history", return_value=CompletionHistoryPage((), True, False, False, 1))
    def test_invalid_filters_fall_back_and_empty_state_is_honest(self, load, _tasks):
        response = self.client.get("/history/?period=invalid&page=nope")
        self.assertContains(response, "Пока нет завершённых занятий")
        load.assert_called_once_with("access", "user-1", page=1, days=30)

    def test_history_requires_authentication(self):
        self.client.cookies.clear()
        self.assertEqual(self.client.get("/history/").status_code, 302)
