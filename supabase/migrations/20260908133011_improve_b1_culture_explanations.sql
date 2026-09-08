update public.questions as q
set explanation = v.explanation
from (
  values
    ('b1culture-grammar', 1, 'Forma której wyraża przynależność: nagrodzony film należy do dorobku wspomnianej reżyserki.'),
    ('b1culture-quiz', 0, 'Ekranizacja to filmowa wersja utworu literackiego, która może zmieniać elementy oryginału.'),
    ('b1culture-quiz', 1, 'Fabuła oznacza uporządkowany ciąg wydarzeń przedstawionych w książce, filmie lub spektaklu.'),
    ('b1culture-quiz', 2, 'Zaimek której wyraża przynależność: przeczytana powieść jest dziełem wspomnianej autorki.'),
    ('b1culture-quiz', 4, 'Ocena przekonująca i naturalna opisuje wiarygodną grę aktora, a nie element fabuły.'),
    ('b1culture-quiz', 5, 'Scenografia obejmuje wizualną oprawę sceny, która pomaga budować nastrój przedstawienia.'),
    ('b1culture-quiz', 8, 'Zaimek w którym wskazuje miejsce wydarzenia: wystawa odbywa się w opisanym muzeum.'),
    ('b1culture-reading-check', 2, 'Ola pozytywnie oceniła przekonującą grę głównej aktorki, która wiarygodnie stworzyła postać.'),
    ('b1culture-reading-check', 3, 'Film połączył kilka postaci i skrócił wybrane wątki, dlatego różnił się od powieści.'),
    ('b1culture-reading-check', 4, 'Po seansie publiczność spotkała się z reżyserką i mogła porozmawiać o ekranizacji.')
) as v(lesson_id, position, explanation)
where q.lesson_id = v.lesson_id
  and q.position = v.position;
