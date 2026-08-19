import io
import json
from unittest.mock import patch

from django.test import SimpleTestCase, override_settings

from polskiflow.auth import (
    ACCESS_COOKIE,
    REFRESH_COOKIE,
    SupabaseAuthError,
    SupabaseSession,
    SupabaseUser,
    authenticate_access_token,
    sign_in,
)


class _Response(io.BytesIO):
    status = 200

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        self.close()


@override_settings(
    SUPABASE_URL="https://project.supabase.co",
    SUPABASE_ANON_KEY="public-anon-key",
    SUPABASE_AUTH_TIMEOUT=2,
)
class SupabaseAuthTests(SimpleTestCase):
    @patch("polskiflow.auth.urlopen")
    def test_valid_token_populates_current_user(self, urlopen):
        urlopen.return_value = _Response(
            json.dumps({"id": "user-123", "email": "learner@example.com"}).encode()
        )

        response = self.client.get(
            "/api/auth/me/", headers={"Authorization": "Bearer access-token"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], "user-123")
        request = urlopen.call_args.args[0]
        self.assertEqual(request.get_header("Authorization"), "Bearer access-token")
        self.assertEqual(request.get_header("Apikey"), "public-anon-key")

    def test_missing_token_is_rejected(self):
        response = self.client.get("/api/auth/me/")
        self.assertEqual(response.status_code, 401)

    @override_settings(SUPABASE_URL="", SUPABASE_ANON_KEY="")
    def test_authentication_is_disabled_without_configuration(self):
        self.assertIsNone(authenticate_access_token("token"))

    @patch("polskiflow.auth.authenticate_access_token")
    def test_middleware_exposes_verified_user(self, authenticate):
        authenticate.return_value = SupabaseUser("user-456", None)
        response = self.client.get(
            "/api/auth/me/", headers={"Authorization": "Bearer token"}
        )
        self.assertEqual(response.json(), {"id": "user-456", "email": None})

    @patch("polskiflow.auth.urlopen")
    def test_password_sign_in_returns_session(self, urlopen):
        urlopen.return_value = _Response(
            json.dumps(
                {
                    "access_token": "access",
                    "refresh_token": "refresh",
                    "expires_in": 3600,
                    "user": {"id": "user-123", "email": "learner@example.com"},
                }
            ).encode()
        )

        session = sign_in("learner@example.com", "password")

        self.assertEqual(session.access_token, "access")
        request = urlopen.call_args.args[0]
        self.assertTrue(request.full_url.endswith("/auth/v1/token?grant_type=password"))
        self.assertEqual(json.loads(request.data), {
            "email": "learner@example.com",
            "password": "password",
        })

    @patch("polskiflow.auth.refresh_session")
    @patch("polskiflow.auth.authenticate_access_token")
    def test_expired_cookie_session_is_refreshed(self, authenticate, refresh):
        authenticate.return_value = None
        refresh.return_value = SupabaseSession(
            "new-access",
            "new-refresh",
            3600,
            SupabaseUser("user-789", "renewed@example.com"),
        )
        self.client.cookies[ACCESS_COOKIE] = "expired-access"
        self.client.cookies[REFRESH_COOKIE] = "refresh"

        response = self.client.get("/api/auth/me/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], "user-789")
        self.assertEqual(response.cookies[ACCESS_COOKIE].value, "new-access")
        self.assertTrue(response.cookies[ACCESS_COOKIE]["httponly"])


@override_settings(AUTH_COOKIE_SECURE=False)
class BrowserAuthTests(SimpleTestCase):
    @patch("polskiflow.auth_views.sign_in")
    def test_login_sets_http_only_cookies_and_redirects(self, login):
        login.return_value = SupabaseSession(
            "access",
            "refresh",
            3600,
            SupabaseUser("user-123", "learner@example.com"),
        )

        response = self.client.post(
            "/login/?next=/lesson/words",
            {"email": "learner@example.com", "password": "password", "next": "/lesson/words"},
        )

        self.assertRedirects(response, "/lesson/words", fetch_redirect_response=False)
        self.assertTrue(response.cookies[ACCESS_COOKIE]["httponly"])
        self.assertEqual(response.cookies[REFRESH_COOKIE]["samesite"], "Lax")

    @patch("polskiflow.auth_views.sign_in")
    def test_login_rejects_external_next_url(self, login):
        login.return_value = SupabaseSession(
            "access", "refresh", 3600, SupabaseUser("user-123", None)
        )

        response = self.client.post(
            "/login/",
            {"email": "a@example.com", "password": "password", "next": "https://evil.example"},
        )

        self.assertRedirects(response, "/", fetch_redirect_response=False)

    @patch("polskiflow.auth_views.sign_in")
    def test_login_displays_safe_auth_error(self, login):
        login.side_effect = SupabaseAuthError("Invalid login credentials")
        response = self.client.post(
            "/login/", {"email": "a@example.com", "password": "wrong-password"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid login credentials")

    def test_protected_page_redirects_guest_to_login(self):
        response = self.client.get("/")
        self.assertRedirects(response, "/login/?next=%2F", fetch_redirect_response=False)

    @patch("polskiflow.auth_views.sign_up")
    def test_registration_waits_for_email_confirmation(self, signup):
        signup.return_value = None
        response = self.client.post(
            "/register/", {"email": "new@example.com", "password": "password"}
        )
        self.assertContains(response, "Подтвердите email")

    @patch("polskiflow.auth_views.sign_out")
    @patch("polskiflow.auth.authenticate_access_token")
    def test_logout_clears_auth_cookies(self, authenticate, logout):
        authenticate.return_value = SupabaseUser("user-123", "learner@example.com")
        self.client.cookies[ACCESS_COOKIE] = "access"
        self.client.cookies[REFRESH_COOKIE] = "refresh"

        response = self.client.post("/logout/")

        logout.assert_called_once_with("access")
        self.assertRedirects(response, "/login/", fetch_redirect_response=False)
        self.assertEqual(response.cookies[ACCESS_COOKIE]["max-age"], 0)
