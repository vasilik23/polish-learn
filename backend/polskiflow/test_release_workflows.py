from pathlib import Path

from django.test import SimpleTestCase


class ReleaseWorkflowTests(SimpleTestCase):
    def test_lighthouse_workflow_is_manual_sequential_and_budgeted(self):
        workflow = (
            Path(__file__).resolve().parents[2]
            / ".github/workflows/lighthouse-preview.yml"
        ).read_text(encoding="utf-8")

        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("https://*)", workflow)
        self.assertIn("lighthouse@13.4.1", workflow)
        self.assertIn("for route in login sources", workflow)
        self.assertIn("for run_number in 1 2 3", workflow)
        self.assertNotIn("&\n", workflow)
        self.assertEqual(workflow.count("manage.py check_lighthouse_budget"), 2)
        self.assertIn("actions/upload-artifact@v4", workflow)
