-- First original A1 content block: introductions.
-- Public learning content remains read-only through existing RLS policies.

alter table public.lessons
  add column source_metadata jsonb not null default '{}'::jsonb
  check (jsonb_typeof(source_metadata) = 'object');

alter table public.flashcards
  add column source_metadata jsonb not null default '{}'::jsonb
  check (jsonb_typeof(source_metadata) = 'object');

alter table public.reading_texts
  add column source_metadata jsonb not null default '{}'::jsonb
  check (jsonb_typeof(source_metadata) = 'object');

update public.topics
set position = 1
where course_id = 'a1-foundations' and position = 0;

insert into public.topics
  (id, course_id, title, description, emoji, position, is_active)
values
  (
    'introductions',
    'a1-foundations',
    'Знакомство',
    'Приветствия, представление и первые вопросы о человеке',
    '👋',
    0,
    true
  )
on conflict (id) do update set
  title = excluded.title,
  description = excluded.description,
  emoji = excluded.emoji,
  position = excluded.position,
  is_active = excluded.is_active;

update public.lessons as lesson
set
  title = content.title,
  plan_title = content.plan_title,
  subtitle = content.subtitle,
  description = content.description,
  minutes = content.minutes,
  emoji = content.emoji,
  topic_id = 'introductions',
  source_metadata = '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'::jsonb
from (
  values
    ('words', 'Pierwsze słowa', 'Знакомство: слова', '8 фраз · A1', 'Поздоровайся и представься', 6::smallint, '👋'),
    ('grammar', 'Czasownik być', 'Грамматика', 'Глагол być', 'Научись говорить, кто ты и откуда', 8::smallint, '✏️'),
    ('review', 'Przedstaw się', 'Фразы знакомства', '7 карточек · A1', 'Закрепи вопросы и вежливые обращения', 6::smallint, '🔄'),
    ('quiz', 'Quiz: poznajmy się', 'Мини-тест', '8 вопросов · A1', 'Проверь тему «Знакомство»', 5::smallint, '🎯')
) as content(id, title, plan_title, subtitle, description, minutes, emoji)
where lesson.id = content.id;

update public.lessons
set
  theory_title = 'Być — быть',
  theory_sections = '[
    ["Формы настоящего времени","ja jestem · ty jesteś · on/ona/ono jest · my jesteśmy · wy jesteście · oni/one są"],
    ["Представляемся","Jestem Anna. — Я Анна. Jestem z Polski. — Я из Польши."],
    ["Вежливое обращение","С pan и pani используется третье лицо: Czy pan jest z Polski? Czy pani jest nauczycielką?"]
  ]'::jsonb
where id = 'grammar';

insert into public.flashcards
  (id, polish, translation, example, position, is_active, source_metadata)
