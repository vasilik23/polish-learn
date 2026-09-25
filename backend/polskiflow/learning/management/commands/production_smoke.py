"""Run the read-only production synthetic smoke from an operator shell."""

import os

from django.core.management.base import BaseCommand, CommandError

from polskiflow.domain.synthetic_smoke import SmokeFailure, run_synthetic_smoke


class Command(BaseCommand):
    help = "Check public probes and the authenticated mobile cold-start path without writes"

    def add_arguments(self, parser):
        parser.add_argument("base_url", help="Production or Preview HTTPS origin")
        parser.add_argument(
            "--token-env",
            default="POLSKIFLOW_SMOKE_ACCESS_TOKEN",
            help="Environment variable containing a short-lived learner access token",
        )
        parser.add_argument("--timeout", type=float, default=10)
        parser.add_argument(
            "--public-only",
            action="store_true",
            help="Check public contracts without a learner token",
        )

    def handle(self, *args, **options):
        public_only = options["public_only"]
        token = os.environ.get(options["token_env"], "") if not public_only else ""
        if not public_only and not token:
            raise CommandError(f"Missing access token in {options['token_env']}")
        try:
            results = run_synthetic_smoke(
                options["base_url"], token, timeout=options["timeout"],
                include_private=not public_only,
            )
        except SmokeFailure as error:
            raise CommandError(str(error)) from error
        for result in results:
            self.stdout.write(f"PASS {result.name} status={result.status} request_id={result.request_id}")
        self.stdout.write(self.style.SUCCESS(f"Synthetic smoke passed ({len(results)} checks)"))
