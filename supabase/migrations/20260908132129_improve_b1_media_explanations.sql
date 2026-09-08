update public.questions as q
set explanation = v.explanation
from (
  values
    ('b1media-grammar', 2, 'W mowie zależnej treść relacji po czasowniku relacjonował wprowadzamy spójnikiem że.'),
    ('b1media-grammar', 3, 'Słowo następnie porządkuje streszczenie, łącząc przedstawienie tematu z kolejną główną myślą.'),
    ('b1media-quiz', 1, 'Udostępniać wiadomość znaczy przekazywać ją dalej, czego nie warto robić bez sprawdzenia źródła.'),
    ('b1media-quiz', 2, 'Czasownik twierdzić wprowadza zdecydowane stanowisko autora, a nie neutralny wynik analizy.'),
    ('b1media-quiz', 4, 'Dobre streszczenie najpierw wskazuje temat tekstu, a następnie jasno podaje jego główną myśl.'),
    ('b1media-quiz', 5, 'Po czasowniku zaprzeczył treść odrzucanego twierdzenia wprowadzamy w tym zdaniu spójnikiem że.'),
    ('b1media-quiz', 8, 'Czasownik relacjonować oznacza przedstawiać przebieg wydarzenia w uporządkowanym porządku chronologicznym.'),
    ('b1media-reading-check', 1, 'Nagłówek wzbudził wątpliwości Marty, ponieważ nie zawierał autora ani daty opisywanej decyzji.'),
    ('b1media-reading-check', 2, 'Marta sprawdziła wiadomość, porównując wpis z oficjalną stroną oraz wiarygodnym lokalnym portalem.'),
    ('b1media-reading-check', 3, 'Biblioteka planowała jedynie krótki remont jednego piętra, a nie całkowite zamknięcie placówki.')
) as v(lesson_id, position, explanation)
where q.lesson_id = v.lesson_id
  and q.position = v.position;
