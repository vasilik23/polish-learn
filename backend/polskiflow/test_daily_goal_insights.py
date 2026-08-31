from django.test import SimpleTestCase

from polskiflow.domain.daily_goal_insights import build_daily_goal_insight


class DailyGoalInsightTests(SimpleTestCase):
    def test_success_share_uses_all_28_calendar_days(self):
        insight = build_daily_goal_insight([2] * 14 + [0] * 14, current_goal=2)

        self.assertEqual(insight.successful_days, 14)
        self.assertEqual(insight.success_rate, 50)
        self.assertEqual(insight.active_days, 14)
        self.assertEqual(insight.typical_active_day_lessons, 2)
        self.assertEqual(insight.status, "sustainable")

    def test_sparse_history_is_reported_as_incomplete(self):
        insight = build_daily_goal_insight([0] * 25 + [4, 0, 4], current_goal=4)

        self.assertEqual(insight.status, "collecting")
        self.assertIn("ещё на несколько занятий", insight.recommendation)

    def test_demanding_goal_gets_a_gentle_lower_suggestion(self):
        insight = build_daily_goal_insight([2] * 8 + [0] * 20, current_goal=5)

        self.assertEqual(insight.status, "demanding")
        self.assertEqual(insight.typical_active_day_lessons, 2)
        self.assertIn("временно 2 в день", insight.recommendation)
        self.assertIn("можно оставить как ориентир", insight.recommendation)

    def test_partial_input_is_padded_to_a_fixed_28_day_window(self):
        insight = build_daily_goal_insight([1, 1, 1, 1], current_goal=1)

        self.assertEqual(insight.period_days, 28)
        self.assertEqual(insight.successful_days, 4)
        self.assertEqual(insight.success_rate, 14)
