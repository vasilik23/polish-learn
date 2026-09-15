"""Authenticated, non-persistent CEFR self-assessment page."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from polskiflow.auth_views import require_browser_user
from polskiflow.domain.diagnostic import (
    CHECK_TASKS,
    LEVELS,
    MODE_OPTIONS,
    MODES,
    score_checked_tasks,
    score_diagnostic,
)
from polskiflow.progress_store import load_dashboard_progress, save_profile_settings


@require_browser_user
@require_http_methods(["GET", "POST"])
def diagnostic(request: HttpRequest) -> HttpResponse:
    selections = {
        key: request.POST.get(key, "")
        for key, _title, _description in MODES
    }
    checked_answers = {
        task["key"]: request.POST.get(task["key"], "") for task in CHECK_TASKS
    }
    context = {
        "mode_fields": tuple(
            {
                "key": key,
                "title": title,
                "description": description,
                "selected": selections[key],
                "options": MODE_OPTIONS[key],
            }
            for key, title, description in MODES
        ),
        "selections": selections,
        "result": None,
        "check_tasks": tuple(
            {**task, "selected": checked_answers[task["key"]]} for task in CHECK_TASKS
        ),
        "checked_result": None,
        "recommended_level": "",
        "error": "",
    }
    status = 200
    if request.method == "POST" and request.POST.get("action") == "apply-level":
        level = request.POST.get("recommended_level", "").upper()
        if level not in LEVELS:
            context["error"] = "Некорректный рекомендованный уровень. Пройди диагностику заново."
            status = 400
        else:
            fallback_name = (request.supabase_user.email or "ученик").split("@", 1)[0]
            dashboard = load_dashboard_progress(
                request.supabase_access_token,
                request.supabase_user.id,
                fallback_name,
            )
            if save_profile_settings(
                request.supabase_access_token,
                request.supabase_user.id,
                dashboard.display_name,
                level,
                dashboard.daily_goal_lessons,
            ):
                return redirect(f"/course/?level={level}&diagnostic=applied")
            context["error"] = "Не удалось сохранить уровень. Попробуй ещё раз."
            status = 503
    elif request.method == "POST":
        try:
            self_result = score_diagnostic(selections)
            checked_result = score_checked_tasks(checked_answers)
            context["result"] = self_result
            context["checked_result"] = checked_result
            context["recommended_level"] = min(
                (self_result.level, checked_result.level), key=LEVELS.index
            )
        except ValueError as error:
            context["error"] = str(error)
            status = 400
    return render(request, "diagnostic.html", context, status=status)
