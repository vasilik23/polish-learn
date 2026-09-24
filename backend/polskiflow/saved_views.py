"""Saved-learning web surface."""

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_GET, require_POST

from polskiflow.auth_views import require_browser_user
from polskiflow.learning.models import Lesson, ReadingText
from polskiflow.lesson_bookmark_store import load_lesson_bookmarks, set_lesson_bookmark
from polskiflow.reading_bookmark_store import load_reading_bookmarks


@require_browser_user
@require_GET
def saved_learning(request: HttpRequest) -> HttpResponse:
    lesson_ids = load_lesson_bookmarks(request.supabase_access_token, request.supabase_user.id)
    reading_ids = load_reading_bookmarks(request.supabase_access_token, request.supabase_user.id)
    available = lesson_ids is not None and reading_ids is not None
    lessons = list(
        Lesson.objects.filter(
            id__in=lesson_ids or (), is_active=True, topic__is_active=True, topic__course__is_active=True
        )
        .select_related("topic__course")
        .order_by("topic__course__position", "topic__position", "position", "id")
    )
    readings = list(
        ReadingText.objects.filter(id__in=reading_ids or (), is_active=True)
        .order_by("level", "position", "id")
    )
    return render(request, "saved.html", {"saved_lessons": lessons, "saved_readings": readings, "saved_available": available})


@require_POST
@require_browser_user
def toggle_lesson_bookmark(request: HttpRequest, lesson_id: str) -> HttpResponse:
    if not Lesson.objects.filter(id=lesson_id, is_active=True, topic__is_active=True, topic__course__is_active=True).exists():
        raise Http404
    saved = request.POST.get("saved") == "1"
    set_lesson_bookmark(request.supabase_access_token, request.supabase_user.id, lesson_id, saved)
    candidate = request.POST.get("next", "")
    if not url_has_allowed_host_and_scheme(candidate, {request.get_host()}, require_https=request.is_secure()):
        candidate = "/saved/" if not saved else f"/lesson/{lesson_id}/"
    return redirect(candidate)
