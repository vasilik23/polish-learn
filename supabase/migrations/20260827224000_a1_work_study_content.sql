-- Ninth original A1 vertical block: work and study. Existing RLS/grants remain unchanged.
update public.topics set position=9 where course_id='a1-foundations' and position=8;
insert into public.topics(id,course_id,title,description,emoji,position,is_active) values
('work-study','a1-foundations','Работа и учёба','Рассказываем о занятии, месте и простых обязанностях','💼',8,true)
on conflict(id) do update set title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,theory_title,theory_sections,source_metadata,position,is_active) values
('work-words','work-study','words','Praca i szkoła','Работа и учёба','8 карточек · A1','Назови места и людей',7,'💼','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',32,true),
('work-grammar','work-study','grammar','Mogę i muszę','Возможности и обязанности','5 заданий · A1','Используй móc и musieć с инфинитивом',8,'✏️','Mogę pracować — muszę skończyć','[["Возможность","Móc + инфинитив: mogę pracować, możesz pomóc, on/ona może przyjść."],["Обязанность","Musieć + инфинитив: muszę skończyć, musisz napisać, on/ona musi przeczytać."],["Множественное число","My możemy / musimy, wy możecie / musicie. После модального глагола форма действия не меняется."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',33,true),
('work-review','work-study','review','Co robisz?','Задачи дня','7 карточек · A1','Расскажи о работе и занятиях',6,'🔄','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',34,true),
('work-quiz','work-study','quiz','Quiz: praca','Проверка темы','8 вопросов · A1','Проверь занятия и модальные глаголы',5,'🎯','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',35,true)
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('work-praca','praca','работа','Mam nową pracę.',120,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('work-szkola','szkoła','школа','Szkoła jest blisko domu.',121,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('work-biuro','biuro','офис','Pracuję w małym biurze.',122,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('work-firma','firma','компания','Ta firma jest w centrum.',123,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('work-student','student','студент','Jestem studentem.',124,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('work-nauczyciel','nauczyciel','учитель','Nauczyciel prowadzi lekcję.',125,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('work-pracownik','pracownik','сотрудник','Pracownik zaczyna o ósmej.',126,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('work-uczyc-sie','uczyć się','учиться','Uczę się języka polskiego.',127,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('work-pracowac','pracować','работать','Pracuję od poniedziałku do piątku.',128,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('work-studiowac','studiować','учиться в вузе','Studiuję informatykę.',129,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('work-zaczynac','zaczynać','начинать','Zaczynam pracę o dziewiątej.',130,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('work-konczyc','kończyć','заканчивать','Kończę kurs o szóstej.',131,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('work-zadanie','zadanie','задание','Mam dziś ważne zadanie.',132,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('work-moc','móc','мочь','Mogę pracować w domu.',133,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('work-music','musieć','быть должным','Muszę wysłać wiadomość.',134,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('work-words','work-review');
insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('work-words','work-praca',0),('work-words','work-szkola',1),('work-words','work-biuro',2),('work-words','work-firma',3),('work-words','work-student',4),('work-words','work-nauczyciel',5),('work-words','work-pracownik',6),('work-words','work-uczyc-sie',7),
('work-review','work-pracowac',0),('work-review','work-studiowac',1),('work-review','work-zaczynac',2),('work-review','work-konczyc',3),('work-review','work-zadanie',4),('work-review','work-moc',5),('work-review','work-music',6);

delete from public.questions where lesson_id in ('work-grammar','work-quiz');
insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('work-grammar','Dzisiaj ___ pracować w domu.','["mogę","może","możesz"]',0,'Для ja форма глагола móc — mogę.',0),
('work-grammar','Anna ___ skończyć zadanie.','["muszę","musisz","musi"]',2,'Для ona форма musieć — musi; после неё употребляем инфинитив.',1),
('work-grammar','Czy ___ mi pomóc?','["możesz","mogę","może"]',0,'К одному собеседнику обращаемся: Czy możesz…?',2),
('work-grammar','My ___ uczyć się codziennie.','["musimy","musicie","musi"]',0,'Для my форма musieć — musimy.',3),
('work-grammar','Что ставим после mogę / muszę?','["инфинитив","прошедшее время","существительное только"]',0,'Модальный глагол соединяется с инфинитивом: mogę pracować, muszę skończyć.',4),
('work-quiz','Что означает biuro?','["офис","школа","задание"]',0,'Biuro — офис.',0),
('work-quiz','Ja ___ pracować jutro.','["może","mogę","możesz"]',1,'С ja употребляем mogę.',1),
('work-quiz','Paweł ___ wysłać email.','["muszę","musisz","musi"]',2,'Для on форма — musi.',2),
('work-quiz','Выберите базовую форму «учиться».','["uczyć się","uczę się","uczy"]',0,'Словарная форма — uczyć się.',3),
('work-quiz','Как сказать «я работаю в офисе»?','["Pracuję w biurze.","Praca jestem biuro.","Pracować na biuro."]',0,'Естественная конструкция: pracuję w biurze.',4),
('work-quiz','My ___ o ósmej.','["zaczynamy","zaczyna","zaczynasz"]',0,'Для my: zaczynamy.',5),
('work-quiz','Что означает zadanie?','["компания","занятие","задание"]',2,'Zadanie — задание или задача.',6),
('work-quiz','Выберите естественное предложение.','["Muszę skończyć pracę.","Muszę kończę pracę.","Musi ja praca."]',0,'После muszę нужен инфинитив: skończyć.',7);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('pierwszy-dzien-w-pracy','work-study','Pierwszy dzień w pracy','Касия начинает новую работу и продолжает учить польский','A1',4,'💼','["Kasia ma nową pracę w małej firmie w centrum. Pracuje w biurze od poniedziałku do piątku. Zaczyna o ósmej, ale pierwszego dnia przychodzi dziesięć minut wcześniej.","Kierownik pokazuje jej biurko i przedstawia innych pracowników. Kasia musi przeczytać krótką instrukcję i napisać pierwszą wiadomość. Może pytać koleżankę, kiedy czegoś nie rozumie.","Po pracy Kasia jedzie do szkoły językowej. Uczy się polskiego dwa razy w tygodniu. Lekcja kończy się o siódmej. Kasia jest zmęczona, ale zadowolona: może pracować i studiować w tym samym mieście."]','{"pracuje":{"lemma":"pracować","translation":"работать","part_of_speech":"глагол"},"przychodzi":{"lemma":"przychodzić","translation":"приходить","part_of_speech":"глагол"},"kierownik":{"lemma":"kierownik","translation":"руководитель","part_of_speech":"существительное"},"pokazuje":{"lemma":"pokazywać","translation":"показывать","part_of_speech":"глагол"},"biurko":{"lemma":"biurko","translation":"письменный стол","part_of_speech":"существительное"},"przedstawia":{"lemma":"przedstawiać","translation":"представлять","part_of_speech":"глагол"},"pracowników":{"lemma":"pracownik","translation":"сотрудник","part_of_speech":"существительное"},"przeczytać":{"lemma":"przeczytać","translation":"прочитать","part_of_speech":"глагол"},"wiadomość":{"lemma":"wiadomość","translation":"сообщение","part_of_speech":"существительное"},"pytać":{"lemma":"pytać","translation":"спрашивать","part_of_speech":"глагол"},"rozumie":{"lemma":"rozumieć","translation":"понимать","part_of_speech":"глагол"},"zmęczona":{"lemma":"zmęczony","translation":"уставший","part_of_speech":"прилагательное"},"zadowolona":{"lemma":"zadowolony","translation":"довольный","part_of_speech":"прилагательное"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',8,true)
on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
