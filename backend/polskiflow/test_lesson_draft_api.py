import json
from unittest.mock import patch

from django.test import TestCase, override_settings

from polskiflow.auth import SupabaseUser
from polskiflow.lesson_draft_store import LessonDraftLoadResult


@override_settings(SUPABASE_URL="https://example.supabase.co", SUPABASE_ANON_KEY="anon")
class LessonDraftApiTests(TestCase):
    authorization = {"HTTP_AUTHORIZATION": "Bearer owner-token"}

    def _auth(self):
        return patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser(id="owner-1", email="owner@example.com"),
        )

    def test_latest_requires_bearer_and_distinguishes_empty_from_failure(self):
        self.client.cookies["polskiflow_access_token"] = "cookie-token"
        with self._auth(), patch("polskiflow.api_views.load_latest_lesson_draft_result") as load:
            rejected = self.client.get("/api/v1/me/lesson-drafts/latest/")
        self.assertEqual(rejected.status_code, 401)
        load.assert_not_called()

        for result, status, expected in (
            (LessonDraftLoadResult(True), 200, None),
            (LessonDraftLoadResult(False), 503, "upstream_unavailable"),
        ):
            with self.subTest(status=status), self._auth(), patch(
                "polskiflow.api_views.load_latest_lesson_draft_result", return_value=result
            ):
                response = self.client.get(
                    "/api/v1/me/lesson-drafts/latest/", **self.authorization
                )
            self.assertEqual(response.status_code, status)
            value = response.json()["data"]["draft"] if status == 200 else response.json()["error"]["code"]
            self.assertEqual(value, expected)

    def test_latest_returns_owner_scoped_safe_draft(self):
        draft = {"lesson_id": "lesson-1", "lesson_kind": "quiz", "step_index": 2, "score": 1, "updated_at": "2026-09-15T10:00:00Z"}
        with self._auth(), patch(
            "polskiflow.api_views.load_latest_lesson_draft_result",
            return_value=LessonDraftLoadResult(True, draft),
        ) as load:
            response = self.client.get("/api/v1/me/lesson-drafts/latest/", **self.authorization)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"]["draft"], draft)
        load.assert_called_once_with("owner-token", "owner-1")
        self.assertNotIn("owner-1", str(response.json()))

    def test_put_derives_owner_and_kind_server_side(self):
        with self._auth(), patch("polskiflow.api_views.task", return_value={"kind": "quiz"}), patch(
            "polskiflow.api_views._lesson_step_count", return_value=5
        ), patch("polskiflow.api_views.save_lesson_draft", return_value=True) as save:
            response = self.client.put(
                "/api/v1/me/lesson-drafts/lesson-1/",
                data=json.dumps({"step_index": 2, "score": 1}),
                content_type="application/json",
                **self.authorization,
            )
        self.assertEqual(response.status_code, 200)
        save.assert_called_once_with("owner-token", "owner-1", "lesson-1", "quiz", 2, 1)
        self.assertEqual(response.json()["data"]["draft"]["lesson_kind"], "quiz")

    def test_put_rejects_ownership_content_and_invalid_progress(self):
        invalid = (
            {"step_index": 2, "score": 1, "user_id": "other"},
            {"step_index": 2, "score": 1, "answers": [0, 1]},
            {"step_index": 5, "score": 1},
            {"step_index": 2, "score": 3},
            {"step_index": True, "score": 1},
        )
        for payload in invalid:
            with self.subTest(payload=payload), self._auth(), patch(
                "polskiflow.api_views.task", return_value={"kind": "quiz"}
            ), patch("polskiflow.api_views._lesson_step_count", return_value=5), patch(
                "polskiflow.api_views.save_lesson_draft"
            ) as save:
                response = self.client.put(
                    "/api/v1/me/lesson-drafts/lesson-1/", data=json.dumps(payload),
                    content_type="application/json", **self.authorization,
                )
            self.assertEqual(response.status_code, 400)
            save.assert_not_called()

    def test_delete_is_bearer_only_owner_scoped_and_idempotent(self):
        with self._auth(), patch("polskiflow.api_views.task", return_value={"kind": "review"}), patch(
            "polskiflow.api_views.delete_lesson_draft", return_value=True
        ) as delete:
            response = self.client.delete("/api/v1/me/lesson-drafts/lesson-1/", **self.authorization)
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.json()["data"]["draft"])
        delete.assert_called_once_with("owner-token", "owner-1", "lesson-1")

    def test_unknown_lesson_and_upstream_failure_are_explicit(self):
        with self._auth(), patch("polskiflow.api_views.task", return_value=None):
            missing = self.client.delete("/api/v1/me/lesson-drafts/missing/", **self.authorization)
        with self._auth(), patch("polskiflow.api_views.task", return_value={"kind": "quiz"}), patch(
            "polskiflow.api_views.delete_lesson_draft", return_value=False
        ):
            unavailable = self.client.delete("/api/v1/me/lesson-drafts/lesson-1/", **self.authorization)
        self.assertEqual(missing.status_code, 404)
        self.assertEqual(unavailable.status_code, 503)
