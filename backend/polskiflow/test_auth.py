import io
import json
from unittest.mock import patch

from django.test import SimpleTestCase, override_settings

from polskiflow.auth import SupabaseUser, authenticate_access_token


class _Response(io.BytesIO):
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
