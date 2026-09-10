update public.questions as q
set options = v.options, correct = 0
from (
  values
    ('b2view-grammar', 4, '["Z jednej strony propozycja oszczędza czas, z drugiej strony ogranicza wybór.", "Z jednej strony propozycja oszczędza czas, z drugiej strony zwiększa wybór.", "Propozycja oszczędza czas, dlatego nie ogranicza wyboru."]'::jsonb),
    ('b2news-grammar', 4, '["Według urzędu most zostanie otwarty w poniedziałek.", "Według urzędu most został otwarty w poniedziałek.", "Według urzędu most będzie zamknięty w poniedziałek."]'::jsonb),
    ('b2prof-grammar', 4, '["W nawiązaniu do naszego spotkania przesyłam uzgodnione podsumowanie.", "W nawiązaniu do naszego spotkania przesłałem wstępne podsumowanie.", "Przed naszym spotkaniem przesyłam uzgodniony porządek obrad."]'::jsonb),
    ('b2tech-grammar', 4, '["Algorytm to zbiór reguł, który jest wykorzystywany do przetwarzania danych.", "Algorytm to zbiór danych, który jest wykorzystywany do ustalania reguł.", "Algorytm to pojedyncza reguła, która nie służy do przetwarzania danych."]'::jsonb),
    ('b2economy-grammar', 4, '["Popyt wzrósł o 8%, ale podaż prawie się nie zmieniła.", "Podaż wzrosła o 8%, ale popyt prawie się nie zmienił.", "Popyt wzrósł o 8%, dlatego podaż wyraźnie się zwiększyła."]'::jsonb),
    ('b2law-grammar', 4, '["Proszę o ponowne rozpatrzenie sprawy na podstawie załączonych dokumentów.", "Proszę o pierwsze rozpatrzenie sprawy bez załączonych dokumentów.", "Proszę o ponowne odrzucenie sprawy na podstawie ustnego wyjaśnienia."]'::jsonb),
    ('b2psych-grammar', 4, '["Prawdopodobnie wycofała się, ponieważ obawiała się kolejnego konfliktu.", "Z pewnością wycofała się, chociaż nie obawiała się kolejnego konfliktu.", "Prawdopodobnie zaangażowała się, ponieważ oczekiwała kolejnego konfliktu."]'::jsonb),
    ('b2lit-grammar', 4, '["Ten obraz można odczytać jako symbol utraconej bliskości.", "Ten obraz należy odczytać dosłownie jako opis odzyskanej bliskości.", "Ten obraz można odczytać jako symbol przyszłego sukcesu."]'::jsonb),
    ('b2discussion-grammar', 4, '["Jeśli dobrze rozumiem, proponuje pan zmienić porządek dyskusji.", "Jeśli dobrze rozumiem, proponuje pan zakończyć dyskusję.", "Ponieważ dobrze rozumiem, zmienił pan temat dyskusji."]'::jsonb),
    ('b2intercultural-grammar', 4, '["W moim doświadczeniu lepiej doprecyzować normę, niż robić założenia.", "W moim doświadczeniu lepiej przyjąć założenie, niż pytać o normę.", "Bez względu na moje doświadczenie nie warto doprecyzowywać normy."]'::jsonb),
    ('b2academic-grammar', 4, '["Oba źródła wskazują na korzyść, ale stosują różne metody.", "Oba źródła wskazują na zagrożenie i stosują tę samą metodę.", "Tylko jedno źródło wskazuje na korzyść, choć metody są podobne."]'::jsonb),
    ('b2final-grammar', 4, '["Chociaż wynik potwierdził tezę, nie można ignorować ograniczenia próby.", "Ponieważ wynik podważył tezę, można pominąć ograniczenie próby.", "Wynik potwierdził tezę, dlatego ograniczenie próby nie ma znaczenia."]'::jsonb)
) as v(lesson_id, position, options),
(
  select count(*) filter (where candidate.correct = 0) > 250 as should_rebalance
  from public.questions candidate
  join public.lessons lesson on lesson.id = candidate.lesson_id
  join public.topics topic on topic.id = lesson.topic_id
  where topic.course_id = 'b2-advanced' and candidate.is_active = true
) as gate
where q.lesson_id = v.lesson_id
  and q.position = v.position
  and gate.should_rebalance;

with rebalance_gate as (
  select count(*) filter (where q.correct = 0) > 250 as should_rebalance
  from public.questions q
  join public.lessons l on l.id = q.lesson_id
  join public.topics t on t.id = l.topic_id
  where t.course_id = 'b2-advanced' and q.is_active = true
), targets as (
  select q.id, q.options, q.correct,
         jsonb_array_length(q.options) as option_count,
         mod(
           row_number() over (order by q.lesson_id, q.position, q.id) - 1,
           jsonb_array_length(q.options)
         )::integer as target
  from public.questions q
  join public.lessons l on l.id = q.lesson_id
  join public.topics t on t.id = l.topic_id
  cross join rebalance_gate gate
  where t.course_id = 'b2-advanced'
    and q.is_active = true
    and jsonb_array_length(q.options) >= 2
    and gate.should_rebalance
), reordered as (
  select target.id, target.target,
         jsonb_agg(
           element.value
           order by case
             when element.ordinality - 1 = target.correct then target.target
             when element.ordinality - 1 < target.correct then
               element.ordinality - 1 + case when element.ordinality - 1 >= target.target then 1 else 0 end
             else
               element.ordinality - 2 + case when element.ordinality - 2 >= target.target then 1 else 0 end
           end
         ) as options
  from targets target
  cross join lateral jsonb_array_elements(target.options) with ordinality as element(value, ordinality)
  group by target.id, target.target
)
update public.questions as q
set options = reordered.options,
    correct = reordered.target
from reordered
where q.id = reordered.id;
