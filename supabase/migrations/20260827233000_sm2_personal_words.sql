-- Add per-user SM-2 scheduling to personal dictionary entries.
-- The existing ownership RLS policies continue to protect every updated row.

alter table public.personal_words
  add column if not exists ease_factor double precision not null default 2.5,
  add column if not exists interval_days integer not null default 0,
  add column if not exists repetitions integer not null default 0,
  add column if not exists next_review_date date not null default (timezone('utc', now()))::date,
  add column if not exists last_reviewed_at timestamptz;

alter table public.personal_words
  drop constraint if exists personal_word_minimum_ease,
  add constraint personal_word_minimum_ease check (ease_factor >= 1.3),
  drop constraint if exists personal_word_nonnegative_interval,
  add constraint personal_word_nonnegative_interval check (interval_days >= 0),
  drop constraint if exists personal_word_nonnegative_repetitions,
  add constraint personal_word_nonnegative_repetitions check (repetitions >= 0);

create index if not exists personal_words_user_due_idx
  on public.personal_words(user_id, next_review_date, created_at);

-- No new table or privilege is exposed. Keep the existing authenticated-only
-- SELECT/INSERT/UPDATE/DELETE grant and owner-scoped SELECT/UPDATE policies.
alter table public.personal_words enable row level security;
