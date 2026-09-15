"""Owner-scoped learning history UI."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from polskiflow.auth_views import require_browser_user
from polskiflow.content import tasks
from polskiflow.progress_store import load_completion_history


PERIODS = {"7": 7, "30": 30, "90": 90, "all": None}


@require_browser_user
@require_GET
def learning_history(request: HttpRequest) -> HttpResponse:
    period = request.GET.get("period", "30")
    if period not in PERIODS:
        period = "30"
    try:
        page_number = int(request.GET.get("page", "1"))
    except (TypeError, ValueError):
        page_number = 1
    page = load_completion_history(
        request.supabase_access_token,
        request.supabase_user.id,
        page=max(1, page_number),
        days=PERIODS[period],
    )
    lesson_map = {lesson["id"]: lesson for lesson in tasks()}
    rows = []
    for completion in page.rows:
        lesson = lesson_map.get(completion.get("lesson_id"), {})
        total = completion.get("cards_total") or 0
        known = completion.get("cards_known") or 0
        rows.append({
            **completion,
            "title": lesson.get("title") or completion.get("lesson_id") or "Урок",
            "emoji": lesson.get("emoji") or "✓",
            "level": lesson.get("level") or "—",
            "score": f"{known} / {total}" if total else "завершён",
        })
    return render(request, "history.html", {
        "history_rows": rows,
        "history_available": page.available,
        "history_page": page,
        "selected_period": period,
    })
