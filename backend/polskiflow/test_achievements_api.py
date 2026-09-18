from unittest.mock import patch

from django.test import TestCase, override_settings

from polskiflow.auth import SupabaseUser
from polskiflow.progress_store import DashboardProgress


@override_settings(SUPABASE_URL="https://example.supabase.co", SUPABASE_ANON_KEY="anon")
class AchievementsApiTests(TestCase):
    authorization = {"HTTP_AUTHORIZATION": "Bearer owner-token"}

    def _auth(self):
        return patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser(id="owner-1", email="ada@example.com"),
        )

    def _progress(self, available=True):
        return DashboardProgress(
            "Ada", "B1", 4, frozenset(), available,
            all_completed_lesson_ids=frozenset({"lesson-1", "lesson-2", "stale"}),
            active_days=12,
        )

    def test_requires_bearer_and_derives_bounded_progress_without_owner_data(self):
        lessons = [{"id": "lesson-1"}, {"id": "lesson-2"}, {"id": "lesson-3"}]
        words = [{"id": str(index)} for index in range(25)]
        self.client.cookies["polskiflow_access_token"] = "cookie-token"
        with self._auth(), patch("polskiflow.api_views.load_dashboard_progress") as load:
            rejected = self.client.get("/api/v1/me/achievements/")
        self.assertEqual(rejected.status_code, 401)
        load.assert_not_called()

        with self._auth(), patch(
            "polskiflow.api_views.load_dashboard_progress", return_value=self._progress()
        ) as load, patch(
            "polskiflow.api_views.load_personal_words", return_value=words
        ) as dictionary, patch("polskiflow.api_views.tasks", return_value=lessons):
            response = self.client.get("/api/v1/me/achievements/", **self.authorization)
        self.assertEqual(response.status_code, 200)
        data = response.json()["data"]
        self.assertEqual(data["achievement_count"], 7)
        self.assertEqual(data["unlocked_count"], 4)
        by_id = {item["id"]: item for item in data["achievements"]}
        self.assertEqual(by_id["momentum"]["current"], 2)
        self.assertEqual(by_id["word-collector"]["progress_percent"], 100)
        self.assertTrue(by_id["steady-month"]["unlocked"])
        self.assertNotIn("owner-1", str(data))
        self.assertNotIn("ada@example.com", str(data))
        self.assertEqual(response["Cache-Control"], "private, no-store")
        load.assert_called_once_with("owner-token", "owner-1", "ada")
        dictionary.assert_called_once_with("owner-token", "owner-1")

    def test_upstream_failure_returns_503_without_partial_achievements(self):
        for progress, words in ((self._progress(False), []), (self._progress(), None)):
            with self.subTest(progress=progress.available, words=words), self._auth(), patch(
                "polskiflow.api_views.load_dashboard_progress", return_value=progress
            ), patch("polskiflow.api_views.load_personal_words", return_value=words):
                response = self.client.get("/api/v1/me/achievements/", **self.authorization)
            self.assertEqual(response.status_code, 503)
            self.assertEqual(response.json()["error"]["code"], "upstream_unavailable")
            self.assertNotIn("data", response.json())

    def test_supports_head_rejects_post_and_is_in_openapi(self):
        with self._auth(), patch(
            "polskiflow.api_views.load_dashboard_progress", return_value=self._progress()
        ), patch("polskiflow.api_views.load_personal_words", return_value=[]), patch(
            "polskiflow.api_views.tasks", return_value=[]
        ):
            head = self.client.head("/api/v1/me/achievements/", **self.authorization)
            post = self.client.post("/api/v1/me/achievements/", **self.authorization)
        self.assertEqual(head.status_code, 200)
        self.assertEqual(post.status_code, 405)
        operation = self.client.get("/api/v1/openapi.json").json()["paths"]["/api/v1/me/achievements/"]["get"]
        self.assertEqual(operation["security"], [{"supabaseBearer": []}])
