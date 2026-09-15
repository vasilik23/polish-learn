create table public.user_feedback (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  category text not null check (category in ('content', 'translation', 'interface', 'technical', 'idea')),
  message text not null check (char_length(message) between 20 and 2000),
  page_url text not null default '' check (char_length(page_url) <= 300),
  status text not null default 'new' check (status in ('new', 'reviewed', 'resolved')),
  created_at timestamptz not null default now()
);
create index user_feedback_user_created_idx on public.user_feedback (user_id, created_at desc);
alter table public.user_feedback enable row level security;
revoke all on table public.user_feedback from anon, authenticated;
grant select, insert on table public.user_feedback to authenticated;
create policy "Users can read own feedback" on public.user_feedback for select to authenticated using ((select auth.uid()) = user_id);
create policy "Users can submit own feedback" on public.user_feedback for insert to authenticated with check ((select auth.uid()) = user_id and status = 'new');
