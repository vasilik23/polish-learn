update public.questions as q
set explanation = v.explanation
from (
  values
    ('b1health-grammar', 0, 'Jednorazowa rada z oczekiwanym skutkiem wymaga formy dokonanej odłożyć, czyli usunąć telefon.'),
    ('b1health-quiz', 0, 'Utrzymać nawyk oznacza regularnie kontynuować wybrane działanie mimo pojawiających się trudności.'),
    ('b1health-quiz', 1, 'Czasownik wysypiać się oznacza spać wystarczająco długo, aby odzyskać energię i koncentrację.'),
    ('b1health-quiz', 4, 'Dokonana forma wykonałem podkreśla, że cały zaplanowany zestaw ćwiczeń został zakończony.'),
    ('b1health-quiz', 6, 'Jedna niewielka zmiana naraz jest bezpieczniejsza i łatwiejsza do trwałego utrzymania.'),
    ('b1health-reading-check', 0, 'Kuba chciał zmienić tryb życia, ponieważ często czuł zmęczenie i źle spał.'),
    ('b1health-reading-check', 2, 'Fizjoterapeutka zaleciła jeden mały nawyk oraz uważne obserwowanie reakcji własnego organizmu.'),
    ('b1health-reading-check', 3, 'Kuba zaczął od krótkiego spaceru po pracy, wybierając realistyczny i łagodny pierwszy krok.'),
    ('b1health-reading-check', 4, 'Po kilku tygodniach regularnych spacerów Kuba lepiej spał i miał więcej energii.'),
    ('b1health-reading-check', 5, 'Trwała zmiana powstaje stopniowo i wymaga obserwacji samopoczucia oraz odpowiedniej regeneracji.')
) as v(lesson_id, position, explanation)
where q.lesson_id = v.lesson_id
  and q.position = v.position;
