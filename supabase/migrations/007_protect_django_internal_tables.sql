-- Django owns these tables through its PostgreSQL connection. They are not part
-- of the browser-facing Supabase Data API and must not expose rows or metadata.

alter table public.auth_group enable row level security;
alter table public.auth_group_permissions enable row level security;
alter table public.auth_permission enable row level security;
alter table public.auth_user enable row level security;
alter table public.auth_user_groups enable row level security;
alter table public.auth_user_user_permissions enable row level security;
alter table public.django_admin_log enable row level security;
alter table public.django_content_type enable row level security;
alter table public.django_migrations enable row level security;
alter table public.django_session enable row level security;

revoke all privileges on table
  public.auth_group,
  public.auth_group_permissions,
  public.auth_permission,
  public.auth_user,
  public.auth_user_groups,
  public.auth_user_user_permissions,
  public.django_admin_log,
  public.django_content_type,
  public.django_migrations,
  public.django_session
from public, anon, authenticated;

revoke all privileges on sequence
  public.auth_group_id_seq,
  public.auth_permission_id_seq,
  public.auth_user_id_seq,
  public.django_admin_log_id_seq,
  public.django_content_type_id_seq
from public, anon, authenticated;
