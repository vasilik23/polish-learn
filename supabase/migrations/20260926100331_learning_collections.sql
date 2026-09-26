create table public.learning_collections (
  id uuid primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  name text not null check (char_length(name) between 1 and 60),
  created_at timestamptz not null default now(),
  unique (id, user_id)
);

create table public.learning_collection_items (
  id uuid primary key,
  collection_id uuid not null,
  user_id uuid not null references auth.users(id) on delete cascade,
  content_type text not null check (content_type in ('lesson', 'reading')),
  content_id text not null,
  created_at timestamptz not null default now(),
  unique (collection_id, content_type, content_id),
  foreign key (collection_id, user_id)
    references public.learning_collections(id, user_id) on delete cascade
);

create index learning_collections_user_idx on public.learning_collections(user_id, created_at);
create index learning_collection_items_user_idx on public.learning_collection_items(user_id, collection_id, created_at);

alter table public.learning_collections enable row level security;
alter table public.learning_collection_items enable row level security;
revoke all on table public.learning_collections, public.learning_collection_items from anon;
revoke all on table public.learning_collections, public.learning_collection_items from authenticated;
grant select, insert, update, delete on table public.learning_collections, public.learning_collection_items to authenticated;

create policy "collections_select_own" on public.learning_collections for select to authenticated using ((select auth.uid()) = user_id);
create policy "collections_insert_own" on public.learning_collections for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "collections_update_own" on public.learning_collections for update to authenticated using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
create policy "collections_delete_own" on public.learning_collections for delete to authenticated using ((select auth.uid()) = user_id);
create policy "collection_items_select_own" on public.learning_collection_items for select to authenticated using ((select auth.uid()) = user_id);
create policy "collection_items_insert_own" on public.learning_collection_items for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "collection_items_delete_own" on public.learning_collection_items for delete to authenticated using ((select auth.uid()) = user_id);
