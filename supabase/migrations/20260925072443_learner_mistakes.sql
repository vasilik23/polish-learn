create table if not exists public.learner_mistakes (
  user_id uuid not null references auth.users(id) on delete cascade,
  lesson_id text not null references public.lessons(id) on delete cascade,
  question_position smallint not null check (question_position >= 0),
  last_wrong_at timestamptz not null default now(),
  primary key (user_id, lesson_id, question_position)
);

create index if not exists learner_mistakes_lesson_id_idx
  on public.learner_mistakes (lesson_id);

alter table public.learner_mistakes enable row level security;
revoke all on table public.learner_mistakes from anon;
revoke all on table public.learner_mistakes from authenticated;
grant select, insert, update, delete on table public.learner_mistakes to authenticated;

create policy "Users can read own mistakes" on public.learner_mistakes
  for select to authenticated using ((select auth.uid()) = user_id);
create policy "Users can insert own mistakes" on public.learner_mistakes
  for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "Users can update own mistakes" on public.learner_mistakes
  for update to authenticated using ((select auth.uid()) = user_id)
  with check ((select auth.uid()) = user_id);
create policy "Users can delete own mistakes" on public.learner_mistakes
  for delete to authenticated using ((select auth.uid()) = user_id);
