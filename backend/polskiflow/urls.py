from django.http import JsonResponse
from django.urls import path
from django.contrib import admin

from polskiflow.auth import require_supabase_user
from polskiflow.auth_views import course, daily_tasks, forgot_password, home, listening_practice, login_view, logout_view, profile, register_view, resend_confirmation, reset_password, sources, writing_practice
from polskiflow.diagnostic_views import diagnostic
from polskiflow.lesson_views import lesson, lesson_step
from polskiflow.interaction_views import interaction_practice
from polskiflow.reading_views import (
    add_dictionary_word,
    dictionary,
    dictionary_practice,
    dictionary_practice_step,
    news_library,
    reader,
    reading_library,
    remove_dictionary_word,
)


def health(_request):
    return JsonResponse({"status": "ok"})


@require_supabase_user
def current_user(request):
    return JsonResponse(
        {"id": request.supabase_user.id, "email": request.supabase_user.email}
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("tasks/", daily_tasks, name="daily-tasks"),
    path("course/", course, name="course"),
    path("diagnostic/", diagnostic, name="diagnostic"),
    path("profile/", profile, name="profile"),
    path("writing/", writing_practice, name="writing-practice"),
    path("interaction/", interaction_practice, name="interaction-practice"),
    path("listening/", listening_practice, name="listening-practice"),
    path("sources/", sources, name="sources"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("forgot-password/", forgot_password, name="forgot-password"),
    path("reset-password/", reset_password, name="reset-password"),
    path("resend-confirmation/", resend_confirmation, name="resend-confirmation"),
    path("logout/", logout_view, name="logout"),
    path("lesson/<slug:lesson_id>/", lesson, name="lesson"),
    path("lesson/<slug:lesson_id>/step/", lesson_step, name="lesson-step"),
    path("reading/", reading_library, name="reading-library"),
    path("news/", news_library, name="news-library"),
    path("reading/<slug:text_id>/", reader, name="reader"),
    path("reading/<slug:text_id>/save/", add_dictionary_word, name="add-dictionary-word"),
    path("dictionary/", dictionary, name="dictionary"),
    path("dictionary/practice/", dictionary_practice, name="dictionary-practice"),
    path("dictionary/practice/step/", dictionary_practice_step, name="dictionary-practice-step"),
    path("dictionary/<uuid:word_id>/delete/", remove_dictionary_word, name="remove-dictionary-word"),
    path("health/", health, name="health"),
    path("api/auth/me/", current_user, name="current-user"),
]
