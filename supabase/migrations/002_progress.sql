-- Выполните в SQL Editor, если schema.sql уже был запущен раньше

alter table public.profiles
  add column if not exists streak_days int not null default 0,
  add column if not exists last_active_date date;

create table if not exists public.lesson_completions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users (id) on delete cascade,
  lesson_id text not null check (lesson_id in ('words', 'grammar', 'review', 'quiz')),
  plan_date date not null default (timezone('utc', now()))::date,
  cards_total int not null default 0,
  cards_known int not null default 0,
  completed_at timestamptz not null default now(),
  unique (user_id, lesson_id, plan_date)
);

alter table public.lesson_completions enable row level security;

create policy "Users can read own lesson completions"
  on public.lesson_completions for select
  using (auth.uid() = user_id);

create policy "Users can insert own lesson completions"
  on public.lesson_completions for insert
  with check (auth.uid() = user_id);

create policy "Users can update own lesson completions"
  on public.lesson_completions for update
  using (auth.uid() = user_id);

-- Профили для пользователей, созданных до триггера
insert into public.profiles (id, display_name)
select id, split_part(email, '@', 1)
from auth.users
where id not in (select id from public.profiles);
