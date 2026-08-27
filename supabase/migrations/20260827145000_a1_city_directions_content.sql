-- Seventh original A1 vertical block: city and directions. Existing RLS/grants remain unchanged.
update public.topics set position=7 where course_id='a1-foundations' and position=6;
insert into public.topics(id,course_id,title,description,emoji,position,is_active) values
('city-directions','a1-foundations','Город и дорога','Спрашиваем дорогу, называем места и объясняем маршрут','🗺️',6,true)
on conflict(id) do update set title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,theory_title,theory_sections,source_metadata,position,is_active) values
('city-words','city-directions','words','W mieście','Места в городе','8 карточек · A1','Назови городские места',7,'🏙️','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',24,true),
('city-grammar','city-directions','grammar','Jak dojść?','Как пройти?','5 заданий · A1','Объясни маршрут вежливыми клише',8,'✏️','Proszę iść prosto — proszę skręcić w lewo','[["Вежливая инструкция","Proszę + инфинитив: proszę iść, proszę skręcić, proszę przejść."],["Направления","Iść prosto — идти прямо; skręcić w lewo / w prawo — повернуть налево / направо."],["Ориентиры","Obok — рядом, naprzeciwko — напротив, przy — у. Спрашиваем: Jak dojść do dworca?"]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',25,true),
('city-review','city-directions','review','Prosto i w lewo','Направления','7 карточек · A1','Закрепи ориентиры и движения',6,'🔄','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',26,true),
('city-quiz','city-directions','quiz','Quiz: miasto','Проверка темы','8 вопросов · A1','Проверь места и объяснение пути',5,'🎯','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',27,true)
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('city-miasto','miasto','город','To miasto jest duże.',90,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('city-ulica','ulica','улица','To jest ulica Długa.',91,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('city-plac','plac','площадь','Spotykamy się na placu.',92,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('city-dworzec','dworzec','вокзал','Dworzec jest blisko centrum.',93,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('city-przystanek','przystanek','остановка','Czekam na przystanku.',94,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('city-apteka','apteka','аптека','Apteka jest obok banku.',95,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('city-bank','bank','банк','Bank jest naprzeciwko kawiarni.',96,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('city-centrum','centrum','центр','Idziemy do centrum.',97,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('city-prosto','prosto','прямо','Proszę iść prosto.',98,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('city-lewo','w lewo','налево','Potem proszę skręcić w lewo.',99,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('city-prawo','w prawo','направо','Na skrzyżowaniu skręć w prawo.',100,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('city-obok','obok','рядом','Muzeum jest obok parku.',101,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('city-naprzeciwko','naprzeciwko','напротив','Kino jest naprzeciwko hotelu.',102,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('city-skrecac','skręcać','поворачивать','Tutaj trzeba skręcić.',103,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('city-przechodzic','przechodzić','переходить','Proszę przejść przez ulicę.',104,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('city-words','city-review');
insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('city-words','city-miasto',0),('city-words','city-ulica',1),('city-words','city-plac',2),('city-words','city-dworzec',3),('city-words','city-przystanek',4),('city-words','city-apteka',5),('city-words','city-bank',6),('city-words','city-centrum',7),
('city-review','city-prosto',0),('city-review','city-lewo',1),('city-review','city-prawo',2),('city-review','city-obok',3),('city-review','city-naprzeciwko',4),('city-review','city-skrecac',5),('city-review','city-przechodzic',6);

delete from public.questions where lesson_id in ('city-grammar','city-quiz');
insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('city-grammar','Proszę iść ___.','["prosto","prosty","prosta"]',0,'После iść направление передаёт наречие prosto: идти прямо.',0),
('city-grammar','Na skrzyżowaniu proszę skręcić ___.','["na lewo","w lewo","do lewa"]',1,'Устойчивое направление — w lewo: повернуть налево.',1),
('city-grammar','Apteka jest ___ banku.','["obok","prosto","przez"]',0,'Obok + родительный падеж обозначает расположение рядом: obok banku.',2),
('city-grammar','Proszę ___ przez ulicę.','["przejść","przechodzi","idzie"]',0,'В вежливой инструкции после proszę употребляем инфинитив: proszę przejść.',3),
('city-grammar','Как вежливо спросить дорогу к вокзалу?','["Gdzie dworzec robi?","Jak dojść do dworca?","Czy dworzec idzie?"]',1,'Jak dojść do…? — естественный вопрос о пути к месту.',4),
('city-quiz','Что означает przystanek?','["остановка","площадь","вокзал"]',0,'Przystanek — остановка общественного транспорта.',0),
('city-quiz','Proszę iść ___.','["prosto","prostą","proste"]',0,'Направление движения выражает наречие prosto.',1),
('city-quiz','Как сказать «поверните направо»?','["Proszę skręcić w prawo.","Proszę iść na prawy.","Proszę prawo jest."]',0,'Skręcić w prawo — повернуть направо.',2),
('city-quiz','Bank jest ___ kawiarni.','["przez","naprzeciwko","w lewo"]',1,'Naprzeciwko означает «напротив» и требует родительного падежа.',3),
('city-quiz','Выберите «вокзал».','["dworzec","przystanek","plac"]',0,'Dworzec — вокзал.',4),
('city-quiz','Proszę ___ przez ulicę.','["przejść","przejdzie","przechodzę"]',0,'После вежливого proszę используем инфинитив przejść.',5),
('city-quiz','Где встречаются на площади?','["na placu","w plac","do plac"]',0,'Для местонахождения на площади употребляем na placu.',6),
('city-quiz','Выберите естественный вопрос о дороге.','["Jak dojść do apteki?","Jak apteka chodzi?","Gdzie iść aptekę?"]',0,'Jak dojść do apteki? — «Как дойти до аптеки?».',7);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('droga-do-muzeum','city-directions','Droga do muzeum','Анна спрашивает дорогу к городскому музею','A1',4,'🗺️','["Anna jest pierwszy raz w tym mieście. Wychodzi z dworca i chce dojść do muzeum w centrum. Nie zna drogi, więc pyta kobietę na przystanku: „Przepraszam, jak dojść do muzeum?”.","Kobieta odpowiada: „Proszę iść prosto ulicą Dworcową. Na drugim skrzyżowaniu proszę skręcić w lewo i przejść przez plac. Potem proszę skręcić w prawo przy banku”.","Anna dziękuje i idzie zgodnie z instrukcją. Muzeum jest obok parku, naprzeciwko małej kawiarni. Droga zajmuje dziesięć minut. Anna bez problemu znajduje wejście."]','{"wychodzi":{"lemma":"wychodzić","translation":"выходить","part_of_speech":"глагол"},"chce":{"lemma":"chcieć","translation":"хотеть","part_of_speech":"глагол"},"dojść":{"lemma":"dojść","translation":"дойти","part_of_speech":"глагол"},"zna":{"lemma":"znać","translation":"знать","part_of_speech":"глагол"},"drogę":{"lemma":"droga","translation":"дорога; путь","part_of_speech":"существительное"},"pyta":{"lemma":"pytać","translation":"спрашивать","part_of_speech":"глагол"},"odpowiada":{"lemma":"odpowiadać","translation":"отвечать","part_of_speech":"глагол"},"skrzyżowaniu":{"lemma":"skrzyżowanie","translation":"перекрёсток","part_of_speech":"существительное"},"przejść":{"lemma":"przejść","translation":"перейти; пройти","part_of_speech":"глагол"},"zgodnie":{"lemma":"zgodnie","translation":"согласно","part_of_speech":"наречие"},"zajmuje":{"lemma":"zajmować","translation":"занимать (время)","part_of_speech":"глагол"},"znajduje":{"lemma":"znajdować","translation":"находить","part_of_speech":"глагол"},"wejście":{"lemma":"wejście","translation":"вход","part_of_speech":"существительное"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',6,true)
on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
