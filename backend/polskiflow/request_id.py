"""Privacy-safe request correlation for browser, API, and runtime logs."""

import logging
import uuid


logger = logging.getLogger("polskiflow.request")


class RequestIdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_id = _request_id(request.headers.get("X-Request-ID"))
        request.request_id = request_id
        response = self.get_response(request)
        response["X-Request-ID"] = request_id
        if response.status_code >= 500:
            logger.warning(
                "request_failed request_id=%s method=%s path=%s status=%s",
                request_id,
                request.method,
                request.path,
                response.status_code,
            )
        return response


def _request_id(candidate):
    try:
        return str(uuid.UUID(candidate))
    except (AttributeError, TypeError, ValueError):
        return str(uuid.uuid4())
