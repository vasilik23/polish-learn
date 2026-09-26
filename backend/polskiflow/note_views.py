"""Searchable web library for owner-scoped lesson notes."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from polskiflow.auth_views import require_browser_user
from polskiflow.learning.models import Lesson
from polskiflow.lesson_note_store import load_lesson_notes, save_lesson_note


@require_browser_user
@require_GET
def lesson_notes(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q", "").strip()[:80]
    rows = load_lesson_notes(request.supabase_access_token, request.supabase_user.id)
    lessons = {
        lesson.id: lesson
        for lesson in Lesson.objects.filter(
            id__in={row["lesson_id"] for row in rows or ()},
            is_active=True,
            topic__is_active=True,
            topic__course__is_active=True,
        ).select_related("topic__course")
    }
    items = []
    needle = query.casefold()
    for row in rows or ():
        lesson = lessons.get(row["lesson_id"])
        if lesson is None:
            continue
        haystack = " ".join((row["body"], lesson.plan_title, lesson.topic.title, lesson.topic.course.level)).casefold()
        if needle and needle not in haystack:
            continue
        items.append({"lesson": lesson, "body": row["body"], "updated_at": row.get("updated_at")})
    return render(request, "notes.html", {"notes": items, "notes_available": rows is not None, "query": query, "total_count": len(rows or ())})


@require_POST
@require_browser_user
def delete_lesson_note(request: HttpRequest, lesson_id: str) -> HttpResponse:
    saved = save_lesson_note(request.supabase_access_token, request.supabase_user.id, lesson_id, "")
    return redirect("/notes/?status=deleted" if saved else "/notes/?status=error")
