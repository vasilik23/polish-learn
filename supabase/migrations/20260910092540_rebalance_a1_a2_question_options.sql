with level_gate as (
  select c.level,
         greatest(
           count(*) filter (where q.correct = 0),
           count(*) filter (where q.correct = 1),
           count(*) filter (where q.correct = 2)
         ) - least(
           count(*) filter (where q.correct = 0),
           count(*) filter (where q.correct = 1),
           count(*) filter (where q.correct = 2)
         ) > 1
         or count(*) filter (where q.correct not in (0, 1, 2)) > 0 as should_rebalance
  from public.questions q
  join public.lessons l on l.id = q.lesson_id
  join public.topics t on t.id = l.topic_id
  join public.courses c on c.id = t.course_id
  where c.level in ('A1', 'A2') and q.is_active = true
  group by c.level
), targets as (
  select q.id, q.options, q.correct,
         mod(
           row_number() over (
             partition by c.level order by q.lesson_id, q.position, q.id
           ) - 1,
           least(jsonb_array_length(q.options), 3)
         )::integer as target
  from public.questions q
  join public.lessons l on l.id = q.lesson_id
  join public.topics t on t.id = l.topic_id
  join public.courses c on c.id = t.course_id
  join level_gate gate on gate.level = c.level
  where c.level in ('A1', 'A2')
    and q.is_active = true
    and jsonb_array_length(q.options) >= 2
    and q.correct < jsonb_array_length(q.options)
    and gate.should_rebalance
), reordered as (
  select target.id, target.target,
         jsonb_agg(
           element.value
           order by case
             when element.ordinality - 1 = target.correct then target.target
             when element.ordinality - 1 < target.correct then
               element.ordinality - 1
               + case when element.ordinality - 1 >= target.target then 1 else 0 end
             else
               element.ordinality - 2
               + case when element.ordinality - 2 >= target.target then 1 else 0 end
           end
         ) as options
  from targets target
  cross join lateral jsonb_array_elements(target.options)
    with ordinality as element(value, ordinality)
  group by target.id, target.target
)
update public.questions as q
set options = reordered.options,
    correct = reordered.target
from reordered
where q.id = reordered.id;
