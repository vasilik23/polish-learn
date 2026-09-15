"""Authenticated account-security settings."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from polskiflow.auth import SupabaseAuthError, clear_auth_cookies, update_password
from polskiflow.auth_views import require_browser_user
from polskiflow.domain.password_policy import password_error


@require_browser_user
@require_http_methods(["GET", "POST"])
def account_security(request: HttpRequest) -> HttpResponse:
    context = {"error": ""}
    if request.method == "POST":
        current = request.POST.get("current_password", "")
        password = request.POST.get("password", "")
        confirmation = request.POST.get("password_confirmation", "")
        if not current:
            context["error"] = "Укажите текущий пароль"
        elif password != confirmation:
            context["error"] = "Новые пароли не совпадают"
        elif current == password:
            context["error"] = "Новый пароль должен отличаться от текущего"
        elif error := password_error(password):
            context["error"] = error
        else:
            try:
                update_password(
                    request.supabase_access_token,
                    password,
                    current_password=current,
                )
            except SupabaseAuthError:
                context["error"] = (
                    "Не удалось изменить пароль. Проверьте текущий пароль или войдите заново."
                )
            else:
                response = redirect(f"{reverse('login')}?password_changed=1")
                clear_auth_cookies(response)
                response["Cache-Control"] = "private, no-store"
                return response
    response = render(request, "account/security.html", context)
    response["Cache-Control"] = "private, no-store"
    return response
