"""Browser views for the transitional Django authentication flow."""

from dataclasses import replace
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
    request_password_reset,
    resend_signup_confirmation,
    update_password,
)
from polskiflow.content import course_topics, tasks
from polskiflow.dictionary_store import load_personal_words
from polskiflow.domain.achievements import build_achievements
from polskiflow.domain.daily_plan import build_daily_plan
from polskiflow.domain.daily_goal_insights import build_daily_goal_insight
from polskiflow.domain.password_policy import password_error
from polskiflow.domain.course_catalog import (
    COMPLETION_FILTERS,
    DURATION_FILTERS,
    LESSON_KINDS,
    filter_course_topics,
)
from polskiflow.progress_store import load_dashboard_progress, save_profile_settings


PROFILE_LEVELS = ("A1", "A2", "B1", "B2", "C1", "C2")
WRITING_PROMPTS = {
    "B1": (
    {
        "id": "formal-request",
        "title": "Официальная просьба",
        "task": "Напиши 80–100 слов администратору курса: объясни, почему пропустишь занятие, попроси материалы и предложи новый срок сдачи задания.",
        "hint": "Начни с «Szanowna Pani / Szanowny Panie», раздели причины и просьбы на абзацы.",
        "min_words": 80, "min_paragraphs": 2, "markers": ("proszę", "termin"),
    },
    {
        "id": "recommendation",
        "title": "Рекомендация места",
        "task": "Посоветуй другу польский город или место для выходных в 90–120 словах. Приведи минимум два аргумента и одно практическое предостережение.",
        "hint": "Используй связки «po pierwsze», «poza tym», «jednak» и заверши ясной рекомендацией.",
        "min_words": 90, "min_paragraphs": 2, "markers": ("po pierwsze", "polecam"),
    },
    {
        "id": "opinion",
        "title": "Личное мнение",
        "task": "Ответь в 100–120 словах: лучше учиться самостоятельно или на курсах? Обозначь позицию, аргумент, контраргумент и вывод.",
        "hint": "Полезные рамки: «moim zdaniem», «z jednej strony», «z drugiej strony», «dlatego uważam, że…».",
        "min_words": 100, "min_paragraphs": 2, "markers": ("moim zdaniem", "z drugiej strony"),
    },
    {
        "id": "story",
        "title": "Короткая история",
        "task": "Опиши в 100–130 словах ситуацию, когда планы неожиданно изменились. Покажи последовательность событий, реакцию и итог.",
        "hint": "Свяжи события словами «najpierw», «nagle», «wtedy», «w końcu» и проверь формы прошедшего времени.",
        "min_words": 100, "min_paragraphs": 2, "markers": ("najpierw", "w końcu"),
    },
    ),
    "B2": (
        {
            "id": "source-comparison",
            "title": "Сравнение двух сообщений",
            "task": "Напиши 180–220 слов: сопоставь два сообщения об одном событии, отдели подтверждённые факты от оценок и сформулируй осторожный вывод.",
            "hint": "Укажи источники и степень уверенности: «według», «źródło podaje», «prawdopodobnie», «nie można wykluczyć». ",
            "min_words": 180, "min_paragraphs": 3, "markers": ("według", "prawdopodobnie"),
        },
        {
            "id": "reasoned-recommendation",
            "title": "Обоснованная рекомендация",
            "task": "Подготовь 180–220 слов для городской консультации: представь решение, два аргумента, существенное ограничение и ответ на возможное возражение.",
            "hint": "Организуй позицию связками «wprawdzie», «jednak», «co więcej», «biorąc to pod uwagę». ",
            "min_words": 180, "min_paragraphs": 3, "markers": ("wprawdzie", "biorąc to pod uwagę"),
        },
        {
            "id": "formal-summary",
            "title": "Итог деловой встречи",
            "task": "Напиши 160–200 слов участникам встречи: нейтрально подведи итог обсуждения, зафиксируй решение, ответственных и следующие сроки.",
            "hint": "Соблюдай официальный регистр и отделяй принятые решения от предложений, которые ещё обсуждаются.",
            "min_words": 160, "min_paragraphs": 3, "markers": ("ustalono", "termin"),
        },
        {
            "id": "critical-review",
            "title": "Критическая рецензия",
            "task": "Напиши 200–240 слов о книге или фильме: кратко представь произведение, интерпретируй один приём, оцени его эффект и обоснуй рекомендацию.",
            "hint": "Не пересказывай весь сюжет; связывай наблюдение и интерпретацию через «dzięki temu», «można odczytać jako», «sugeruje». ",
            "min_words": 200, "min_paragraphs": 3, "markers": ("dzięki temu", "polecam"),
        },
    ),
}

