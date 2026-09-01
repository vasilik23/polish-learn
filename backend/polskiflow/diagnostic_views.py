"""Authenticated, non-persistent CEFR self-assessment page."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from polskiflow.auth_views import require_browser_user
from polskiflow.domain.diagnostic import MODE_OPTIONS, MODES, score_diagnostic


@require_browser_user
@require_http_methods(["GET", "POST"])
def diagnostic(request: HttpRequest) -> HttpResponse:
    selections = {
        key: request.POST.get(key, "")
        for key, _title, _description in MODES
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
        "error": "",
    }
    status = 200
    if request.method == "POST":
        try:
            context["result"] = score_diagnostic(selections)
        except ValueError as error:
            context["error"] = str(error)
            status = 400
    return render(request, "diagnostic.html", context, status=status)
