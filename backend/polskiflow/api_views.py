"""Versioned API contracts for separate clients."""

from datetime import date

import json

from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST, require_safe

from polskiflow.auth import require_supabase_user
from polskiflow.content import flashcards, grammar, public_course_catalog, quiz, reading_text, task
from polskiflow.dictionary_store import load_personal_words
from polskiflow.domain.lesson_results import (
    MAX_REQUEST_BYTES,
    LessonResultValidationError,
    validate_lesson_result,
)
from polskiflow.domain.openapi_v1 import build_openapi_v1
from polskiflow.learning.models import Lesson, Level
from polskiflow.lesson_draft_store import delete_lesson_draft, load_latest_lesson_draft_result, save_lesson_draft
from polskiflow.progress_store import load_completion_history, load_dashboard_progress, record_lesson_result_event
from polskiflow.reading_bookmark_store import load_reading_bookmarks, set_reading_bookmark


API_VERSION = "v1"
CATALOG_CONTRACT_VERSION = "1.0.0"
LEARNER_CONTRACT_VERSION = "1.0.0"


@require_safe
def openapi_v1(_request):
    response = JsonResponse(build_openapi_v1(), json_dumps_params={"ensure_ascii": False})
    response["Cache-Control"] = "public, max-age=300, s-maxage=3600"
    return response


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


@require_safe
@require_supabase_user
def learner_reading_bookmarks_v1(request):
    bookmarks = load_reading_bookmarks(request.supabase_access_token, request.supabase_user.id)
    if bookmarks is None:
        return _unavailable_response("learner-reading-bookmarks")
    return _private_response("learner-reading-bookmarks", {"reading_text_ids": sorted(bookmarks)})


@require_safe
@require_supabase_user
def learner_history_v1(request):
    """Return one bounded owner-scoped completion page for separate clients."""
    if not _valid_bearer(request):
        return _error_response("bearer_required", "A valid Bearer token is required", 401)
    period = request.GET.get("period", "30")
    periods = {"7": 7, "30": 30, "90": 90, "all": None}
    try:
        page = int(request.GET.get("page", "1"))
    except (TypeError, ValueError):
        page = 0
    if period not in periods or not 1 <= page <= 500:
        return _error_response("invalid_pagination", "Use page 1..500 and period 7, 30, 90, or all", 400)
    history = load_completion_history(
        request.supabase_access_token,
        request.supabase_user.id,
        page=page,
        page_size=50,
        days=periods[period],
    )
    if not history.available:
        return _unavailable_response("learner-history")
    return _private_response("learner-history", {
        "period": period,
        "page": history.page,
        "page_size": 50,
        "has_previous": history.has_previous,
        "has_next": history.has_next,
        "completions": list(history.rows),
    })


@require_safe
@require_supabase_user
def learner_latest_lesson_draft_v1(request):
    if not _valid_bearer(request):
        return _error_response("bearer_required", "A valid Bearer token is required", 401)
    result = load_latest_lesson_draft_result(
        request.supabase_access_token, request.supabase_user.id
    )
    if not result.available:
        return _unavailable_response("learner-lesson-draft")
    return _private_response("learner-lesson-draft", {"draft": result.draft})


@csrf_exempt
@require_http_methods(["PUT", "DELETE"])
@require_supabase_user
def learner_lesson_draft_v1(request, lesson_id):
    if not _valid_bearer(request):
        return _error_response("bearer_required", "A valid Bearer token is required", 401)
    lesson = task(lesson_id)
    if lesson is None:
        return _error_response("lesson_not_found", "Active lesson was not found", 404)
    token, owner = request.supabase_access_token, request.supabase_user.id
    if request.method == "DELETE":
        if not delete_lesson_draft(token, owner, lesson_id):
            return _unavailable_response("learner-lesson-draft")
        return _private_response("learner-lesson-draft", {"draft": None})
    if request.content_type != "application/json":
        return _error_response("unsupported_media_type", "Content-Type must be application/json", 415)
    if len(request.body) > 1024:
        return _error_response("payload_too_large", "Request body is too large", 413)
    try:
        payload = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return _error_response("invalid_json", "Request body must be valid JSON", 400)
    if not isinstance(payload, dict) or set(payload) != {"step_index", "score"}:
        return _error_response("validation_error", "Use exactly step_index and score", 400)
    step_index, score = payload["step_index"], payload["score"]
    if isinstance(step_index, bool) or isinstance(score, bool) or not isinstance(step_index, int) or not isinstance(score, int):
        return _error_response("validation_error", "step_index and score must be integers", 400)
    total = _lesson_step_count(lesson_id, lesson["kind"])
    if total < 2 or not (0 < step_index < total) or not (0 <= score <= step_index):
        return _error_response("validation_error", "Draft must describe a valid unfinished step and score", 400)
    if not save_lesson_draft(token, owner, lesson_id, lesson["kind"], step_index, score):
        return _unavailable_response("learner-lesson-draft")
    return _private_response("learner-lesson-draft", {"draft": {
        "lesson_id": lesson_id, "lesson_kind": lesson["kind"],
        "step_index": step_index, "score": score,
    }})


