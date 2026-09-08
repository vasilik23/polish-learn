update public.questions as q
set explanation = v.explanation
from (
  values
    ('b1trip-grammar', 0, 'Czasownik dojechać podkreśla dotarcie do celu, tutaj do Krakowa przed określoną godziną.'),
    ('b1trip-grammar', 2, 'Zwrot przejechać przez opisuje ruch przez miejsce bez zatrzymywania się w nim.'),
    ('b1trip-quiz', 0, 'Przesiadka oznacza zmianę pociągu lub innego środka transportu podczas jednej podróży.'),
    ('b1trip-quiz', 1, 'Odwołany lot nie odbędzie się zgodnie z planem, dlatego trzeba znaleźć inne połączenie.'),
    ('b1trip-quiz', 4, 'Czasownik dojechać wskazuje na osiągnięcie celu podróży, a nie sam ruch.'),
    ('b1trip-quiz', 9, 'Stałe wyrażenie zrobić wrażenie oznacza wywołać u kogoś określoną reakcję lub ocenę.'),
    ('b1trip-reading-check', 0, 'Marta i Paweł jechali do Pragi, co tekst wskazuje jako cel ich podróży.'),
    ('b1trip-reading-check', 1, 'Pierwszy problem pojawił się w Katowicach, gdzie podróżni dowiedzieli się o utrudnieniach.'),
    ('b1trip-reading-check', 3, 'Pracownica znalazła połączenie przez inną miejscowość, dzięki czemu podróż mogła trwać dalej.'),
    ('b1trip-reading-check', 4, 'Podczas przerwy podróżni zwiedzili okolicę, zamiast cały czas czekać na peronie.')
) as v(lesson_id, position, explanation)
where q.lesson_id = v.lesson_id
  and q.position = v.position;
