from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from polskiflow.auth_views import require_browser_user
from polskiflow.content import tasks
from polskiflow.learning.models import Question
from polskiflow.mistake_store import load_mistakes


@require_browser_user
@require_GET
def mistake_notebook(request: HttpRequest) -> HttpResponse:
    rows = load_mistakes(request.supabase_access_token, request.supabase_user.id)
    lesson_map = {item["id"]: item for item in tasks()}
    questions = {
        (row.lesson_id, row.position): row.prompt
        for row in Question.objects.filter(is_active=True).only("lesson_id", "position", "prompt")
    }
    items = []
    for row in rows or []:
        lesson_id, position = row.get("lesson_id"), row.get("question_position")
        lesson = lesson_map.get(lesson_id)
        if lesson and type(position) is int and (lesson_id, position) in questions:
            items.append({
                "lesson_id": lesson_id, "title": lesson["plan_title"],
                "emoji": lesson["emoji"], "level": lesson["level"],
                "prompt": questions[(lesson_id, position)],
            })
    return render(request, "mistakes.html", {"mistakes": items, "mistakes_available": rows is not None})
