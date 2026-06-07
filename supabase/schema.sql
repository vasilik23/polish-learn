-- Запустите в Supabase SQL Editor после создания проекта

-- Профиль пользователя (расширение auth.users)
create table if not exists public.profiles (
  id uuid primary key references auth.users (id) on delete cascade,
  display_name text,
  level text default 'A1' check (level in ('A1', 'A2', 'B1', 'B2', 'C1', 'C2')),
  streak_days int not null default 0,
  last_active_date date,
  created_at timestamptz default now()
);

alter table public.profiles enable row level security;

create policy "Users can read own profile"
  on public.profiles for select
  using (auth.uid() = id);

create policy "Users can update own profile"
  on public.profiles for update
  using (auth.uid() = id);

create policy "Users can insert own profile"
  on public.profiles for insert
  with check (auth.uid() = id);

-- Автосоздание профиля при регистрации
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer set search_path = public
as $$
begin
  insert into public.profiles (id, display_name)
  values (new.id, split_part(new.email, '@', 1));
  return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();

-- Прогресс уроков (и плана на день — один урок = один пункт плана)
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
