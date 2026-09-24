create table if not exists public.lesson_bookmarks (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  lesson_id text not null references public.lessons(id) on delete cascade,
  created_at timestamptz not null default now(),
  constraint lesson_bookmarks_user_lesson_unique unique (user_id, lesson_id)
);

create index if not exists lesson_bookmarks_lesson_id_idx
  on public.lesson_bookmarks (lesson_id);

alter table public.lesson_bookmarks enable row level security;
revoke all on table public.lesson_bookmarks from anon;
revoke all on table public.lesson_bookmarks from authenticated;
grant select, insert, delete on table public.lesson_bookmarks to authenticated;

create policy "Users can read own lesson bookmarks"
  on public.lesson_bookmarks for select to authenticated
  using ((select auth.uid()) = user_id);
create policy "Users can insert own lesson bookmarks"
  on public.lesson_bookmarks for insert to authenticated
  with check ((select auth.uid()) = user_id);
create policy "Users can delete own lesson bookmarks"
  on public.lesson_bookmarks for delete to authenticated
  using ((select auth.uid()) = user_id);
