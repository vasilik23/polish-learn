import json

from django.core.management.base import BaseCommand, CommandError

from polskiflow.domain.performance_budget import (
    LighthouseReportError,
    evaluate_lighthouse_reports,
)


class Command(BaseCommand):
    help = "Check the median of three or more sequential Lighthouse JSON reports."

    def add_arguments(self, parser):
        parser.add_argument("reports", nargs="+", help="Lighthouse JSON report paths")

    def handle(self, *args, **options):
        try:
            median, failures = evaluate_lighthouse_reports(options["reports"])
        except LighthouseReportError as exc:
            raise CommandError(str(exc)) from exc
        self.stdout.write(json.dumps(median.as_dict(), sort_keys=True))
        if failures:
            raise CommandError("Performance budget failed: " + ", ".join(failures))
        self.stdout.write(self.style.SUCCESS("Performance budget passed"))
