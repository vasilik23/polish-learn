from datetime import date
from unittest import TestCase

from polskiflow.domain.progress import next_streak


class NextStreakTests(TestCase):
    TODAY = date(2026, 8, 17)

    def test_starts_first_streak(self):
        self.assertEqual(next_streak(0, None, self.TODAY), 1)

    def test_same_day_does_not_increment(self):
        self.assertEqual(next_streak(4, self.TODAY, self.TODAY), 4)

    def test_consecutive_day_increments(self):
        self.assertEqual(next_streak(4, date(2026, 8, 16), self.TODAY), 5)

    def test_gap_resets_streak(self):
        self.assertEqual(next_streak(12, date(2026, 8, 15), self.TODAY), 1)

    def test_negative_streak_is_rejected(self):
        with self.assertRaises(ValueError):
            next_streak(-1, None, self.TODAY)
