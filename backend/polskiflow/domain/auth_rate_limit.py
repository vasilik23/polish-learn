"""Privacy-preserving best-effort throttling for public auth forms."""

from django.conf import settings
from django.core.cache import cache
from django.utils.crypto import salted_hmac


def consume_auth_attempt(request, action: str, email: str) -> tuple[bool, int]:
    limits = settings.AUTH_FORM_RATE_LIMITS
    limit, window = limits[action]
    address = _client_address(request)
    identity = f"{action}\0{address}\0{email.strip().casefold()}"
    digest = salted_hmac("polskiflow.auth-rate-limit", identity).hexdigest()
    key = f"auth-rate:{action}:{digest}"
    if cache.add(key, 1, timeout=window):
        return True, window
    try:
        attempts = cache.incr(key)
    except ValueError:
        cache.set(key, 1, timeout=window)
        attempts = 1
    return attempts <= limit, window


def _client_address(request) -> str:
    if getattr(settings, "VERCEL", False):
        forwarded = request.META.get("HTTP_X_FORWARDED_FOR", "")
        if forwarded:
            return forwarded.split(",", 1)[0].strip()
    return request.META.get("REMOTE_ADDR", "unknown")
