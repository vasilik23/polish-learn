update public.questions as q
set explanation = v.explanation
from (
  values
    ('b1edu-grammar', 0, 'Spójnik ponieważ wprowadza rzeczywistą przyczynę regularnej nauki, czyli zamiar zdania egzaminu.'),
    ('b1edu-grammar', 2, 'W mowie zależnej twierdzenie po czasowniku powiedział wprowadzamy spójnikiem że, bez cudzysłowu.'),
    ('b1edu-quiz', 2, 'Stałe wyrażenie robić postępy oznacza stopniowo rozwijać umiejętności i osiągać lepsze wyniki.'),
    ('b1edu-quiz', 3, 'Spójnik chociaż wprowadza ustępstwo: brak zgody nie wyklucza zrozumienia komentarza nauczyciela.'),
    ('b1edu-quiz', 4, 'Po czasowniku powiedziała przekazujemy twierdzenie w mowie zależnej za pomocą spójnika że.'),
    ('b1edu-quiz', 5, 'Spójnik czy rozpoczyna w mowie zależnej pytanie, na które można odpowiedzieć tak albo nie.'),
    ('b1edu-quiz', 6, 'Konkretna informacja zwrotna wskazuje dokładny błąd i podpowiada, co należy poprawić.'),
    ('b1edu-quiz', 8, 'Spójnik ponieważ podaje przyczynę: zajęcia praktyczne pozwalają wykorzystać wiedzę teoretyczną w działaniu.'),
    ('b1edu-reading-check', 0, 'Lena zapisała się na kurs, aby pewniej prowadzić spotkania zawodowe po polsku.'),
    ('b1edu-reading-check', 5, 'Lena uznała, że postęp wynika z regularnej, świadomej praktyki, a nie wyłącznie z talentu.')
) as v(lesson_id, position, explanation)
where q.lesson_id = v.lesson_id
  and q.position = v.position;
