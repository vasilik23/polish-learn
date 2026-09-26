create table if not exists public.lesson_notes (
  user_id uuid not null references auth.users(id) on delete cascade,
  lesson_id text not null references public.lessons(id) on delete cascade,
  body text not null check (char_length(body) between 1 and 2000),
  updated_at timestamptz not null default now(),
  primary key (user_id, lesson_id)
);

create index if not exists lesson_notes_lesson_id_idx
  on public.lesson_notes (lesson_id);

alter table public.lesson_notes enable row level security;

revoke all on table public.lesson_notes from anon;
revoke all on table public.lesson_notes from authenticated;
grant select, insert, update, delete on table public.lesson_notes to authenticated;

drop policy if exists "lesson_notes_select_own" on public.lesson_notes;
create policy "lesson_notes_select_own"
  on public.lesson_notes for select to authenticated
  using ((select auth.uid()) = user_id);

drop policy if exists "lesson_notes_insert_own" on public.lesson_notes;
create policy "lesson_notes_insert_own"
  on public.lesson_notes for insert to authenticated
  with check ((select auth.uid()) = user_id);

drop policy if exists "lesson_notes_update_own" on public.lesson_notes;
create policy "lesson_notes_update_own"
  on public.lesson_notes for update to authenticated
  using ((select auth.uid()) = user_id)
  with check ((select auth.uid()) = user_id);

drop policy if exists "lesson_notes_delete_own" on public.lesson_notes;
create policy "lesson_notes_delete_own"
  on public.lesson_notes for delete to authenticated
  using ((select auth.uid()) = user_id);
