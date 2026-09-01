"""Authenticated interaction and mediation practice."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from polskiflow.auth_views import require_browser_user
from polskiflow.domain.interaction_scenarios import SCENARIOS, validate_answer


@require_browser_user
@require_http_methods(["GET", "POST"])
def interaction_practice(request: HttpRequest) -> HttpResponse:
    result = None
    error = ""
    status = 200

    if request.method == "POST":
        allowed_fields = {"csrfmiddlewaretoken", "scenario_id", "option_id"}
        unexpected_fields = set(request.POST) - allowed_fields
        has_single_values = all(
            len(request.POST.getlist(field)) == 1
            for field in ("scenario_id", "option_id")
        )
        if unexpected_fields or not has_single_values:
            error = "Не удалось проверить ответ. Обновите страницу и попробуйте снова."
            status = 400
        else:
            scenario_id = request.POST.get("scenario_id", "")
            option_id = request.POST.get("option_id", "")
            try:
                scenario, is_correct = validate_answer(scenario_id, option_id)
            except ValueError as exc:
                error = str(exc)
                status = 400
            else:
                selected_option = next(
                    option for option in scenario.options if option.id == option_id
                )
                correct_option = next(
                    option
                    for option in scenario.options
                    if option.id == scenario.correct_option_id
                )
                result = {
                    "scenario": scenario,
                    "selected_option": selected_option,
                    "correct_option": correct_option,
                    "is_correct": is_correct,
                }

    return render(
        request,
        "interaction.html",
        {"scenarios": SCENARIOS, "result": result, "error": error},
        status=status,
    )
