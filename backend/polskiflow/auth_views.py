"""Browser views for the transitional Django authentication flow."""

from functools import wraps
from urllib.parse import urlencode

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_http_methods, require_POST

from polskiflow.auth import (
    SupabaseAuthError,
    clear_auth_cookies,
    set_auth_cookies,
    sign_in,
    sign_out,
    sign_up,
)
from polskiflow.content import course_topics, tasks
from polskiflow.dictionary_store import load_personal_words
from polskiflow.domain.daily_plan import build_daily_plan
from polskiflow.domain.password_policy import password_error
from polskiflow.progress_store import load_dashboard_progress


def require_browser_user(view):
    @wraps(view)
    def protected(request: HttpRequest, *args, **kwargs):
        if request.supabase_user is None:
            login_url = reverse("login")
            query = urlencode({"next": request.get_full_path()})
            return redirect(f"{login_url}?{query}")
        return view(request, *args, **kwargs)

    return protected


@require_http_methods(["GET", "POST"])
def login_view(request: HttpRequest) -> HttpResponse:
    if request.supabase_user is not None:
        return redirect("home")

    next_url = _safe_next(request)
    context = {"mode": "login", "next": next_url}
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        if not email or not password:
            context["error"] = "Укажите email и пароль"
        else:
            try:
                session = sign_in(email, password)
            except SupabaseAuthError as error:
                context["error"] = str(error)
            else:
                response = redirect(next_url)
                set_auth_cookies(response, session)
                return response
    return render(request, "auth/form.html", context)


@require_http_methods(["GET", "POST"])
def register_view(request: HttpRequest) -> HttpResponse:
    if request.supabase_user is not None:
        return redirect("home")

    context = {"mode": "register", "next": "/"}
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        context["email"] = email
        if not email or not password:
            context["error"] = "Укажите email и пароль"
        elif error := password_error(password):
            context["error"] = error
        else:
            try:
                session = sign_up(email, password)
            except SupabaseAuthError as error:
                context["error"] = str(error)
            else:
                if session is None:
                    context["message"] = (
                        "Аккаунт создан. Подтвердите email, затем войдите."
                    )
                else:
                    response = redirect("home")
                    set_auth_cookies(response, session)
                    return response
    return render(request, "auth/form.html", context)


@require_POST
def logout_view(request: HttpRequest) -> HttpResponse:
    if request.supabase_access_token:
        try:
            sign_out(request.supabase_access_token)
        except SupabaseAuthError:
            pass
    response = redirect("login")
    clear_auth_cookies(response)
    return response


@require_browser_user
def home(request: HttpRequest) -> HttpResponse:
    dashboard, lesson_tasks, completed_count, progress_percent = _daily_plan(request)
    return render(
        request,
        "home.html",
        {
            "user": request.supabase_user,
            "dashboard": dashboard,
            "tasks": lesson_tasks,
            "completed_count": completed_count,
            "progress_percent": progress_percent,
        },
    )


@require_browser_user
def daily_tasks(request: HttpRequest) -> HttpResponse:
    dashboard, lesson_tasks, completed_count, progress_percent = _daily_plan(request)
    return render(
        request,
        "daily_tasks.html",
        {
            "dashboard": dashboard,
            "tasks": lesson_tasks,
            "completed_count": completed_count,
            "progress_percent": progress_percent,
        },
    )


@require_browser_user
def profile(request: HttpRequest) -> HttpResponse:
    fallback_name = (request.supabase_user.email or "ученик").split("@", 1)[0]
    dashboard = load_dashboard_progress(
        request.supabase_access_token,
        request.supabase_user.id,
        fallback_name,
    )
    lesson_ids = {lesson_task["id"] for lesson_task in tasks()}
    completed_lessons = len(dashboard.all_completed_lesson_ids & lesson_ids)
    total_lessons = len(lesson_ids)
    progress_percent = (
        round(completed_lessons / total_lessons * 100) if total_lessons else 0
    )
    personal_words = load_personal_words(
        request.supabase_access_token,
        request.supabase_user.id,
    )
    return render(
        request,
        "profile.html",
        {
            "dashboard": dashboard,
            "email": request.supabase_user.email or "Email не указан",
            "completed_lessons": completed_lessons,
            "total_lessons": total_lessons,
            "progress_percent": progress_percent,
            "dictionary_count": len(personal_words or []),
            "dictionary_available": personal_words is not None,
        },
    )


def sources(request: HttpRequest) -> HttpResponse:
    """Show the public attribution and content-source policy summary."""
    return render(request, "sources.html")


def _daily_plan(request: HttpRequest):
    fallback_name = (request.supabase_user.email or "ученик").split("@", 1)[0]
    dashboard = load_dashboard_progress(
        request.supabase_access_token,
        request.supabase_user.id,
        fallback_name,
    )
    personal_words = load_personal_words(
        request.supabase_access_token, request.supabase_user.id
    )
    lesson_tasks = build_daily_plan(
        tasks(),
        level=dashboard.level,
        completed_all_time=dashboard.all_completed_lesson_ids,
        completed_today=dashboard.completed_lesson_ids,
        personal_words=personal_words,
        today=timezone.localdate(),
    )
    completed_count = sum(task["completed"] for task in lesson_tasks)
    progress_percent = (
        round(completed_count / len(lesson_tasks) * 100) if lesson_tasks else 0
    )
    return dashboard, lesson_tasks, completed_count, progress_percent


@require_browser_user
def course(request: HttpRequest) -> HttpResponse:
    fallback_name = (request.supabase_user.email or "ученик").split("@", 1)[0]
    dashboard = load_dashboard_progress(
        request.supabase_access_token,
        request.supabase_user.id,
        fallback_name,
    )
    levels = ("A1", "A2", "B1", "B2", "C1")
    requested_level = request.GET.get("level", "A1").upper()
    selected_level = requested_level if requested_level in levels else "A1"
    all_topics = course_topics()
    level_counts = {
        level: sum(topic["level"] == level for topic in all_topics) for level in levels
    }

    def topic_count_label(count: int) -> str:
        if count == 0:
            return "Скоро"
        if count % 10 == 1 and count % 100 != 11:
            suffix = "тема"
        elif count % 10 in (2, 3, 4) and count % 100 not in (12, 13, 14):
            suffix = "темы"
        else:
            suffix = "тем"
        return f"{count} {suffix}"
    topics = [topic for topic in all_topics if topic["level"] == selected_level]
    for topic in topics:
        completed_count = 0
        next_lesson = None
        for lesson in topic["lessons"]:
            lesson["completed"] = lesson["id"] in dashboard.all_completed_lesson_ids
            if lesson["completed"]:
                completed_count += 1
            elif next_lesson is None:
                next_lesson = lesson
        lesson_count = len(topic["lessons"])
        topic["completed_count"] = completed_count
        topic["lesson_count"] = lesson_count
        topic["progress_percent"] = round(completed_count / lesson_count * 100)
        topic["next_lesson"] = next_lesson
        topic["completed"] = completed_count == lesson_count
    return render(
        request,
        "course.html",
        {
            "dashboard": dashboard,
            "course_topics": topics,
            "course_levels": [
                {
                    "name": level,
                    "topic_count": level_counts[level],
                    "topic_count_label": topic_count_label(level_counts[level]),
                }
                for level in levels
            ],
            "selected_level": selected_level,
        },
    )


def _safe_next(request: HttpRequest) -> str:
    candidate = request.POST.get("next") or request.GET.get("next") or "/"
    if url_has_allowed_host_and_scheme(
        candidate,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return candidate
    return "/"
