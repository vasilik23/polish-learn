import uuid

from django.http import HttpResponse
from django.test import RequestFactory, SimpleTestCase

from polskiflow.request_id import RequestIdMiddleware


class RequestIdMiddlewareTests(SimpleTestCase):
    def test_response_gets_generated_uuid_request_id(self):
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(uuid.UUID(response["X-Request-ID"])), response["X-Request-ID"])

    def test_valid_client_request_id_is_preserved(self):
        request_id = "cf4fc5e8-6f30-4a96-b89c-779fca0456b3"
        response = self.client.get("/health/", headers={"X-Request-ID": request_id})
        self.assertEqual(response["X-Request-ID"], request_id)

    def test_invalid_or_oversized_value_is_replaced(self):
        for value in ("not-a-uuid", "x" * 10_000):
            with self.subTest(value=value[:20]):
                response = self.client.get("/health/", headers={"X-Request-ID": value})
                self.assertNotEqual(response["X-Request-ID"], value)
                uuid.UUID(response["X-Request-ID"])

    def test_not_found_response_also_has_request_id(self):
        response = self.client.get("/missing-page/")
        self.assertEqual(response.status_code, 404)
        uuid.UUID(response["X-Request-ID"])

    def test_server_error_is_logged_with_request_id(self):
        middleware = RequestIdMiddleware(lambda _request: HttpResponse(status=503))
        request = RequestFactory().get("/health/")
        with self.assertLogs("polskiflow.request", level="WARNING") as captured:
            response = middleware(request)
        self.assertIn(f"request_id={response['X-Request-ID']}", captured.output[0])
        self.assertIn("path=/health/", captured.output[0])
