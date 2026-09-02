create table public.lesson_result_events (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  event_id uuid not null,
  payload_hash text not null check (payload_hash ~ '^[0-9a-f]{64}$'),
  lesson_id text not null references public.lessons(id),
  plan_date date not null,
  completed_at timestamptz not null,
  cards_total integer not null check (cards_total between 0 and 10000),
  cards_known integer not null check (cards_known between 0 and cards_total),
  contract_version text not null check (contract_version = '1.0'),
  client_instance_id text check (
    client_instance_id is null
    or client_instance_id ~ '^[A-Za-z0-9._:-]{1,128}$'
  ),
  created_at timestamptz not null default now(),
  check ((completed_at at time zone 'UTC')::date = plan_date),
  unique (user_id, event_id)
);

create index lesson_result_events_user_id_idx
  on public.lesson_result_events(user_id);

alter table public.lesson_result_events enable row level security;
revoke all on table public.lesson_result_events from public, anon, authenticated;
grant select, insert on table public.lesson_result_events to authenticated;

create policy "Users can read own lesson result events"
  on public.lesson_result_events for select to authenticated
  using ((select auth.uid()) = user_id);

create policy "Users can insert own lesson result events"
  on public.lesson_result_events for insert to authenticated
  with check ((select auth.uid()) = user_id);

-- Defense in depth: completions are never available to anonymous clients.
revoke all on table public.lesson_completions from anon;
revoke all on table public.lesson_completions from authenticated;
grant select, insert, update on table public.lesson_completions to authenticated;

create or replace function public.record_lesson_result(
  p_event_id uuid,
  p_lesson_id text,
  p_plan_date date,
  p_completed_at timestamptz,
  p_cards_total integer,
  p_cards_known integer,
  p_contract_version text,
  p_client_instance_id text,
  p_payload_hash text
) returns jsonb
language plpgsql
security invoker
set search_path = ''
as $$
declare
  v_user_id uuid := (select auth.uid());
  v_existing_hash text;
  v_inserted integer;
  v_status text;
begin
  if v_user_id is null then
    raise insufficient_privilege using message = 'Authentication required';
  end if;

  insert into public.lesson_result_events (
    user_id, event_id, payload_hash, lesson_id, plan_date, completed_at,
    cards_total, cards_known, contract_version, client_instance_id
  ) values (
    v_user_id, p_event_id, p_payload_hash, p_lesson_id, p_plan_date, p_completed_at,
    p_cards_total, p_cards_known, p_contract_version, p_client_instance_id
  ) on conflict (user_id, event_id) do nothing;
  get diagnostics v_inserted = row_count;

  if v_inserted = 0 then
    select payload_hash into v_existing_hash
      from public.lesson_result_events
      where user_id = v_user_id and event_id = p_event_id;
    if v_existing_hash is distinct from p_payload_hash then
      return jsonb_build_object('status', 'conflict');
    end if;
    v_status := 'duplicate';
  else
    v_status := 'created';
  end if;

  insert into public.lesson_completions (
    user_id, lesson_id, plan_date, cards_total, cards_known, completed_at
  ) values (
    v_user_id, p_lesson_id, p_plan_date, p_cards_total, p_cards_known, p_completed_at
  )
  on conflict (user_id, lesson_id, plan_date) do update set
    cards_total = greatest(public.lesson_completions.cards_total, excluded.cards_total),
    cards_known = greatest(public.lesson_completions.cards_known, excluded.cards_known),
    completed_at = least(public.lesson_completions.completed_at, excluded.completed_at);

  return jsonb_build_object('status', v_status);
end;
$$;

revoke all on function public.record_lesson_result(
  uuid, text, date, timestamptz, integer, integer, text, text, text
) from public, anon, authenticated;
grant execute on function public.record_lesson_result(
  uuid, text, date, timestamptz, integer, integer, text, text, text
) to authenticated;
