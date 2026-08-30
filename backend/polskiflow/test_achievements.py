from django.test import SimpleTestCase

from polskiflow.domain.achievements import build_achievements


class AchievementTests(SimpleTestCase):
    def test_milestones_are_derived_and_progress_is_capped(self):
        achievements = build_achievements(
            completed_lessons=12, streak_days=4, dictionary_count=7, active_days=5
        )
        by_id = {item.id: item for item in achievements}

        self.assertTrue(by_id["first-step"].unlocked)
        self.assertTrue(by_id["momentum"].unlocked)
        self.assertEqual(by_id["momentum"].progress_percent, 100)
        self.assertTrue(by_id["streak-three"].unlocked)
        self.assertFalse(by_id["streak-seven"].unlocked)
        self.assertEqual(by_id["word-collector"].progress_percent, 28)

    def test_zero_progress_is_safe(self):
        achievements = build_achievements(
            completed_lessons=0, streak_days=0, dictionary_count=0, active_days=0
        )
        self.assertTrue(all(not item.unlocked for item in achievements))
        self.assertTrue(all(item.progress_percent == 0 for item in achievements))
