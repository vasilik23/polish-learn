update public.questions as question
set explanation = updates.explanation
from (
  values
    ('b2news-grammar', 3, 'Przymiotnik „przełomowa” wyraża ocenę autora, której nie da się sprawdzić jak faktu.'),
    ('b2news-grammar', 5, 'Spójnik „że” wprowadza treść relacji świadka i wymaga zmiany mowy niezależnej na zależną.'),
    ('b2news-quiz', 0, 'Sprostowanie oficjalnie poprawia wcześniej opublikowaną informację, która okazała się nieprawdziwa lub nieścisła.'),
    ('b2news-quiz', 1, 'Zwrot „jak podaje urząd” jednoznacznie przypisuje wiadomość konkretnemu, możliwemu do sprawdzenia źródłu.'),
    ('b2news-quiz', 2, 'Określenie „katastrofalny” zawiera silną ocenę skutków, zamiast neutralnie opisywać sprawdzalny fakt.'),
    ('b2news-quiz', 3, 'Czasownik „wynikać” łączy się z przyimkiem „z”, dlatego poprawna forma brzmi „wynika z komunikatu”.'),
    ('b2news-quiz', 4, 'Partykuła „podobno” sygnalizuje, że informacja nie została potwierdzona i autor zachowuje wobec niej dystans.'),
    ('b2news-quiz', 5, 'Czasownik „zaprzeczyć” wymaga celownika, dlatego ministerstwo zaprzecza właśnie „doniesieniom”, a nie „doniesienia”.'),
    ('b2news-quiz', 6, 'Godzina rozpoczęcia konferencji jest konkretną daną, którą można niezależnie potwierdzić w harmonogramie.'),
    ('b2news-quiz', 7, 'Spójnik „że” wprowadza mowę zależną, a „jutro” zmienia się na „następnego dnia”.'),
    ('b2news-quiz', 8, 'Zestawienie niezależnych relacji ujawnia ich wspólne fakty oraz oddziela je od ocen i przypuszczeń.'),
    ('b2news-quiz', 9, 'Nagłówek podaje mierzalny wynik bez emocjonalnych epitetów, dlatego pozostaje najbardziej bezstronny.'),
    ('b2news-reading-check', 0, 'Każda z trzech publikacji opisywała tę samą awarię systemu sprzedaży biletów.'),
    ('b2news-reading-check', 1, 'Operator potwierdził czas rozpoczęcia awarii oraz liczbę niedostępnych punktów sprzedaży.'),
    ('b2news-reading-check', 2, 'Operator nie wskazał przyczyny awarii, ponieważ miała zostać ustalona dopiero po analizie.'),
    ('b2news-reading-check', 3, 'Po aktualizacji redakcja zastąpiła sensacyjne określenia ostrożniejszym, bardziej neutralnym językiem.'),
    ('b2news-reading-check', 4, 'Porównanie źródeł potwierdziło samą awarię, lecz nie sensacyjne hipotezy dotyczące jej przyczyn.'),
    ('b2news-reading-check', 5, 'Grupa postanowiła wyraźnie oznaczać fakty, oceny i przypuszczenia, aby kontrolować stopień pewności.')
) as updates(lesson_id, position, explanation)
where question.lesson_id = updates.lesson_id
  and question.position = updates.position;
