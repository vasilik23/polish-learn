import uuid
from datetime import date, datetime, timezone

from django.db import connection
from django.test import TransactionTestCase

from .models import (
    Course,
    Flashcard,
    FlashcardReview,
    Lesson,
    LessonCompletion,
    LessonFlashcard,
    PersonalWord,
    Profile,
    ReadingText,
    Topic,
)


class LearningModelsTests(TransactionTestCase):
    """Exercise mappings against temporary stand-ins for Supabase-owned tables."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        with connection.schema_editor() as editor:
            for model in (Profile, LessonCompletion, FlashcardReview, PersonalWord):
                editor.create_model(model)

    @classmethod
    def tearDownClass(cls):
        with connection.schema_editor() as editor:
            for model in (PersonalWord, FlashcardReview, LessonCompletion, Profile):
                editor.delete_model(model)
        super().tearDownClass()

    def test_profile_defaults_match_current_mvp(self):
        profile = Profile.objects.create(id=uuid.uuid4())

        self.assertEqual(profile.level, "A1")
        self.assertEqual(profile.streak_days, 0)

    def test_lesson_completion_is_persisted(self):
        completion = LessonCompletion.objects.create(
            user_id=uuid.uuid4(),
            lesson_id="quiz",
            plan_date=date(2026, 8, 17),
            cards_total=5,
            cards_known=4,
            completed_at=datetime(2026, 8, 17, 12, tzinfo=timezone.utc),
        )

        self.assertEqual(
            LessonCompletion.objects.get(pk=completion.pk).cards_known,
            4,
        )

    def test_flashcard_review_uses_user_and_card_composite_key(self):
        user_id = uuid.uuid4()
        review = FlashcardReview.objects.create(
            user_id=user_id,
            card_id="czesc",
            next_review_date=date(2026, 8, 18),
        )

        self.assertEqual(review.pk, (user_id, "czesc"))
        self.assertTrue(
            FlashcardReview.objects.filter(
                user_id=user_id,
                card_id="czesc",
            ).exists()
        )

    def test_course_topic_and_lesson_vocabulary_are_related(self):
        course = Course.objects.create(id="a1-test", title="A1 test")
        topic = Topic.objects.create(id="greetings-test", course=course, title="Greetings")
        lesson = Lesson.objects.create(
            id="hello-test",
            topic=topic,
            kind="words",
            title="Hello",
            plan_title="Hello",
            subtitle="Test",
            description="Test lesson",
        )
        card = Flashcard.objects.create(
            id="witaj-test", polish="witaj", translation="привет"
        )
        LessonFlashcard.objects.create(lesson=lesson, flashcard=card)

        self.assertEqual(topic.lessons.get(), lesson)
        self.assertEqual(lesson.flashcard_links.get().flashcard, card)

    def test_reading_text_and_personal_word_models_match_content_flow(self):
        text = ReadingText.objects.create(
            id="reading-test",
            title="Reading test",
            description="Test",
            paragraphs=["To jest dom."],
            glossary={"dom": "дом"},
        )
        user_id = uuid.uuid4()
        word = PersonalWord.objects.create(
            user_id=user_id,
            word="dom",
            translation="дом",
            source_text_id=text.id,
        )

        self.assertEqual(ReadingText.objects.get().glossary["dom"], "дом")
        self.assertEqual(PersonalWord.objects.get(pk=word.pk).user_id, user_id)
