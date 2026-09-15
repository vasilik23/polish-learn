create table if not exists public.lesson_drafts (
  user_id uuid not null references auth.users(id) on delete cascade,
  lesson_id text not null references public.lessons(id) on delete cascade,
  lesson_kind text not null check (lesson_kind in ('words', 'review', 'grammar', 'quiz')),
  step_index integer not null default 0 check (step_index >= 0 and step_index <= 1000),
  score integer not null default 0 check (score >= 0 and score <= step_index),
  updated_at timestamptz not null default now(),
  primary key (user_id, lesson_id)
);

create index if not exists lesson_drafts_user_updated_idx
  on public.lesson_drafts (user_id, updated_at desc);
create index if not exists lesson_drafts_lesson_id_idx
  on public.lesson_drafts (lesson_id);

alter table public.lesson_drafts enable row level security;
revoke all on public.lesson_drafts from anon, authenticated;
grant select, insert, update, delete on public.lesson_drafts to authenticated;

drop policy if exists "Learners select own lesson drafts" on public.lesson_drafts;
create policy "Learners select own lesson drafts" on public.lesson_drafts
  for select to authenticated using ((select auth.uid()) = user_id);
drop policy if exists "Learners insert own lesson drafts" on public.lesson_drafts;
create policy "Learners insert own lesson drafts" on public.lesson_drafts
  for insert to authenticated with check ((select auth.uid()) = user_id);
drop policy if exists "Learners update own lesson drafts" on public.lesson_drafts;
create policy "Learners update own lesson drafts" on public.lesson_drafts
  for update to authenticated
  using ((select auth.uid()) = user_id)
  with check ((select auth.uid()) = user_id);
drop policy if exists "Learners delete own lesson drafts" on public.lesson_drafts;
create policy "Learners delete own lesson drafts" on public.lesson_drafts
  for delete to authenticated using ((select auth.uid()) = user_id);
