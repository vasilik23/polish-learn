update public.questions as q
set explanation = v.explanation
from (
  values
    ('b1rel-quiz', 1, 'Wyrażenie liczyć na kogoś oznacza ufać, że dana osoba udzieli potrzebnego wsparcia.'),
    ('b1rel-quiz', 3, 'Po stopniu wyższym bardziej otwarty używamy przyimka od oraz rzeczownika w dopełniaczu.'),
    ('b1rel-quiz', 4, 'Czasownik opowiedzieć łączy się z celownikiem, dlatego poprawną formą zaimka jest której.'),
    ('b1rel-quiz', 5, 'Konstrukcja tak samo jak porównuje równy stopień cechy u nas i naszych rodziców.'),
    ('b1rel-quiz', 6, 'Spokojna i szczera rozmowa pozwala obu stronom wyjaśnić potrzeby oraz zakończyć nieporozumienie.'),
    ('b1rel-quiz', 8, 'Czasownik dogadać się oznacza osiągnąć wzajemne porozumienie mimo wcześniejszej różnicy zdań.'),
    ('b1rel-reading-check', 0, 'Ola i Michał pokłócili się, ponieważ mieli różne oczekiwania dotyczące wspólnego wyjazdu.'),
    ('b1rel-reading-check', 2, 'Michał zaproponował, aby każda osoba spokojnie opisała własne potrzeby dotyczące wyjazdu.'),
    ('b1rel-reading-check', 3, 'Ola potrzebowała spokojnego odpoczynku bez pośpiechu, zamiast codziennych długich wędrówek.'),
    ('b1rel-reading-check', 4, 'Kompromis połączył potrzeby obojga: wspólną aktywność oraz czas na spokojny odpoczynek.')
) as v(lesson_id, position, explanation)
where q.lesson_id = v.lesson_id
  and q.position = v.position;
