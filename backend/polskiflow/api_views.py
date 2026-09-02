"""Versioned read-only API contracts for separate clients."""

from datetime import date

from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_safe

from polskiflow.auth import require_supabase_user
from polskiflow.content import public_course_catalog
from polskiflow.dictionary_store import load_personal_words
from polskiflow.learning.models import Level
from polskiflow.progress_store import load_dashboard_progress


API_VERSION = "v1"
CATALOG_CONTRACT_VERSION = "1.0.0"
LEARNER_CONTRACT_VERSION = "1.0.0"


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


@require_safe
@require_supabase_user
def learner_progress_v1(request):
    """Expose only the authenticated learner's aggregate progress."""
    user = request.supabase_user
    progress = load_dashboard_progress(
        request.supabase_access_token,
        user.id,
        user.email or "Ученик",
    )
    if not progress.available:
        return _unavailable_response("learner-progress")

    return _private_response(
        "learner-progress",
        {
            "profile": {
                "display_name": progress.display_name,
                "level": progress.level,
                "daily_goal_lessons": progress.daily_goal_lessons,
            },
            "streak_days": progress.streak_days,
            "active_days": progress.active_days,
            "completed_lesson_ids": sorted(progress.all_completed_lesson_ids),
            "periods": {
                "week": {
                    "active_days": progress.weekly_active_days,
                    "completed_lessons": progress.weekly_completed_count,
                },
                "previous_week": {
                    "active_days": progress.previous_week_active_days,
                    "completed_lessons": progress.previous_week_completed_count,
                },
                "month": {
                    "active_days": progress.monthly_active_days,
                    "completed_lessons": progress.monthly_completed_count,
                },
            },
        },
    )


@require_safe
@require_supabase_user
def learner_sm2_v1(request):
    """Expose the authenticated learner's personal SM-2 review queue."""
    words = load_personal_words(request.supabase_access_token, request.supabase_user.id)
    if words is None:
        return _unavailable_response("learner-sm2")

    today = timezone.localdate()
    reviews = [_serialize_review(word, today) for word in words]
    reviews.sort(key=lambda item: (item["next_review_date"] or "9999-12-31", item["id"]))
    return _private_response(
        "learner-sm2",
        {
            "as_of": today.isoformat(),
            "due_count": sum(review["due"] for review in reviews),
            "reviews": reviews,
        },
    )


def _serialize_review(word: dict, today: date) -> dict:
    next_review_date = word.get("next_review_date")
    try:
        due = date.fromisoformat(next_review_date) <= today
    except (TypeError, ValueError):
        due = True
        next_review_date = None
    return {
        "id": str(word.get("id") or ""),
        "word": word.get("word") or "",
        "translation": word.get("translation") or "",
        "context": word.get("context") or "",
        "source_text_id": word.get("source_text_id") or "",
        "ease_factor": word.get("ease_factor"),
        "interval_days": word.get("interval_days") or 0,
        "repetitions": word.get("repetitions") or 0,
        "next_review_date": next_review_date,
        "last_reviewed_at": word.get("last_reviewed_at"),
        "due": due,
    }


def _private_response(contract: str, data: dict) -> JsonResponse:
    response = JsonResponse(
        {
            "api_version": API_VERSION,
            "meta": {
                "contract": contract,
                "contract_version": LEARNER_CONTRACT_VERSION,
                "generated_at": timezone.now().isoformat(),
            },
            "data": data,
        },
        json_dumps_params={"ensure_ascii": False},
    )
    response["Cache-Control"] = "private, no-store"
    response["Vary"] = "Authorization, Cookie"
    return response


def _unavailable_response(contract: str) -> JsonResponse:
    response = JsonResponse(
        {
            "api_version": API_VERSION,
            "meta": {
                "contract": contract,
                "contract_version": LEARNER_CONTRACT_VERSION,
            },
            "error": {
                "code": "upstream_unavailable",
                "detail": "Learner data is temporarily unavailable",
            },
        },
        status=503,
    )
    response["Cache-Control"] = "private, no-store"
    response["Vary"] = "Authorization, Cookie"
    return response
