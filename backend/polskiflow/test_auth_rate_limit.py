from django.core.cache import cache
from unittest.mock import patch
from django.test import RequestFactory, SimpleTestCase, TestCase, override_settings
from polskiflow.auth import SupabaseAuthError

from polskiflow.domain.auth_rate_limit import consume_auth_attempt


@override_settings(AUTH_FORM_RATE_LIMITS={"login": (2, 60)}, VERCEL=True)
class AuthRateLimitTests(SimpleTestCase):
    def setUp(self):
        cache.clear()
        self.request = RequestFactory().post("/login/", HTTP_X_FORWARDED_FOR="203.0.113.1, 10.0.0.1")

    def test_limit_is_scoped_by_normalized_email_and_client(self):
        self.assertTrue(consume_auth_attempt(self.request, "login", " A@Example.com ")[0])
        self.assertTrue(consume_auth_attempt(self.request, "login", "a@example.COM")[0])
        self.assertFalse(consume_auth_attempt(self.request, "login", "a@example.com")[0])
        self.assertTrue(consume_auth_attempt(self.request, "login", "other@example.com")[0])


@override_settings(AUTH_FORM_RATE_LIMITS={"login": (1, 60), "register": (5, 60), "forgot": (5, 60), "resend": (5, 60)})
class AuthRateLimitViewTests(TestCase):
    def setUp(self):
        cache.clear()

    @patch("polskiflow.auth_views.sign_in", side_effect=SupabaseAuthError("Неверные данные"))
    def test_login_returns_generic_429_with_retry_after(self, sign_in):
        payload = {"email": "learner@example.com", "password": "wrong-password"}
        self.assertEqual(self.client.post("/login/", payload).status_code, 200)
        limited = self.client.post("/login/", payload)
        self.assertEqual(limited.status_code, 429)
        self.assertEqual(limited["Retry-After"], "60")
        self.assertEqual(limited["Cache-Control"], "private, no-store")
        self.assertContains(limited, "Слишком много попыток", status_code=429)
        self.assertEqual(sign_in.call_count, 1)
