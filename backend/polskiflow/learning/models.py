import uuid

from django.db import models


class Level(models.TextChoices):
    A1 = "A1", "A1"
    A2 = "A2", "A2"
    B1 = "B1", "B1"
    B2 = "B2", "B2"
    C1 = "C1", "C1"
    C2 = "C2", "C2"


class LessonKind(models.TextChoices):
    WORDS = "words", "Новые слова"
    GRAMMAR = "grammar", "Грамматика"
    REVIEW = "review", "Повторение"
    QUIZ = "quiz", "Мини-тест"


class Course(models.Model):
    id = models.SlugField(primary_key=True, max_length=64)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    level = models.CharField(max_length=2, choices=Level.choices, default=Level.A1)
    position = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "courses"
        ordering = ("position", "id")

    def __str__(self):
        return f"{self.level} · {self.title}"


class Topic(models.Model):
    id = models.SlugField(primary_key=True, max_length=80)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    emoji = models.CharField(max_length=8, blank=True)
    position = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "topics"
        ordering = ("position", "id")
        constraints = [
            models.UniqueConstraint(
                fields=("course", "position"), name="unique_topic_position"
            )
        ]

    def __str__(self):
        return f"{self.course.level} · {self.title}"


class Lesson(models.Model):
    id = models.SlugField(primary_key=True, max_length=32)
    title = models.CharField(max_length=120)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.SET_NULL,
        related_name="lessons",
        blank=True,
        null=True,
    )
    kind = models.CharField(
        max_length=16, choices=LessonKind.choices, default=LessonKind.WORDS
    )
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


class LessonFlashcard(models.Model):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name="flashcard_links"
    )
    flashcard = models.ForeignKey(
        Flashcard, on_delete=models.CASCADE, related_name="lesson_links"
    )
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = "lesson_flashcards"
        ordering = ("position", "flashcard_id")
        constraints = [
            models.UniqueConstraint(
                fields=("lesson", "flashcard"), name="unique_lesson_flashcard"
            ),
            models.UniqueConstraint(
                fields=("lesson", "position"),
                name="unique_lesson_flashcard_position",
            ),
        ]


class ReadingText(models.Model):
    id = models.SlugField(primary_key=True, max_length=80)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.SET_NULL,
        related_name="reading_texts",
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=160)
    description = models.CharField(max_length=240)
    level = models.CharField(max_length=2, choices=Level.choices, default=Level.A1)
    minutes = models.PositiveSmallIntegerField(default=5)
    emoji = models.CharField(max_length=8, blank=True)
    paragraphs = models.JSONField(default=list)
    glossary = models.JSONField(default=dict)
    position = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "reading_texts"
        ordering = ("position", "id")

    def __str__(self):
        return f"{self.level} · {self.title}"


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
    lesson_id = models.CharField(max_length=80)
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


class PersonalWord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField(db_index=True)
    word = models.CharField(max_length=160)
    translation = models.CharField(max_length=240)
    context = models.TextField(blank=True)
    source_text_id = models.CharField(max_length=80, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "personal_words"
        managed = False
        ordering = ("-created_at",)
        constraints = [
            models.UniqueConstraint(
                fields=("user_id", "word"), name="unique_personal_word"
            )
        ]
