from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from polskiflow.auth_views import require_browser_user
from polskiflow.catalog_search import search_learning_catalog
from polskiflow.lesson_bookmark_store import load_lesson_bookmarks


@require_browser_user
@require_GET
def global_search(request: HttpRequest) -> HttpResponse:
    raw_query = request.GET.get("q", "")
    result = search_learning_catalog(raw_query)
    bookmarks = load_lesson_bookmarks(
        request.supabase_access_token, request.supabase_user.id
    )
    for lesson in result["lessons"]:
        lesson["saved"] = lesson["id"] in (bookmarks or set())
    return render(
        request,
        "search.html",
        {
            "search_result": result,
            "search_performed": len(result["query"]) >= 2,
            "lesson_bookmarks_available": bookmarks is not None,
        },
    )
