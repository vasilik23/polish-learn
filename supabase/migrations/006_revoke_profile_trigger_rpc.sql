-- The trigger owner may execute this function; browser-facing roles must not.
revoke all privileges on function public.handle_new_user() from public, anon, authenticated;
