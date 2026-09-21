import io
import json
import os
from unittest.mock import MagicMock, patch

from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import SimpleTestCase

from polskiflow.domain.synthetic_smoke import SmokeFailure, run_synthetic_smoke


def _response(payload, *, cache="public, max-age=0", request_id="request-1"):
    response = MagicMock()
    response.__enter__.return_value = response
    response.status = 200
    response.headers = {"Cache-Control": cache, "X-Request-ID": request_id}
    response.read.return_value = json.dumps(payload).encode()
    return response


class SyntheticSmokeTests(SimpleTestCase):
    @patch("polskiflow.domain.synthetic_smoke.urlopen")
    def test_read_only_public_and_private_path_passes_without_exposing_token(self, urlopen):
        urlopen.side_effect = [
            _response({"status": "ok"}),
            _response({"status": "ready"}),
            _response({"paths": {"/api/v1/me/bootstrap/": {}}}),
            _response({"data": {"courses": []}}),
            _response({"meta": {"contract": "learner-bootstrap"}, "data": {}}, cache="private, no-store"),
            _response({"meta": {"contract": "learner-data-export"}, "data": {}}, cache="private, no-store"),
        ]

        results = run_synthetic_smoke("https://learn.example/", "secret-token")

        self.assertEqual([result.name for result in results], ["health", "ready", "openapi", "catalog", "bootstrap", "export"])
        for index, call in enumerate(urlopen.call_args_list):
            request = call.args[0]
            self.assertEqual(request.get_method(), "GET")
            if index < 4:
                self.assertNotIn("Authorization", request.headers)
            else:
                self.assertEqual(request.headers["Authorization"], "Bearer secret-token")

    def test_rejects_unsafe_origin_and_invalid_token(self):
        for base_url in ("http://example.com", "https://user:pass@example.com", "https://example.com/app/", "https://example.com/?x=1"):
            with self.subTest(base_url=base_url), self.assertRaises(SmokeFailure):
                run_synthetic_smoke(base_url, "token")
        with self.assertRaises(SmokeFailure):
            run_synthetic_smoke("https://example.com", "token with whitespace")
        with self.assertRaises(SmokeFailure):
            run_synthetic_smoke("https://example.com", "token", timeout=0)

    @patch("polskiflow.domain.synthetic_smoke.urlopen")
    def test_rejects_private_response_without_no_store(self, urlopen):
        urlopen.side_effect = [
            _response({"status": "ok"}), _response({"status": "ready"}),
            _response({"paths": {"/api/v1/me/bootstrap/": {}}}),
            _response({"data": {"courses": []}}),
            _response({"meta": {"contract": "learner-bootstrap"}, "data": {}}),
        ]
        with self.assertRaisesRegex(SmokeFailure, "private cache boundary"):
            run_synthetic_smoke("https://example.com", "token")

    @patch("polskiflow.learning.management.commands.production_smoke.run_synthetic_smoke", return_value=())
    def test_command_reads_token_only_from_environment(self, run):
        output = io.StringIO()
        with patch.dict(os.environ, {"CUSTOM_SMOKE_TOKEN": "token-value"}):
            call_command("production_smoke", "https://example.com", token_env="CUSTOM_SMOKE_TOKEN", stdout=output)
        run.assert_called_once_with("https://example.com", "token-value", timeout=10)
        self.assertNotIn("token-value", output.getvalue())

    def test_command_requires_configured_token(self):
        with patch.dict(os.environ, {}, clear=True), self.assertRaises(CommandError):
            call_command("production_smoke", "https://example.com")
