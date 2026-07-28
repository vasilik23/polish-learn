-- Выполните в SQL Editor после 002_progress.sql

create table if not exists public.flashcard_reviews (
  user_id uuid not null references auth.users (id) on delete cascade,
  card_id text not null,
  ease_factor float not null default 2.5 check (ease_factor >= 1.3),
  interval_days int not null default 0,
  repetitions int not null default 0,
  next_review_date date not null default (timezone('utc', now()))::date,
  last_reviewed_at timestamptz,
  primary key (user_id, card_id)
);

alter table public.flashcard_reviews enable row level security;

create policy "Users can read own flashcard reviews"
  on public.flashcard_reviews for select
  using (auth.uid() = user_id);

create policy "Users can insert own flashcard reviews"
  on public.flashcard_reviews for insert
  with check (auth.uid() = user_id);

create policy "Users can update own flashcard reviews"
  on public.flashcard_reviews for update
  using (auth.uid() = user_id);
