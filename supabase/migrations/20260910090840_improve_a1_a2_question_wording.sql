update public.questions as q
set prompt = v.prompt,
    options = v.options
from (
  values
    ('food-grammar', 2, 'Kupuję dziś ___.', '["chleb", "chleba", "chlebem"]'::jsonb),
    ('weather-grammar', 0, 'Lekarz podkreśla konieczność: podczas upału ___ pić dużo wody.', '["trzeba", "można", "wolno"]'::jsonb),
    ('weather-grammar', 3, 'Prognoza nie jest pewna: jutro ___ padać, więc zabierz parasol.', '["może", "musi", "powinno"]'::jsonb),
    ('city-grammar', 4, 'Как вежливо спросить: «Как дойти до вокзала?»', '["Gdzie można kupić bilet?", "Jak dojść do dworca?", "O której odjeżdża pociąg?"]'::jsonb),
    ('city-quiz', 2, 'Как сказать «Пожалуйста, поверните направо»?', '["Proszę skręcić w prawo.", "Proszę skręcić w lewo.", "Proszę iść prosto."]'::jsonb),
    ('city-quiz', 7, 'Как спросить: «Как дойти до аптеки?»', '["Jak dojść do apteki?", "Czy apteka jest dziś otwarta?", "O której zamykają aptekę?"]'::jsonb),
    ('countries-grammar', 4, 'Как ответить «Я родом из Украины»?', '["Pochodzę z Ukrainy.", "Mieszkam teraz w Ukrainie.", "Jadę jutro do Ukrainy."]'::jsonb),
    ('daily-routine-grammar', 4, 'Как сказать «Я никогда не пью кофе вечером»?', '["Nigdy nie piję kawy wieczorem.", "Rzadko piję kawę wieczorem.", "Zawsze piję kawę wieczorem."]'::jsonb),
    ('family-grammar', 3, 'Как спросить: «Сколько лет твоей сестре?»', '["Gdzie mieszka twoja siostra?", "Ile lat ma twoja siostra?", "Jak ma na imię twoja siostra?"]'::jsonb),
    ('family-quiz', 7, 'Как спросить «Сколько лет твоему брату?»', '["Ile lat ma twój brat?", "Gdzie mieszka twój brat?", "Jak ma na imię twój brat?"]'::jsonb),
    ('final-quiz', 0, 'Как естественно сказать «Меня зовут Лена»?', '["Mam na imię Lena.", "Mam siostrę Lenę.", "Mieszkam z Leną."]'::jsonb),
    ('final-quiz', 6, 'Как спросить «Как дойти до вокзала?»', '["Jak dojść do dworca?", "Kiedy odjeżdża pociąg?", "Gdzie kupić bilet?"]'::jsonb),
    ('food-quiz', 7, 'Как заказать кофе без сахара?', '["Poproszę kawę bez cukru.", "Poproszę herbatę bez cukru.", "Poproszę kawę z cukrem."]'::jsonb),
    ('free-quiz', 6, 'Как спросить «Что ты любишь делать в выходные?»', '["Co lubisz robić w weekend?", "Gdzie pracujesz w weekend?", "Kiedy zaczyna się weekend?"]'::jsonb),
    ('home-quiz', 6, 'Как спросить «Где ключ?»', '["Gdzie jest klucz?", "Czy to jest klucz?", "Do czego jest ten klucz?"]'::jsonb),
    ('a2final-quiz', 5, 'Mam gorączkę. Co powinienem zrobić?', '["Powinieneś odpocząć i skontaktować się z lekarzem.", "Powinieneś intensywnie ćwiczyć przez cały dzień.", "Powinieneś zignorować gorączkę i iść do pracy."]'::jsonb),
    ('a2final-quiz', 8, 'Jak grzecznie poprosić urzędniczkę o wskazanie miejsca na podpis?', '["Czy może mi pani powiedzieć, gdzie mam podpisać?", "Proszę natychmiast podpisać ten dokument.", "Czy może mi pani powiedzieć, gdzie jest wyjście?"]'::jsonb),
    ('office-grammar', 0, 'Как вежливо сказать «Я хотел бы подать заявление»?', '["Chciałbym złożyć wniosek.", "Chciałbym odebrać dokument.", "Muszę wypełnić formularz."]'::jsonb),
    ('office-grammar', 2, 'Как прочитать дату 12.03.2026?', '["dwunasty marca dwa tysiące dwudziestego szóstego roku", "dwudziesty pierwszy marca dwa tysiące dwudziestego szóstego roku", "dwunasty maja dwa tysiące dwudziestego szóstego roku"]'::jsonb),
    ('office-grammar', 3, 'Как сказать «Пожалуйста, подпишите форму здесь»?', '["Proszę podpisać formularz tutaj.", "Proszę wypełnić formularz tutaj.", "Proszę podpisać formularz na dole."]'::jsonb),
    ('housing-quiz', 3, 'Что нужно сделать, если в квартире сломалось отопление?', '["Zgłosić usterkę administracji.", "Podpisać nową umowę najmu.", "Zapłacić czynsz za następny miesiąc."]'::jsonb),
    ('med-quiz', 3, 'Как сообщить врачу об аллергии на пенициллин?', '["Mam uczulenie na penicylinę.", "Biorę penicylinę dwa razy dziennie.", "Potrzebuję recepty na penicylinę."]'::jsonb),
    ('med-quiz', 5, 'Как сказать «Если состояние ухудшится…»?', '["Jeśli stan się pogorszy…", "Jeśli stan się poprawi…", "Jeśli stan się nie zmieni…"]'::jsonb)
) as v(lesson_id, position, prompt, options)
where q.lesson_id = v.lesson_id
  and q.position = v.position;
