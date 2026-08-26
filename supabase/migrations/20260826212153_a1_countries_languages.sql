-- Second original A1 content block: countries and languages.
-- Existing public-content RLS policies and grants remain unchanged.

update public.topics set position = 2
where course_id = 'a1-foundations' and position = 1;

insert into public.topics (id, course_id, title, description, emoji, position, is_active)
values ('countries-languages', 'a1-foundations', 'Страны и языки',
  'Рассказываем, откуда мы и на каких языках говорим', '🌍', 1, true)
on conflict (id) do update set title=excluded.title, description=excluded.description,
  emoji=excluded.emoji, position=excluded.position, is_active=excluded.is_active;

insert into public.lessons
  (id, topic_id, kind, title, plan_title, subtitle, description, minutes, emoji,
   theory_title, theory_sections, source_metadata, position, is_active)
values
('countries-words','countries-languages','words','Kraje i ludzie','Страны и люди','8 карточек · A1','Назови страну, жителя и язык',7,'🌍','', '[]', '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}',4,true),
('countries-grammar','countries-languages','grammar','Język polski','Род и прилагательные','5 заданий · A1','Свяжи страну, человека и язык',8,'✏️','Страна, человек и язык','[["Род","Polak — мужчина, Polka — женщина; Polska — название страны женского рода."],["Прилагательные","język polski, język ukraiński, język niemiecki. Прилагательное согласуется с существительным."],["Как сказать о языке","Mówię po polsku. Znam język polski. Pochodzę z Polski."]]', '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}',5,true),
('countries-review','countries-languages','review','Mówię po polsku','Языки общения','7 карточек · A1','Расскажи, какие языки знаешь',6,'🔄','', '[]', '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}',6,true),
('countries-quiz','countries-languages','quiz','Quiz: kraje i języki','Проверка темы','8 вопросов · A1','Закрепи страны, жителей и языки',5,'🎯','', '[]', '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}',7,true)
on conflict (id) do update set topic_id=excluded.topic_id, kind=excluded.kind, title=excluded.title,
 plan_title=excluded.plan_title, subtitle=excluded.subtitle, description=excluded.description,
 minutes=excluded.minutes, emoji=excluded.emoji, theory_title=excluded.theory_title,
 theory_sections=excluded.theory_sections, source_metadata=excluded.source_metadata,
 position=excluded.position, is_active=excluded.is_active;

