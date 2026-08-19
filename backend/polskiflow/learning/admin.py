from django.contrib import admin

from .models import Flashcard, Lesson, Question


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0
    fields = ("prompt", "options", "correct", "explanation", "position", "is_active")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "position", "is_active")
    list_editable = ("position", "is_active")
    search_fields = ("id", "title", "description")
    inlines = (QuestionInline,)


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ("polish", "translation", "position", "is_active")
    list_editable = ("position", "is_active")
    search_fields = ("polish", "translation", "example")


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("prompt", "lesson", "position", "is_active")
    list_filter = ("lesson", "is_active")
    list_editable = ("position", "is_active")
    search_fields = ("prompt", "explanation")
