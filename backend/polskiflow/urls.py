from django.http import JsonResponse
from django.urls import path

from polskiflow.auth import require_supabase_user
from polskiflow.auth_views import home, login_view, logout_view, register_view


def health(_request):
    return JsonResponse({"status": "ok"})


@require_supabase_user
def current_user(request):
    return JsonResponse(
        {"id": request.supabase_user.id, "email": request.supabase_user.email}
    )


urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("health/", health, name="health"),
    path("api/auth/me/", current_user, name="current-user"),
]