insert into public.flashcards (id,polish,translation,example,position,is_active,source_metadata) values
('polska','Polska','Польша','Polska leży w Europie.',15,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('polak','Polak','поляк','Marek to Polak.',16,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('polka','Polka','полька','Anna to Polka.',17,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('polski','polski','польский','Uczę się języka polskiego.',18,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('ukraina','Ukraina','Украина','Oksana pochodzi z Ukrainy.',19,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('ukrainiec','Ukrainiec','украинец','Andrij to Ukrainiec.',20,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('ukrainka','Ukrainka','украинка','Oksana to Ukrainka.',21,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('ukrainski','ukraiński','украинский','Mówię po ukraińsku.',22,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('niemcy','Niemcy','Германия','Berlin leży w Niemczech.',23,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('niemiec','Niemiec','немец','Thomas to Niemiec.',24,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('niemiecki','niemiecki','немецкий','Znam język niemiecki.',25,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('jezyk','język','язык','Jaki język znasz?',26,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('mowic','mówić','говорить','Mówię trochę po polsku.',27,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('znac','znać','знать','Znam polski i angielski.',28,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('pochodzic','pochodzić','быть родом','Skąd pochodzisz?',29,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}')
on conflict (id) do update set polish=excluded.polish,translation=excluded.translation,
 example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('countries-words','countries-review');
insert into public.lesson_flashcards (lesson_id,flashcard_id,position) values
('countries-words','polska',0),('countries-words','polak',1),('countries-words','polka',2),('countries-words','polski',3),
('countries-words','ukraina',4),('countries-words','ukrainiec',5),('countries-words','ukrainka',6),('countries-words','ukrainski',7),
('countries-review','niemcy',0),('countries-review','niemiec',1),('countries-review','niemiecki',2),('countries-review','jezyk',3),
('countries-review','mowic',4),('countries-review','znac',5),('countries-review','pochodzic',6);

delete from public.questions where lesson_id in ('countries-grammar','countries-quiz');
insert into public.questions (lesson_id,prompt,options,correct,explanation,position) values
('countries-grammar','Какого рода слово Polska?','["мужского","женского","среднего"]',1,'Названия стран на -a обычно женского рода: ta Polska.',0),
('countries-grammar','Выберите правильную пару.','["Polska — polski","Polska — polska język","Polska — polsko"]',0,'Прилагательное мужского рода: język polski.',1),
('countries-grammar','Ona jest ___. Вставьте «полька».','["Polak","Polką","polski"]',1,'После jest при указании национальности употребляется творительный падеж: jest Polką.',2),
('countries-grammar','Как сказать «Я говорю по-польски»?','["Mówię polski.","Mówię po polsku.","Znam z Polski."]',1,'Для языка общения используется конструкция mówić po + наречие: po polsku.',3),
('countries-grammar','Skąd pochodzisz? Выберите естественный ответ.','["Pochodzę z Ukrainy.","Mówię Ukraina.","Jestem język."]',0,'Pochodzę z… означает «Я родом из…».',4),
('countries-quiz','Что означает «Skąd pochodzisz?»','["Где ты живёшь?","Откуда ты родом?","На каком языке ты говоришь?"]',1,'Pochodzić — быть родом, происходить.',0),
('countries-quiz','Как сказать «польский язык»?','["język polska","polski język","język polski"]',2,'Нейтральный порядок: język polski.',1),
('countries-quiz','Выберите женскую национальность.','["Polak","Polka","polski"]',1,'Polka — полька; Polak — поляк.',2),
('countries-quiz','Mówię ___ ukraińsku.','["na","z","po"]',2,'Язык общения выражается через po: po ukraińsku.',3),
('countries-quiz','Thomas pochodzi z Niemiec. Kim jest?','["Niemcem","Polakiem","Ukraińcem"]',0,'Человек из Германии — Niemiec; после jest: Niemcem.',4),
('countries-quiz','Что значит «Trochę znam język polski»?','["Я немного знаю польский","Я родом из Польши","Я не говорю по-польски"]',0,'Znać język — знать язык.',5),
('countries-quiz','Выберите название страны.','["ukraiński","Ukrainiec","Ukraina"]',2,'Ukraina — страна; Ukrainiec — человек; ukraiński — прилагательное.',6),
('countries-quiz','Как спросить «На каких языках ты говоришь?»','["Jakimi językami mówisz?","Skąd jesteś język?","Jaki kraj znasz?"]',0,'Jakimi językami mówisz? — естественный вопрос о языках общения.',7);

insert into public.reading_texts
(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('rozmowa-w-miedzynarodowej-grupie','countries-languages','Rozmowa w międzynarodowej grupie','Участники курса рассказывают о странах и языках','A1',4,'🌍',
'["Na kursie języka polskiego jest międzynarodowa grupa. Oksana pochodzi z Ukrainy. Mówi po ukraińsku, po rosyjsku i trochę po polsku. Chce dobrze znać polski, ponieważ mieszka w Krakowie.","Thomas jest Niemcem i pochodzi z Berlina. Jego język ojczysty to niemiecki, ale zna też angielski. Z Anną rozmawia po polsku. Anna jest Polką i pomaga nowym osobom.","Nauczyciel pyta każdego: Skąd pochodzisz i jakimi językami mówisz? Wszyscy odpowiadają inaczej, ale razem uczą się jednego języka. Dzięki temu grupa szybko się poznaje."]',
'{"międzynarodowa":"международная","pochodzi":"родом","rosyjsku":"по-русски","ponieważ":"потому что","dobrze":"хорошо","ojczysty":"родной","angielski":"английский","rozmawia":"разговаривает","pomaga":"помогает","każdego":"каждого","jakimi":"какими","wszyscy":"все","inaczej":"по-разному","razem":"вместе","dzięki":"благодаря","szybko":"быстро"}',
'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}',1,true)
on conflict (id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,
 level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,
 glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
