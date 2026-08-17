import uuid
from datetime import date, datetime, timezone

from django.test import TestCase

from .models import FlashcardReview, LessonCompletion, Profile


class LearningModelsTests(TestCase):
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
