"""Best-effort per-user throttling for authenticated API mutations."""

from django.conf import settings
from django.core.cache import cache
from django.utils.crypto import salted_hmac


def consume_api_mutation(user_id: str, action: str) -> tuple[bool, int]:
    limit, window = settings.API_MUTATION_RATE_LIMITS[action]
    digest = salted_hmac("polskiflow.api-mutation-rate", f"{action}\0{user_id}").hexdigest()
    key = f"api-mutation:{action}:{digest}"
    if cache.add(key, 1, timeout=window):
        return True, window
    try:
        attempts = cache.incr(key)
    except ValueError:
        cache.set(key, 1, timeout=window)
        attempts = 1
    return attempts <= limit, window
