update public.questions as q
set explanation = v.explanation
from (
  values
    ('b1work-quiz', 0, 'Stanowisko oznacza określoną funkcję lub miejsce pracownika w strukturze firmy albo instytucji.'),
    ('b1work-quiz', 1, 'Wyrażenie należeć do łączy się z dopełniaczem, dlatego poprawna forma brzmi do obowiązków.'),
    ('b1work-quiz', 2, 'Proces rekrutacji zwykle rozpoczyna kandydat, wysyłając CV z opisem doświadczenia i umiejętności.'),
    ('b1work-quiz', 7, 'Szkolenie wspiera rozwój zawodowy, ponieważ pozwala zdobywać nowe kompetencje potrzebne w pracy.'),
    ('b1work-quiz', 8, 'Forma mógłby Pan tworzy uprzejmą oficjalną prośbę odpowiednią w kontakcie zawodowym.'),
    ('b1work-quiz', 9, 'Otrzymać awans oznacza przejść na wyższe stanowisko dzięki dobrym wynikom zawodowym.'),
    ('b1work-reading-check', 0, 'Lena szukała pracy dającej większą odpowiedzialność oraz możliwość dalszego rozwoju zawodowego.'),
    ('b1work-reading-check', 1, 'Przed wysłaniem CV Lena opisała konkretne osiągnięcia i ukończyła dodatkowy kurs.'),
    ('b1work-reading-check', 2, 'Kierownik poprosił Lenę o przykład reakcji na opóźnienie projektu, aby ocenić jej kompetencje.'),
    ('b1work-reading-check', 3, 'Lena spokojnie przedstawiła plan działania i rozmowę z klientem, pokazując własną inicjatywę.')
) as v(lesson_id, position, explanation)
where q.lesson_id = v.lesson_id
  and q.position = v.position;
