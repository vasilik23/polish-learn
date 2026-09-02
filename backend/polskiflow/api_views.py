"""Versioned, public, read-only API contracts for separate clients."""

from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_safe

from polskiflow.content import public_course_catalog
from polskiflow.learning.models import Level


API_VERSION = "v1"
CATALOG_CONTRACT_VERSION = "1.0.0"


@require_safe
def catalog_v1(_request):
    """Expose active learning structure, never learner-owned state or answers."""
    courses = public_course_catalog()
    response = JsonResponse(
        {
            "api_version": API_VERSION,
            "meta": {
                "contract": "public-course-catalog",
                "contract_version": CATALOG_CONTRACT_VERSION,
                "generated_at": timezone.now().isoformat(),
                "levels": list(Level.values),
                "course_count": len(courses),
            },
            "data": {"courses": courses},
        },
        json_dumps_params={"ensure_ascii": False},
    )
    response["Cache-Control"] = "public, max-age=60, s-maxage=300, stale-while-revalidate=600"
    return response
