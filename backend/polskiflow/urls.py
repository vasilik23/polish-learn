from django.http import JsonResponse
from django.urls import path

from polskiflow.auth import require_supabase_user


def health(_request):
    return JsonResponse({"status": "ok"})


@require_supabase_user
def current_user(request):
    return JsonResponse(
        {"id": request.supabase_user.id, "email": request.supabase_user.email}
    )


urlpatterns = [
    path("health/", health, name="health"),
    path("api/auth/me/", current_user, name="current-user"),
]
