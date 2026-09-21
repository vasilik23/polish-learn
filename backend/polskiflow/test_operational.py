from unittest.mock import patch

from django.test import SimpleTestCase, override_settings


class OperationalProbeTests(SimpleTestCase):
    databases = {"default"}

    def test_liveness_does_not_query_dependencies(self):
        with patch("polskiflow.operational_views._database_ready") as database_ready:
            response = self.client.get("/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})
        self.assertEqual(response["Cache-Control"], "no-store")
        database_ready.assert_not_called()

    def test_readiness_reports_healthy_dependencies(self):
        response = self.client.get("/ready/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "status": "ready",
                "checks": {"database": "ok", "configuration": "ok"},
            },
        )
        self.assertEqual(response["Cache-Control"], "no-store")

    @patch("polskiflow.operational_views._database_ready", return_value=False)
    def test_readiness_returns_503_without_exposing_database_error(self, _database_ready):
        response = self.client.get("/ready/")

        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.json()["checks"]["database"], "unavailable")
        self.assertNotContains(response, "password", status_code=503)

    @override_settings(VERCEL=True, SUPABASE_URL="", SUPABASE_ANON_KEY="")
    def test_production_readiness_requires_supabase_configuration(self):
        response = self.client.get("/ready/")

        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.json()["checks"]["configuration"], "unavailable")
