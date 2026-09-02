# PolskiFlow API v1

`GET /api/v1/catalog/` is the first read-only contract for future mobile and
other separate clients. `HEAD` is supported; mutation methods return `405`.
The endpoint is public because the same active learning tables are readable by
the Supabase `anon` role. It never includes profiles, progress, reviews,
personal dictionary entries, access tokens, quiz answers, flashcards, or full
lesson theory.

## Envelope and versioning

Every response is JSON with these stable top-level fields:

```json
{
  "api_version": "v1",
  "meta": {
    "contract": "public-course-catalog",
    "contract_version": "1.0.0",
    "generated_at": "2026-09-02T10:00:00+00:00",
    "levels": ["A1", "A2", "B1", "B2", "C1", "C2"],
    "course_count": 6
  },
  "data": { "courses": [] }
}
```

`api_version` versions the URL family. `contract_version` follows semantic
versioning for this payload: additive optional fields increment the minor
version; removals, renames, type changes, or changed field meaning require a
new major API path. `generated_at` is an ISO 8601 UTC timestamp for the response
snapshot and must not be used as a content identifier.

## Catalog schema

- `course`: `id`, `title`, `description`, `level`, `position`, `topics`;
- `topic`: `id`, `title`, `description`, `emoji`, `position`, `lessons`;
- `lesson`: `id`, `title`, `description`, `kind`, `minutes`, `emoji`, `position`.

Only active courses, active topics with active lessons, and active lessons are
returned. Arrays are deterministic: courses, topics, and lessons are ordered by
`position`, then `id`. Clients should treat IDs as opaque strings and tolerate
new fields. Responses allow short shared-cache reuse; clients must not infer
that the catalog is permanently immutable.

## Learner contracts

Two read-only endpoints provide the minimum owner-scoped state needed by a
future separate client:

- `GET /api/v1/me/progress/` — profile level and daily goal, streak, active
  days, deterministic completed lesson IDs, and week/month aggregates;
- `GET /api/v1/me/sm2/` — personal dictionary review schedule, current due
  count, and the SM-2 fields required to render the learner's queue.

Both accept the existing Supabase access token as
`Authorization: Bearer <access-token>`. Browser sessions may use the existing
HttpOnly cookie. Missing or invalid authentication returns `401`; mutations
return `405`; a temporary owner-scoped Data API failure returns `503` with
`error.code = "upstream_unavailable"` instead of an empty successful payload.

Learner responses use contract version `1.0.0`, `Cache-Control: private,
no-store`, and `Vary: Authorization, Cookie`. The backend forwards the same
user access token to Supabase, so existing RLS remains the authorization
boundary. The API never accepts a user ID from the client and never exposes
access or refresh tokens. These contracts are intentionally read-only: result
submission and offline synchronization need separate idempotency and conflict
rules before they can become public API operations.

## Lesson-result write contract

`POST /api/v1/me/lesson-results/` implements the first idempotent write
contract. Unlike read endpoints, it requires an explicit Supabase
`Authorization: Bearer` token; cookie-only requests are rejected even though
the view is CSRF-exempt for native clients. The JSON body is capped at 8 KiB
and follows [the result-sync design](api-result-sync.md).

The server rejects client-supplied ownership fields, validates the active
lesson and canonicalizes the payload before hashing it. The first event returns
`201 created`, an exact retry returns `200 duplicate`, and reuse of an
`event_id` for different data returns `409 idempotency_conflict`. Event storage
and the existing daily completion projection are updated atomically by a
`security invoker` Supabase function operating under the caller's RLS context.
