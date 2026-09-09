update public.questions as q
set explanation = v.explanation
from (
  values
    ('b2view-grammar', 1, 'Marker niemniej jednak wprowadza kontrast: wysoki koszt nie wyklucza przyszłych oszczędności.'),
    ('b2view-grammar', 3, 'Stałe wyrażenie odnieść się do wymaga przyimka do oraz rzeczownika w dopełniaczu.'),
    ('b2view-quiz', 0, 'Stanowisko w dyskusji oznacza jasno określoną opinię uczestnika wobec omawianej kwestii.'),
    ('b2view-quiz', 1, 'Uzasadnienie wyjaśnia, dlaczego teza jest przekonująca, łącząc ją z argumentami lub danymi.'),
    ('b2view-quiz', 5, 'Marker z drugiej strony wprowadza odmienną perspektywę, która kontrastuje z wcześniejszym argumentem.'),
    ('b2view-reading-check', 0, 'Debata dotyczyła ograniczenia ruchu samochodowego w centrum oraz skutków takiej zmiany.'),
    ('b2view-reading-check', 1, 'Lena poparła pilotaż warunkowo, domagając się zabezpieczeń i późniejszej oceny jego skutków.'),
    ('b2view-reading-check', 3, 'Kontrargument Leny opierał się na wynikach porównywalnego pilotażu przeprowadzonego w innym mieście.'),
    ('b2view-reading-check', 4, 'Uczestnicy uwzględnili wyjątki oraz ocenę skutków po pół roku działania rozwiązania.'),
    ('b2view-reading-check', 5, 'Tekst pokazuje, że rzeczowa debata może doprecyzować i ulepszyć początkową propozycję.')
) as v(lesson_id, position, explanation)
where q.lesson_id = v.lesson_id
  and q.position = v.position;
