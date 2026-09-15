from unittest.mock import patch

from django.test import TestCase

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser
from polskiflow.progress_store import DashboardProgress


class ProfileExportTests(TestCase):
    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        auth = patch("polskiflow.auth.authenticate_access_token", return_value=SupabaseUser("user-123", "anna@example.com"))
        auth.start(); self.addCleanup(auth.stop)

    @patch("polskiflow.auth_views.load_reading_bookmarks", return_value={"story-b"})
    @patch("polskiflow.auth_views.load_personal_words", return_value=[{"word": "dom"}])
    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_export_is_private_download_without_tokens(self, dashboard, _words, _bookmarks):
        dashboard.return_value = DashboardProgress(display_name="Anna", level="B1", streak_days=3, completed_lesson_ids=frozenset(), available=True, all_completed_lesson_ids=frozenset({"b", "a"}), active_days=5)
        response = self.client.get("/profile/export/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Cache-Control"], "private, no-store")
        self.assertIn("attachment", response["Content-Disposition"])
        self.assertEqual(response.json()["progress"]["completed_lesson_ids"], ["a", "b"])
        self.assertNotIn("token", response.content.decode().lower())

    def test_export_requires_authentication(self):
        self.client.cookies.clear()
        self.assertEqual(self.client.get("/profile/export/").status_code, 302)
