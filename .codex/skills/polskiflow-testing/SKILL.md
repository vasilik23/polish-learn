---
name: polskiflow-testing
description: Verify PolskiFlow changes locally, in Supabase, and on Vercel. Use for Django tests, system and migration checks, regression coverage, browser testing, accessibility smoke checks, database assertions, RLS review, production smoke tests, and deployment log scans.
---

# PolskiFlow testing

Run checks proportional to risk, with this full release baseline:

1. `backend/.venv/bin/python backend/manage.py test`
2. Django `check` and `makemigrations --check --dry-run`.
3. `git diff --check`; inspect migration and secret exposure.
4. For UI changes, start Django and use a real browser: meaningful content, key navigation, mobile viewport, no overlay, no console errors, and an annotated screenshot when useful.
5. For Supabase changes, query prerequisites, apply only the reviewed ordered migration, assert row counts and behavior, then run security advisors. Confirm RLS and grants for every exposed table.
6. Wait for GitHub and Vercel checks. After merge, authenticate in production, exercise the changed flow, and scan Vercel error logs.
7. Report pass/fail, exact checks, deployment URL, and any known gap. Never describe an unrun check as passing.

Use temporary settings only outside the repository and never commit credentials or browser state.