def _lesson_step_count(lesson_id, lesson_kind):
    if lesson_kind in {"words", "review"}:
        return len(flashcards(lesson_id))
    if lesson_kind == "grammar":
        content = grammar(lesson_id)
        return len(content["questions"]) if content else 0
    return len(quiz(lesson_id))


@csrf_exempt
@require_http_methods(["PUT", "DELETE"])
@require_supabase_user
def learner_reading_bookmark_v1(request, text_id):
    if not _valid_bearer(request):
        return _error_response("bearer_required", "A valid Bearer token is required", 401)
    if reading_text(text_id) is None:
        return _error_response("reading_text_not_found", "Active reading text was not found", 404)
    saved = request.method == "PUT"
    if not set_reading_bookmark(request.supabase_access_token, request.supabase_user.id, text_id, saved):
        return _unavailable_response("learner-reading-bookmark")
    return _private_response("learner-reading-bookmark", {"reading_text_id": text_id, "saved": saved})


@csrf_exempt
@require_POST
@require_supabase_user
def lesson_results_v1(request):
    if not _valid_bearer(request):
        return _error_response("bearer_required", "A valid Bearer token is required", 401)
    return _store_lesson_result(request)


def _valid_bearer(request):
    scheme, separator, token = request.headers.get("Authorization", "").partition(" ")
    return scheme.lower() == "bearer" and separator == " " and bool(token) and token == request.supabase_access_token


@require_POST
@require_supabase_user
def lesson_results_session_v1(request):
    """Store a browser-queued result without exposing its HttpOnly token."""
    if request.headers.get("Authorization"):
        return _error_response(
            "cookie_session_required",
            "Use the browser session without an Authorization header",
            401,
        )
    return _store_lesson_result(request)


def _store_lesson_result(request):
    if request.content_type != "application/json":
        return _error_response("unsupported_media_type", "Content-Type must be application/json", 415)
    if len(request.body) > MAX_REQUEST_BYTES:
        return _error_response("payload_too_large", "Request body is too large", 413)
    try:
        payload = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return _error_response("invalid_json", "Request body must be valid JSON", 400)
    try:
        result = validate_lesson_result(payload)
    except LessonResultValidationError as error:
        return _error_response("validation_error", str(error), 400)
    if not Lesson.objects.filter(id=result.lesson_id, is_active=True).exists():
        return _error_response("lesson_not_found", "Active lesson was not found", 404)
    stored = record_lesson_result_event(request.supabase_access_token, result)
    if stored is None:
        return _error_response("upstream_unavailable", "Result could not be stored", 503)
    status = stored.get("status")
    if status == "conflict":
        return _error_response("idempotency_conflict", "event_id already has different data", 409)
    if status not in {"created", "duplicate"}:
        return _error_response("upstream_unavailable", "Unexpected storage response", 503)
    response = JsonResponse(
        {
            "api_version": API_VERSION,
            "meta": {"contract": "lesson-result", "contract_version": "1.0"},
            "data": {"event_id": result.event_id, "status": status},
        },
        status=201 if status == "created" else 200,
    )
    response["Cache-Control"] = "private, no-store"
    response["Vary"] = "Authorization, Cookie"
    return response


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


def _error_response(code: str, detail: str, status: int) -> JsonResponse:
    response = JsonResponse(
        {"api_version": API_VERSION, "error": {"code": code, "detail": detail}},
        status=status,
    )
    response["Cache-Control"] = "private, no-store"
    response["Vary"] = "Authorization, Cookie"
    return response
