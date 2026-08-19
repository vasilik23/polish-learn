import uuid

from django.db import models


class LessonId(models.TextChoices):
    WORDS = "words", "Новые слова"
    GRAMMAR = "grammar", "Грамматика"
    REVIEW = "review", "Повторение"
    QUIZ = "quiz", "Мини-тест"


class Level(models.TextChoices):
    A1 = "A1", "A1"
    A2 = "A2", "A2"
    B1 = "B1", "B1"
    B2 = "B2", "B2"
    C1 = "C1", "C1"
    C2 = "C2", "C2"


class Lesson(models.Model):
    id = models.SlugField(primary_key=True, max_length=32)
    title = models.CharField(max_length=120)
    plan_title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=160)
    description = models.TextField()
    minutes = models.PositiveSmallIntegerField(default=5)
    emoji = models.CharField(max_length=8, blank=True)
    theory_title = models.CharField(max_length=160, blank=True)
    theory_sections = models.JSONField(default=list, blank=True)
    position = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "lessons"
        ordering = ("position", "id")

    def __str__(self):
        return self.title


class Flashcard(models.Model):
    id = models.SlugField(primary_key=True, max_length=80)
    polish = models.CharField(max_length=160)
    translation = models.CharField(max_length=240)
    example = models.TextField(blank=True)
    position = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "flashcards"
        ordering = ("position", "id")

    def __str__(self):
        return f"{self.polish} — {self.translation}"


class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="questions")
    prompt = models.TextField()
    options = models.JSONField(default=list)
    correct = models.PositiveSmallIntegerField()
    explanation = models.TextField(blank=True)
    position = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "questions"
        ordering = ("position", "id")
        constraints = [
            models.UniqueConstraint(
                fields=("lesson", "position"), name="unique_question_position"
            )
        ]

    def __str__(self):
        return self.prompt


class Profile(models.Model):
    id = models.UUIDField(primary_key=True)
    display_name = models.TextField(blank=True, null=True)
    level = models.CharField(max_length=2, choices=Level.choices, default=Level.A1)
    streak_days = models.PositiveIntegerField(default=0)
    last_active_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "profiles"
        managed = False


class LessonCompletion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField(db_index=True)
    lesson_id = models.CharField(max_length=16, choices=LessonId.choices)
    plan_date = models.DateField()
    cards_total = models.PositiveIntegerField(default=0)
    cards_known = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField()

    class Meta:
        db_table = "lesson_completions"
        managed = False
        constraints = [
            models.UniqueConstraint(
                fields=("user_id", "lesson_id", "plan_date"),
                name="unique_daily_lesson_completion",
            ),
            models.CheckConstraint(
                condition=models.Q(cards_known__lte=models.F("cards_total")),
                name="cards_known_not_above_total",
            ),
        ]


class FlashcardReview(models.Model):
    pk = models.CompositePrimaryKey("user_id", "card_id")
    user_id = models.UUIDField()
    card_id = models.TextField()
    ease_factor = models.FloatField(default=2.5)
    interval_days = models.PositiveIntegerField(default=0)
    repetitions = models.PositiveIntegerField(default=0)
    next_review_date = models.DateField()
    last_reviewed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "flashcard_reviews"
        managed = False
        constraints = [
            models.CheckConstraint(
                condition=models.Q(ease_factor__gte=1.3),
                name="flashcard_review_minimum_ease",
            )
        ]
