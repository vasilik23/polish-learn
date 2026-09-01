-- The two legacy A1 readings were moved to introductions in the preceding
-- migration. Keep the now-empty compatibility topic out of the active catalog.
update public.topics
set is_active = false
where id = 'first-steps';