values
  ('czesc', 'cześć', 'привет / пока', 'Cześć, mam na imię Anna.', 0, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
  ('dzien-dobry', 'dzień dobry', 'добрый день', 'Dzień dobry, pani Mario!', 1, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
  ('do-widzenia', 'do widzenia', 'до свидания', 'Do widzenia, do jutra!', 2, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
  ('mam-na-imie', 'mam na imię', 'меня зовут', 'Mam na imię Oleg.', 3, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
  ('jak-masz-na-imie', 'jak masz na imię?', 'как тебя зовут?', 'Cześć! Jak masz na imię?', 4, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
  ('milo-mi', 'miło mi', 'приятно познакомиться', 'Jestem Ewa. Miło mi!', 5, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
  ('jak-sie-masz', 'jak się masz?', 'как ты?', 'Cześć, Piotr! Jak się masz?', 6, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
  ('dobrze', 'dobrze', 'хорошо', 'Dobrze, dziękuję.', 7, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
  ('jestem', 'jestem', 'я являюсь / я есть', 'Jestem Anna.', 8, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
  ('jestes', 'jesteś', 'ты являешься / ты есть', 'Jesteś z Polski?', 9, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
  ('pan', 'pan', 'господин / Вы', 'Czy pan jest nauczycielem?', 10, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
  ('pani', 'pani', 'госпожа / Вы', 'Czy pani jest z Warszawy?', 11, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
  ('skad-jestes', 'skąd jesteś?', 'откуда ты?', 'Skąd jesteś? Jestem z Ukrainy.', 12, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
  ('z-polski', 'z Polski', 'из Польши', 'Marek jest z Polski.', 13, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
  ('tez', 'też', 'тоже', 'Ja też jestem na kursie.', 14, true, '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}')
on conflict (id) do update set
  polish = excluded.polish,
  translation = excluded.translation,
  example = excluded.example,
  position = excluded.position,
  is_active = excluded.is_active,
  source_metadata = excluded.source_metadata;

delete from public.lesson_flashcards
where lesson_id in ('words', 'review');

insert into public.lesson_flashcards (lesson_id, flashcard_id, position)
values
  ('words', 'czesc', 0),
  ('words', 'dzien-dobry', 1),
  ('words', 'do-widzenia', 2),
  ('words', 'mam-na-imie', 3),
  ('words', 'jak-masz-na-imie', 4),
  ('words', 'milo-mi', 5),
  ('words', 'jak-sie-masz', 6),
  ('words', 'dobrze', 7),
  ('review', 'jestem', 0),
  ('review', 'jestes', 1),
  ('review', 'pan', 2),
  ('review', 'pani', 3),
  ('review', 'skad-jestes', 4),
  ('review', 'z-polski', 5),
  ('review', 'tez', 6);

delete from public.questions
where lesson_id in ('grammar', 'quiz');

insert into public.questions
  (lesson_id, prompt, options, correct, explanation, position)
values
  ('grammar', 'Как сказать «Я Анна»?', '["Jesteś Anna.","Jestem Anna.","Jest Anna."]', 1, 'Для «я» используется форма jestem: Jestem Anna.', 0),
  ('grammar', 'Выберите форму для «ты»: Ty ___ z Polski.', '["jestem","jesteś","jest"]', 1, 'С местоимением ty используется jesteś.', 1),
  ('grammar', 'Как вежливо спросить женщину: «Вы из Варшавы?»', '["Czy pani jest z Warszawy?","Czy jesteś pan z Warszawy?","Jestem z Warszawy?"]', 0, 'Pani — вежливое обращение к женщине; используется форма jest.', 2),
  ('grammar', 'My ___ na kursie. Вставьте форму być.', '["są","jesteście","jesteśmy"]', 2, 'My jesteśmy — «мы являемся / мы находимся».', 3),
  ('grammar', 'Oni ___ z Polski. Вставьте форму być.', '["są","jest","jesteś"]', 0, 'Oni są — «они являются».', 4),
  ('quiz', 'Как неформально поздороваться?', '["Do widzenia","Cześć","Dziękuję","Przepraszam"]', 1, 'Cześć — неформальное приветствие; оно также может означать «пока».', 0),
  ('quiz', 'Что значит «Mam na imię Lena»?', '["Мне нравится Лена","Меня зовут Лена","Я вижу Лену","Это Лена"]', 1, 'Mam na imię… — стандартная конструкция «Меня зовут…».', 1),
  ('quiz', 'Как спросить «Как тебя зовут?»', '["Skąd jesteś?","Jak się masz?","Jak masz na imię?","Kim jesteś?"]', 2, 'Jak masz na imię? — «Как тебя зовут?»', 2),
  ('quiz', 'Выберите ответ на «Jak się masz?»', '["Dobrze, dziękuję.","Mam na imię.","Do widzenia?","Z Polski."]', 0, 'Dobrze, dziękuję — естественный короткий ответ: «Хорошо, спасибо».', 3),
  ('quiz', 'Как сказать «Я из Украины»?', '["Jesteś z Ukrainy.","Jest z Ukrainy.","Jestem z Ukrainy.","Są z Ukrainy."]', 2, 'Для «я» нужна форма jestem: Jestem z Ukrainy.', 4),
  ('quiz', 'Что означает «Miło mi» при знакомстве?', '["Мне холодно","Очень хорошо","Приятно познакомиться","До завтра"]', 2, 'Miło mi — краткое «Приятно познакомиться».', 5),
  ('quiz', 'Как вежливо обратиться к незнакомой женщине?', '["pan","pani","ty","oni"]', 1, 'Pani — вежливое обращение к женщине.', 6),
  ('quiz', 'Выберите правильное про Марека: Marek ___ z Polski.', '["jestem","jesteś","jest","są"]', 2, 'Для он/она/оно используется форма jest.', 7);

insert into public.reading_texts
  (id, topic_id, title, description, level, minutes, emoji, paragraphs, glossary, position, is_active, source_metadata)
values
  (
    'pierwszy-dzien-na-kursie',
    'introductions',
    'Pierwszy dzień na kursie',
    'Анна знакомится с группой на первом уроке польского',
    'A1',
    4,
    '👋',
    '[
      "To jest pierwszy dzień Anny na kursie języka polskiego. Anna wchodzi do sali i mówi: Dzień dobry! Nauczyciel uśmiecha się i odpowiada: Dzień dobry, zapraszam.",
      "Obok Anny siedzi nowy kolega. Mam na imię Marek — mówi. A jak ty masz na imię? Jestem Anna. Miło mi! Marek jest z Polski, a Anna jest z Ukrainy.",
      "Na początku lekcji każdy krótko się przedstawia. Potem nauczyciel pyta: Jak się masz? Anna odpowiada: Dobrze, dziękuję. Po lekcji Anna mówi nowym znajomym: Do widzenia! To był dobry początek."
    ]',
    '{
      "pierwszy":"первый","dzień":"день","kursie":"курсе","wchodzi":"входит",
      "sali":"аудитории","mówi":"говорит","nauczyciel":"преподаватель",
      "uśmiecha":"улыбается","odpowiada":"отвечает","zapraszam":"прошу / проходите",
      "obok":"рядом","siedzi":"сидит","nowy":"новый","kolega":"знакомый / одногруппник",
      "początku":"начале","lekcji":"урока","każdy":"каждый","krótko":"кратко",
      "przedstawia":"представляется","potem":"потом","pyta":"спрашивает",
      "znajomym":"знакомым","początek":"начало"
    }',
    0,
    true,
    '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'
  )
on conflict (id) do update set
  topic_id = excluded.topic_id,
  title = excluded.title,
  description = excluded.description,
  level = excluded.level,
  minutes = excluded.minutes,
  emoji = excluded.emoji,
  paragraphs = excluded.paragraphs,
  glossary = excluded.glossary,
  position = excluded.position,
  is_active = excluded.is_active,
  source_metadata = excluded.source_metadata;
