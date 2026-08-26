from django.contrib import admin

from .models import (
    Course,
    Flashcard,
    Lesson,
    LessonFlashcard,
    Question,
    ReadingText,
    Topic,
)


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0
    fields = ("prompt", "options", "correct", "explanation", "position", "is_active")


class LessonFlashcardInline(admin.TabularInline):
    model = LessonFlashcard
    extra = 0
    autocomplete_fields = ("flashcard",)
    fields = ("flashcard", "position")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "position", "is_active")
    list_filter = ("level", "is_active")
    list_editable = ("position", "is_active")
    search_fields = ("id", "title", "description")


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "position", "is_active")
    list_filter = ("course", "is_active")
    list_editable = ("position", "is_active")
    search_fields = ("id", "title", "description")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "kind", "topic", "position", "is_active")
    list_filter = ("kind", "topic__course", "is_active")
    list_editable = ("position", "is_active")
    search_fields = ("id", "title", "description")
    inlines = (QuestionInline, LessonFlashcardInline)


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ("polish", "translation", "position", "is_active")
    list_editable = ("position", "is_active")
    search_fields = ("polish", "translation", "example")


@admin.register(ReadingText)
class ReadingTextAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "topic", "minutes", "position", "is_active")
    list_filter = ("level", "topic__course", "is_active")
    list_editable = ("position", "is_active")
    search_fields = ("id", "title", "description")
    fieldsets = (
        (None, {"fields": ("id", "title", "description", "topic")}),
        ("Публикация", {"fields": ("level", "minutes", "emoji", "position", "is_active")}),
        ("Текст и словарь", {"fields": ("paragraphs", "glossary")}),
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("prompt", "lesson", "position", "is_active")
    list_filter = ("lesson", "is_active")
    list_editable = ("position", "is_active")
    search_fields = ("prompt", "explanation")
