from datetime import date
from unittest import TestCase

from polskiflow.domain.sm2 import DEFAULT_SM2_STATE, Sm2State, sm2_next


class Sm2NextTests(TestCase):
    TODAY = date(2026, 8, 17)

    def test_first_known_card_returns_in_one_day(self):
        result = sm2_next(DEFAULT_SM2_STATE, "know", self.TODAY)

        self.assertEqual(result.repetitions, 1)
        self.assertEqual(result.interval_days, 1)
        self.assertEqual(result.ease_factor, 2.6)
        self.assertEqual(result.next_review_date, date(2026, 8, 18))

    def test_second_known_card_returns_in_six_days(self):
        state = Sm2State(ease_factor=2.6, interval_days=1, repetitions=1)
        result = sm2_next(state, "know", self.TODAY)

        self.assertEqual(result.repetitions, 2)
        self.assertEqual(result.interval_days, 6)
        self.assertEqual(result.next_review_date, date(2026, 8, 23))

    def test_later_interval_uses_ease_factor(self):
        state = Sm2State(ease_factor=2.5, interval_days=6, repetitions=2)
        result = sm2_next(state, "know", self.TODAY)

        self.assertEqual(result.repetitions, 3)
        self.assertEqual(result.interval_days, 15)
        self.assertEqual(result.next_review_date, date(2026, 9, 1))

    def test_interval_matches_javascript_half_rounding(self):
        state = Sm2State(ease_factor=2.5, interval_days=5, repetitions=2)
        result = sm2_next(state, "know", self.TODAY)

        self.assertEqual(result.interval_days, 13)

    def test_again_resets_repetitions_and_interval(self):
        state = Sm2State(ease_factor=2.5, interval_days=15, repetitions=3)
        result = sm2_next(state, "again", self.TODAY)

        self.assertEqual(result.repetitions, 0)
        self.assertEqual(result.interval_days, 1)
        self.assertAlmostEqual(result.ease_factor, 1.96)
        self.assertEqual(result.next_review_date, date(2026, 8, 18))

    def test_ease_factor_never_falls_below_minimum(self):
        state = Sm2State(ease_factor=1.3, interval_days=1, repetitions=0)
        result = sm2_next(state, "again", self.TODAY)

        self.assertEqual(result.ease_factor, 1.3)

    def test_unknown_quality_is_rejected(self):
        with self.assertRaises(ValueError):
            sm2_next(DEFAULT_SM2_STATE, "easy", self.TODAY)  # type: ignore[arg-type]
