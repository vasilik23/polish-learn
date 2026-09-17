import json
from unittest.mock import MagicMock, patch

from django.test import SimpleTestCase, override_settings

from polskiflow.api_rate_limit_store import consume_distributed_api_mutation


@override_settings(SUPABASE_URL="https://project.supabase.co", SUPABASE_ANON_KEY="public", SUPABASE_AUTH_TIMEOUT=2)
class ApiRateLimitStoreTests(SimpleTestCase):
    @patch("polskiflow.api_rate_limit_store.urlopen")
    def test_rpc_uses_user_token_and_only_fixed_action_input(self, urlopen):
        response = MagicMock(); response.read.return_value = b'[{"allowed":false,"retry_after":17}]'
        urlopen.return_value.__enter__.return_value = response
        result = consume_distributed_api_mutation("access", "profile")
        self.assertEqual(result, (False, 17))
        request = urlopen.call_args.args[0]
        self.assertTrue(request.full_url.endswith("/rest/v1/rpc/consume_api_mutation"))
        self.assertEqual(request.headers["Authorization"], "Bearer access")
        self.assertEqual(json.loads(request.data), {"p_action": "profile"})
        self.assertNotIn("user_id", json.loads(request.data))
        self.assertNotIn("limit", json.loads(request.data))

    @patch("polskiflow.api_rate_limit_store.urlopen")
    def test_invalid_rpc_response_falls_back_safely(self, urlopen):
        response = MagicMock(); response.read.return_value = b'[]'
        urlopen.return_value.__enter__.return_value = response
        self.assertIsNone(consume_distributed_api_mutation("access", "profile"))

    @override_settings(SUPABASE_URL="", SUPABASE_ANON_KEY="")
    def test_unconfigured_store_uses_local_fallback(self):
        self.assertIsNone(consume_distributed_api_mutation("access", "profile"))
