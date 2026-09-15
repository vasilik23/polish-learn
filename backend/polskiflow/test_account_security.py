from unittest.mock import patch

from django.test import SimpleTestCase, override_settings

from polskiflow.auth import ACCESS_COOKIE, REFRESH_COOKIE, SupabaseAuthError, SupabaseUser


@override_settings(AUTH_COOKIE_SECURE=False)
class AccountSecurityTests(SimpleTestCase):
    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        self.client.cookies[REFRESH_COOKIE] = "refresh"
        auth = patch("polskiflow.auth.authenticate_access_token", return_value=SupabaseUser("user-1", "learner@example.com"))
        auth.start()
        self.addCleanup(auth.stop)

    def test_page_is_private_and_not_cached(self):
        response = self.client.get("/account/security/")
        self.assertContains(response, "Безопасность")
        self.assertContains(response, 'autocomplete="current-password"')
        self.assertContains(response, 'autocomplete="new-password"', count=2)
        self.assertEqual(response["Cache-Control"], "private, no-store")

    @patch("polskiflow.account_views.update_password")
    def test_valid_change_uses_current_session_then_clears_cookies(self, update):
        response = self.client.post("/account/security/", {
            "current_password": "OldPassword2026",
            "password": "NewPassword2026",
            "password_confirmation": "NewPassword2026",
        })
        update.assert_called_once_with("access", "NewPassword2026", current_password="OldPassword2026")
        self.assertRedirects(response, "/login/?password_changed=1", fetch_redirect_response=False)
        self.assertEqual(response.cookies[ACCESS_COOKIE]["max-age"], 0)
        self.assertEqual(response.cookies[REFRESH_COOKIE]["max-age"], 0)

    @patch("polskiflow.account_views.update_password")
    def test_invalid_input_never_reaches_supabase(self, update):
        response = self.client.post("/account/security/", {
            "current_password": "SamePassword2026",
            "password": "SamePassword2026",
            "password_confirmation": "SamePassword2026",
        })
        self.assertContains(response, "должен отличаться")
        update.assert_not_called()

    @patch("polskiflow.account_views.update_password", side_effect=SupabaseAuthError("sensitive upstream detail"))
    def test_upstream_error_is_neutral(self, _update):
        response = self.client.post("/account/security/", {
            "current_password": "OldPassword2026",
            "password": "NewPassword2026",
            "password_confirmation": "NewPassword2026",
        })
        self.assertContains(response, "Проверьте текущий пароль или войдите заново")
        self.assertNotContains(response, "sensitive upstream detail")

    def test_requires_authentication(self):
        self.client.cookies.clear()
        self.assertEqual(self.client.get("/account/security/").status_code, 302)

    def test_login_confirms_completed_password_change(self):
        self.client.cookies.clear()
        response = self.client.get("/login/?password_changed=1")
        self.assertContains(response, "Пароль обновлён. Теперь войдите с новым паролем.")