LISTENING_ITEMS = (
    {"id": "tecza", "audio": "polskiflow/audio/tecza.ogg", "options": ("tęcza", "część", "ciężar"), "answer": "tęcza", "hint": "Слышны носовое ę и сочетание cz: tę-cza."},
    {"id": "wrobel", "audio": "polskiflow/audio/wrobel.ogg", "options": ("wróbel", "wybór", "wrona"), "answer": "wróbel", "hint": "Начальное wr- и ó /u/ помогают узнать слово wróbel."},
    {"id": "mysz", "audio": "polskiflow/audio/mysz.ogg", "options": ("my", "mysz", "miś"), "answer": "mysz", "hint": "Финальный шипящий sz отличает mysz от my и miś."},
)


def select_cefr_level(request: HttpRequest, profile_level: str) -> str:
    """Prefer an explicit valid filter, otherwise use the learner's level."""

    fallback_level = (
        profile_level.upper()
        if isinstance(profile_level, str) and profile_level.upper() in PROFILE_LEVELS
        else "A1"
    )
    requested_level = request.GET.get("level")
    if requested_level is None:
        return fallback_level
    requested_level = requested_level.upper()
    return requested_level if requested_level in PROFILE_LEVELS else fallback_level


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


@require_http_methods(["GET", "POST"])
def forgot_password(request: HttpRequest) -> HttpResponse:
    context = {"mode": "forgot"}
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        context["email"] = email
        if not email:
            context["error"] = "Укажите email"
        else:
            try:
                request_password_reset(email, request.build_absolute_uri(reverse("reset-password")))
            except SupabaseAuthError:
                pass
            context["message"] = "Если аккаунт существует, ссылка для сброса уже отправлена."
    return _no_store(render(request, "auth/recovery.html", context))


@require_http_methods(["GET", "POST"])
def reset_password(request: HttpRequest) -> HttpResponse:
    context = {"mode": "reset"}
    if request.method == "POST":
        token = request.POST.get("recovery_token", "")
        context["recovery_token"] = token
        password = request.POST.get("password", "")
        confirmation = request.POST.get("password_confirmation", "")
        if not token:
            context["error"] = "Ссылка восстановления недействительна или устарела"
        elif password != confirmation:
            context["error"] = "Пароли не совпадают"
        elif error := password_error(password):
            context["error"] = error
        else:
            try:
                update_password(token, password)
            except SupabaseAuthError as error:
                context["error"] = str(error)
            else:
                response = redirect(f"{reverse('login')}?password_reset=1")
                clear_auth_cookies(response)
                response["Cache-Control"] = "private, no-store"
                return response
    return _no_store(render(request, "auth/recovery.html", context))


@require_http_methods(["GET", "POST"])
def resend_confirmation(request: HttpRequest) -> HttpResponse:
    context = {"mode": "resend"}
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        context["email"] = email
        if not email:
            context["error"] = "Укажите email"
        else:
            try:
                resend_signup_confirmation(email, request.build_absolute_uri(reverse("login")))
            except SupabaseAuthError:
                pass
            context["message"] = "Если подтверждение ожидается, новое письмо уже отправлено."
    return _no_store(render(request, "auth/recovery.html", context))


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
    query = request.GET.urlencode()
    target = reverse("home")
    if query:
        target = f"{target}?{query}"
    return redirect(f"{target}#daily-tasks")


@require_browser_user
@require_http_methods(["GET", "POST"])
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
    dictionary_count = len(personal_words or [])
    achievements = build_achievements(
        completed_lessons=completed_lessons,
        streak_days=dashboard.streak_days,
        dictionary_count=dictionary_count,
        active_days=dashboard.active_days,
    )
    profile_form = {
        "display_name": dashboard.display_name,
        "level": dashboard.level,
        "daily_goal_lessons": dashboard.daily_goal_lessons,
    }
    profile_message = ""
    profile_error = ""
    if request.method == "POST":
        profile_form = {
            "display_name": request.POST.get("display_name", "").strip(),
            "level": request.POST.get("level", "").upper(),
            "daily_goal_lessons": request.POST.get("daily_goal_lessons", str(dashboard.daily_goal_lessons)),
        }
        if not profile_form["display_name"]:
            profile_error = "Укажите имя"
        elif len(profile_form["display_name"]) > 80:
            profile_error = "Имя должно быть не длиннее 80 символов"
        elif profile_form["level"] not in PROFILE_LEVELS:
            profile_error = "Выберите уровень от A1 до C2"
        elif not profile_form["daily_goal_lessons"].isdigit() or not 1 <= int(profile_form["daily_goal_lessons"]) <= 10:
            profile_error = "Цель должна быть от 1 до 10 уроков в день"
        elif save_profile_settings(
            request.supabase_access_token,
            request.supabase_user.id,
            profile_form["display_name"],
            profile_form["level"],
            int(profile_form["daily_goal_lessons"]),
        ):
            dashboard = replace(
                dashboard,
                display_name=profile_form["display_name"],
                level=profile_form["level"],
                daily_goal_lessons=int(profile_form["daily_goal_lessons"]),
            )
            profile_message = "Профиль сохранён"
        else:
            profile_error = "Не удалось сохранить профиль. Попробуйте ещё раз."
    daily_goal_insight = build_daily_goal_insight(
        dashboard.recent_daily_completion_counts,
        dashboard.daily_goal_lessons,
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
            "dictionary_count": dictionary_count,
            "dictionary_available": personal_words is not None,
            "achievements": achievements,
            "unlocked_achievements": sum(item.unlocked for item in achievements),
            "profile_levels": PROFILE_LEVELS,
            "profile_form": profile_form,
            "profile_message": profile_message,
            "profile_error": profile_error,
            "daily_goal_insight": daily_goal_insight,
        },
    )


