"""Small, privacy-safe probes for the hosting platform and operators."""

from django.conf import settings
from django.db import connections
from django.http import JsonResponse


def health(_request):
    """Liveness probe: the Django process can accept requests."""
    response = JsonResponse({"status": "ok"})
    response["Cache-Control"] = "no-store"
    return response


def readiness(_request):
    """Readiness probe: required production dependencies are usable."""
    database_ready = _database_ready()
    configuration_ready = _configuration_ready()
    ready = database_ready and configuration_ready
    response = JsonResponse(
        {
            "status": "ready" if ready else "unavailable",
            "checks": {
                "database": "ok" if database_ready else "unavailable",
                "configuration": "ok" if configuration_ready else "unavailable",
            },
        },
        status=200 if ready else 503,
    )
    response["Cache-Control"] = "no-store"
    return response


def _database_ready():
    try:
        with connections["default"].cursor() as cursor:
            cursor.execute("SELECT 1")
            return cursor.fetchone() == (1,)
    except Exception:  # The probe reports state; middleware records the request ID.
        return False


def _configuration_ready():
    if not settings.VERCEL:
        return True
    return bool(settings.SUPABASE_URL and settings.SUPABASE_ANON_KEY)
