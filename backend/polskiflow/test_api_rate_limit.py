import json
from unittest.mock import patch

from django.core.cache import cache
from django.test import SimpleTestCase, TestCase, override_settings

from polskiflow.auth import SupabaseUser
from polskiflow.domain.api_rate_limit import consume_api_mutation
from polskiflow.progress_store import DashboardProgress


@override_settings(API_MUTATION_RATE_LIMITS={"profile": (2, 60), "sm2": (1, 30)})
class ApiMutationRateLimitDomainTests(SimpleTestCase):
    def setUp(self):
        cache.clear()

    def test_limit_is_scoped_by_hashed_user_and_action(self):
        self.assertTrue(consume_api_mutation("user-1", "profile")[0])
        self.assertTrue(consume_api_mutation("user-1", "profile")[0])
        self.assertFalse(consume_api_mutation("user-1", "profile")[0])
        self.assertTrue(consume_api_mutation("user-2", "profile")[0])
        self.assertTrue(consume_api_mutation("user-1", "sm2")[0])
        self.assertFalse(consume_api_mutation("user-1", "sm2")[0])


@override_settings(
    SUPABASE_URL="https://example.supabase.co", SUPABASE_ANON_KEY="anon",
    API_MUTATION_RATE_LIMITS={"profile": (1, 60)},
)
class ApiMutationRateLimitViewTests(TestCase):
    authorization = {"HTTP_AUTHORIZATION": "Bearer owner-token"}

    def setUp(self):
        cache.clear()

    def _auth(self):
        return patch("polskiflow.auth.authenticate_access_token", return_value=SupabaseUser(id="owner-1", email="owner@example.com"))

    def test_second_profile_mutation_returns_private_429_before_write(self):
        progress = DashboardProgress("Owner", "A1", 0, frozenset(), True, daily_goal_lessons=4)
        with self._auth(), patch("polskiflow.api_views.load_dashboard_progress", return_value=progress), patch(
            "polskiflow.api_views.save_profile_settings", return_value=True
        ) as save:
            first = self.client.patch(
                "/api/v1/me/profile/", data=json.dumps({"level": "A2"}),
                content_type="application/json", **self.authorization,
            )
            limited = self.client.patch(
                "/api/v1/me/profile/", data=json.dumps({"level": "B1"}),
                content_type="application/json", **self.authorization,
            )
        self.assertEqual(first.status_code, 200)
        self.assertEqual(limited.status_code, 429)
        self.assertEqual(limited["Retry-After"], "60")
        self.assertEqual(limited["Cache-Control"], "private, no-store")
        self.assertEqual(limited.json()["error"]["code"], "rate_limited")
        self.assertEqual(save.call_count, 1)

    def test_reads_and_invalid_bearer_do_not_consume_mutation_budget(self):
        progress = DashboardProgress("Owner", "A1", 0, frozenset(), True, daily_goal_lessons=4)
        with self._auth(), patch("polskiflow.api_views.load_dashboard_progress", return_value=progress), patch(
            "polskiflow.api_views.save_profile_settings", return_value=True
        ):
            self.assertEqual(self.client.get("/api/v1/me/profile/", **self.authorization).status_code, 200)
            self.assertEqual(self.client.patch(
                "/api/v1/me/profile/", data=json.dumps({"level": "A2"}), content_type="application/json"
            ).status_code, 401)
            accepted = self.client.patch(
                "/api/v1/me/profile/", data=json.dumps({"level": "A2"}), content_type="application/json", **self.authorization
            )
        self.assertEqual(accepted.status_code, 200)