def sources(request: HttpRequest) -> HttpResponse:
    """Show the public attribution and content-source policy summary."""
    return render(request, "sources.html")


@require_browser_user
def writing_practice(request: HttpRequest) -> HttpResponse:
    """Offer honest, browser-local B1/B2 writing practice without auto-grading."""
    selected_level = request.GET.get("level", "B1").upper()
    if selected_level not in WRITING_PROMPTS:
        selected_level = "B1"
    return render(
        request,
        "writing.html",
        {
            "writing_prompts": WRITING_PROMPTS[selected_level],
            "writing_levels": tuple(WRITING_PROMPTS),
            "selected_writing_level": selected_level,
        },
    )


@require_browser_user
@require_http_methods(["GET", "POST"])
def listening_practice(request: HttpRequest) -> HttpResponse:
    """Small public-domain listening pilot; results stay in this response only."""
    submitted = request.method == "POST"
    answers = {item["id"]: request.POST.get(item["id"], "") for item in LISTENING_ITEMS}
    display_items = tuple(
        {
            **item,
            "selected": answers[item["id"]],
            "is_correct": submitted and answers[item["id"]] == item["answer"],
        }
        for item in LISTENING_ITEMS
    )
    score = sum(item["is_correct"] for item in display_items) if submitted else None
    return render(request, "listening.html", {"listening_items": display_items, "score": score, "submitted": submitted})


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
        daily_task_limit=dashboard.daily_goal_lessons,
    )
    completed_count = sum(task["completed"] for task in lesson_tasks)
    progress_percent = (
        round(completed_count / len(lesson_tasks) * 100) if lesson_tasks else 0
    )
    return dashboard, lesson_tasks, completed_count, progress_percent


def _no_store(response: HttpResponse) -> HttpResponse:
    response["Cache-Control"] = "private, no-store"
    return response


@require_browser_user
def course(request: HttpRequest) -> HttpResponse:
    fallback_name = (request.supabase_user.email or "ученик").split("@", 1)[0]
    dashboard = load_dashboard_progress(
        request.supabase_access_token,
        request.supabase_user.id,
        fallback_name,
    )
    levels = PROFILE_LEVELS
    selected_level = select_cefr_level(request, dashboard.level)
    all_topics = course_topics()
    level_counts = {
        level: sum(topic["level"] == level for topic in all_topics) for level in levels
    }

    def count_label(count: int, forms: tuple[str, str, str]) -> str:
        if count % 10 == 1 and count % 100 != 11:
            suffix = forms[0]
        elif count % 10 in (2, 3, 4) and count % 100 not in (12, 13, 14):
            suffix = forms[1]
        else:
            suffix = forms[2]
        return f"{count} {suffix}"
    level_topics = [topic for topic in all_topics if topic["level"] == selected_level]
    for topic in level_topics:
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
    filters = {
        "q": request.GET.get("q", "").strip()[:120],
        "topic": request.GET.get("topic", ""),
        "kind": request.GET.get("kind", ""),
        "duration": request.GET.get("duration", ""),
        "completion": request.GET.get("completion", ""),
    }
    valid_topic_ids = {topic["id"] for topic in level_topics}
    if filters["topic"] not in valid_topic_ids:
        filters["topic"] = ""
    if filters["kind"] not in LESSON_KINDS:
        filters["kind"] = ""
    if filters["duration"] not in DURATION_FILTERS:
        filters["duration"] = ""
    if filters["completion"] not in COMPLETION_FILTERS:
        filters["completion"] = ""
    topics = filter_course_topics(
        level_topics,
        query=filters["q"],
        topic_id=filters["topic"],
        kind=filters["kind"],
        duration=filters["duration"],
        completion=filters["completion"],
    )
    result_lesson_count = sum(len(topic["lessons"]) for topic in topics)
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
                    "topic_count_label": (
                        count_label(level_counts[level], ("тема", "темы", "тем"))
                        if level_counts[level]
                        else "Скоро"
                    ),
                }
                for level in levels
            ],
            "selected_level": selected_level,
            "catalog_filters": filters,
            "catalog_topic_options": level_topics,
            "catalog_kind_options": LESSON_KINDS.items(),
            "catalog_result_topic_label": count_label(
                len(topics), ("тема", "темы", "тем")
            ),
            "catalog_result_lesson_label": count_label(
                result_lesson_count, ("урок", "урока", "уроков")
            ),
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
