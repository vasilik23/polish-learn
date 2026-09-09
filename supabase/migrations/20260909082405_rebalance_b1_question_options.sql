update public.questions as q
set options = v.options, correct = 0
from (
  values
    ('bio-grammar', 0, '["pracowała", "pracuje", "będzie pracować"]'::jsonb),
    ('b1health-grammar', 0, '["odłożyć", "odkładam", "odłożony"]'::jsonb),
    ('b1health-quiz', 2, '["radzić sobie ze stresem", "radzić stresowi", "radzić o stresie"]'::jsonb),
    ('b1media-grammar', 0, '["twierdzi", "wynika", "streszcza"]'::jsonb),
    ('b1media-quiz', 7, '["streścić publikację", "skomentować publikację", "udostępnić publikację"]'::jsonb),
    ('b1soc-quiz', 6, '["korzyści", "korzyść", "korzystni"]'::jsonb),
    ('b1region-quiz', 6, '["zachować tradycję", "opisać krajobraz", "poznać gwarę"]'::jsonb),
    ('b1final-quiz', 2, '["Z poważaniem", "Do zobaczenia", "Trzymaj się"]'::jsonb),
    ('b1final-quiz', 6, '["konkretny przykład", "powitanie", "zmiana tematu"]'::jsonb)
) as v(lesson_id, position, options),
(
  select count(*) filter (where candidate.correct = 0) > 250 as should_rebalance
  from public.questions candidate
  join public.lessons lesson on lesson.id = candidate.lesson_id
  join public.topics topic on topic.id = lesson.topic_id
  where topic.course_id = 'b1-independent' and candidate.is_active = true
) as gate
where q.lesson_id = v.lesson_id
  and q.position = v.position
  and gate.should_rebalance;

with rebalance_gate as (
  select count(*) filter (where q.correct = 0) > 250 as should_rebalance
  from public.questions q
  join public.lessons l on l.id = q.lesson_id
  join public.topics t on t.id = l.topic_id
  where t.course_id = 'b1-independent' and q.is_active = true
), targets as (
  select q.id, q.options, q.correct,
         jsonb_array_length(q.options) as option_count,
         1 + mod(
           q.position + (
             select sum(ascii(substr(q.lesson_id, char_index, 1)))::integer
             from generate_series(1, length(q.lesson_id)) as positions(char_index)
           ),
           jsonb_array_length(q.options) - 1
         ) as shift
  from public.questions q
  join public.lessons l on l.id = q.lesson_id
  join public.topics t on t.id = l.topic_id
  cross join rebalance_gate gate
  where t.course_id = 'b1-independent'
    and q.is_active = true
    and jsonb_array_length(q.options) >= 2
    and gate.should_rebalance
), rotated as (
  select target.id,
         target.correct,
         target.option_count,
         target.shift,
         jsonb_agg(element.value order by mod(element.ordinality - 1 + target.shift, target.option_count)) as options
  from targets target
  cross join lateral jsonb_array_elements(target.options) with ordinality as element(value, ordinality)
  group by target.id, target.correct, target.option_count, target.shift
)
update public.questions as q
set options = rotated.options,
    correct = mod(rotated.correct + rotated.shift, rotated.option_count)
from rotated
where q.id = rotated.id;
