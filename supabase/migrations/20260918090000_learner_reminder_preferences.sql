create table if not exists public.reminder_preferences (
  user_id uuid primary key references auth.users(id) on delete cascade,
  daily_reminder_enabled boolean not null default false,
  reminder_time time not null default '19:00',
  timezone text not null default 'Europe/Warsaw',
  updated_at timestamptz not null default now(),
  constraint reminder_preferences_timezone_length check (char_length(timezone) between 1 and 64)
);

alter table public.reminder_preferences enable row level security;
revoke all on table public.reminder_preferences from anon;
revoke all on table public.reminder_preferences from authenticated;
grant select, insert, update on table public.reminder_preferences to authenticated;

create policy "Users can read own reminder preferences"
  on public.reminder_preferences for select to authenticated
  using ((select auth.uid()) = user_id);
create policy "Users can insert own reminder preferences"
  on public.reminder_preferences for insert to authenticated
  with check ((select auth.uid()) = user_id);
create policy "Users can update own reminder preferences"
  on public.reminder_preferences for update to authenticated
  using ((select auth.uid()) = user_id)
  with check ((select auth.uid()) = user_id);
