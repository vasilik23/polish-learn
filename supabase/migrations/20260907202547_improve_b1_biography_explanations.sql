update public.questions as q
set explanation = v.explanation
from (
  values
    ('bio-grammar', 1, 'Forma ukończyła nazywa zakończoną czynność z wyraźnym rezultatem: Marta otrzymała certyfikat.'),
    ('bio-quiz', 0, 'Czasownik dorastać opisuje stopniowe dojrzewanie i przechodzenie od dzieciństwa do dorosłości.'),
    ('bio-quiz', 3, 'Wyrażenie osiągnął cel oznacza uzyskanie zamierzonego rezultatu po roku pracy nad projektem.'),
    ('bio-quiz', 4, 'Niedokonana forma jeździłem opisuje czynność wielokrotną, ponieważ podróże powtarzały się w przeszłości.'),
    ('bio-quiz', 6, 'Słowo początkowo wprowadza pierwszy etap historii i zapowiada późniejszą zmianę sytuacji.'),
    ('bio-quiz', 8, 'Markery najpierw, następnie, z czasem i w końcu porządkują kolejne etapy biografii.'),
    ('bio-quiz', 9, 'Forma ukończyłem wskazuje zakończony etap edukacji, a data precyzuje moment jego zamknięcia.'),
    ('bio-reading-check', 0, 'Joanna dorastała w Białymstoku; ta informacja pojawia się na początku jej biografii.'),
    ('bio-reading-check', 1, 'Joanna studiowała architekturę w Warszawie, zanim zaczęła rozwijać własną drogę zawodową.'),
    ('bio-reading-check', 4, 'Joanna postanowiła projektować przestrzenie publiczne, więc ukierunkowała pracę na potrzeby mieszkańców.')
) as v(lesson_id, position, explanation)
where q.lesson_id = v.lesson_id
  and q.position = v.position;
