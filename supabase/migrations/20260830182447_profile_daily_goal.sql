alter table public.profiles
  add column if not exists daily_goal_lessons smallint not null default 4;

alter table public.profiles
  drop constraint if exists profiles_daily_goal_lessons_check;

alter table public.profiles
  add constraint profiles_daily_goal_lessons_check
  check (daily_goal_lessons between 1 and 10);
