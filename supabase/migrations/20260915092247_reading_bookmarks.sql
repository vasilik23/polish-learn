create table if not exists public.reading_bookmarks (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  reading_text_id text not null references public.reading_texts(id) on delete cascade,
  created_at timestamptz not null default now(),
  constraint reading_bookmarks_user_text_unique unique (user_id, reading_text_id)
);

alter table public.reading_bookmarks enable row level security;
revoke all on table public.reading_bookmarks from anon;
revoke all on table public.reading_bookmarks from authenticated;
grant select, insert, delete on table public.reading_bookmarks to authenticated;

create policy "Users can read own reading bookmarks"
  on public.reading_bookmarks for select to authenticated
  using ((select auth.uid()) = user_id);
create policy "Users can insert own reading bookmarks"
  on public.reading_bookmarks for insert to authenticated
  with check ((select auth.uid()) = user_id);
create policy "Users can delete own reading bookmarks"
  on public.reading_bookmarks for delete to authenticated
  using ((select auth.uid()) = user_id);
