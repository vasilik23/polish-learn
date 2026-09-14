import json
from pathlib import Path
from tempfile import TemporaryDirectory

from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import SimpleTestCase


def report(score=0.95, accessibility=1.0, lcp=1900, cls=0.02, tbt=80, ttfb=100):
    return {
        "categories": {
            "performance": {"score": score},
            "accessibility": {"score": accessibility},
        },
        "audits": {
            "largest-contentful-paint": {"numericValue": lcp},
            "cumulative-layout-shift": {"numericValue": cls},
            "total-blocking-time": {"numericValue": tbt},
            "server-response-time": {"numericValue": ttfb},
        },
    }


class PerformanceBudgetTests(SimpleTestCase):
    def write_reports(self, directory, payloads):
        paths = []
        for index, payload in enumerate(payloads):
            path = Path(directory) / f"report-{index}.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            paths.append(str(path))
        return paths

    def test_command_accepts_passing_median_and_reports_diagnostic_ttfb(self):
        with TemporaryDirectory() as directory:
            paths = self.write_reports(directory, [
                report(score=0.91, lcp=2400, ttfb=300),
                report(score=0.98, lcp=1800, ttfb=100),
                report(score=0.95, lcp=2000, ttfb=200),
            ])
            output = __import__("io").StringIO()
            call_command("check_lighthouse_budget", *paths, stdout=output)
        self.assertIn('"lcp_ms": 2000.0', output.getvalue())
        self.assertIn('"accessibility_score": 100.0', output.getvalue())
        self.assertIn('"ttfb_ms": 200.0', output.getvalue())
        self.assertIn("Performance budget passed", output.getvalue())

    def test_command_rejects_failed_budget(self):
        with TemporaryDirectory() as directory:
            paths = self.write_reports(directory, [report(lcp=3000)] * 3)
            with self.assertRaisesMessage(CommandError, "LCP > 2500 ms"):
                call_command("check_lighthouse_budget", *paths)

    def test_command_requires_three_valid_reports(self):
        with TemporaryDirectory() as directory:
            paths = self.write_reports(directory, [report()] * 2)
            with self.assertRaisesMessage(CommandError, "At least three"):
                call_command("check_lighthouse_budget", *paths)

    def test_command_rejects_accessibility_regression(self):
        with TemporaryDirectory() as directory:
            paths = self.write_reports(directory, [report(accessibility=0.94)] * 3)
            with self.assertRaisesMessage(CommandError, "accessibility score < 95"):
                call_command("check_lighthouse_budget", *paths)
