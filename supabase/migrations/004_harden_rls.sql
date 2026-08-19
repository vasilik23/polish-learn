-- Review in a preview/staging Supabase project before production execution.
-- This script is idempotent and does not alter or delete application data.

revoke execute on function public.handle_new_user() from public, anon, authenticated;

drop policy if exists "Users can update own profile" on public.profiles;
create policy "Users can update own profile"
  on public.profiles for update
  using (auth.uid() = id)
  with check (auth.uid() = id);

drop policy if exists "Users can update own lesson completions" on public.lesson_completions;
create policy "Users can update own lesson completions"
  on public.lesson_completions for update
  using (auth.uid() = user_id)
  with check (auth.uid() = user_id);

drop policy if exists "Users can update own flashcard reviews" on public.flashcard_reviews;
create policy "Users can update own flashcard reviews"
  on public.flashcard_reviews for update
  using (auth.uid() = user_id)
  with check (auth.uid() = user_id);

drop policy if exists "Users can delete own flashcard reviews" on public.flashcard_reviews;
create policy "Users can delete own flashcard reviews"
  on public.flashcard_reviews for delete
  using (auth.uid() = user_id);
