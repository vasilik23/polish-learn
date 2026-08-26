-- Third original A1 content block: family.
-- Existing public-content RLS policies and grants remain unchanged.
update public.topics set position=3 where course_id='a1-foundations' and position=2;
insert into public.topics (id,course_id,title,description,emoji,position,is_active)
values ('family','a1-foundations','Семья','Рассказываем о близких, возрасте и родстве','👨‍👩‍👧',2,true)
on conflict (id) do update set title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons (id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,theory_title,theory_sections,source_metadata,position,is_active) values
('family-words','family','words','Moja rodzina','Члены семьи','8 карточек · A1','Назови близких и расскажи, кто есть в семье',7,'👨‍👩‍👧','', '[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}',8,true),
('family-grammar','family','grammar','Mój, moja, moje','Моя семья','5 заданий · A1','Используй притяжательные местоимения и возраст',8,'✏️','Mój, moja, moje — чей это?','[["Согласование","mój tata · moja mama · moje dziecko · moi rodzice. Форма зависит от рода и числа предмета."],["Его и её","jego brat — его брат; jej siostra — её сестра. Jego и jej не изменяются."],["Возраст","Ile masz lat? Mam rok, dwa/trzy/cztery lata, пять и больше — lat: Mam dwanaście lat."]]', '{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}',9,true),
('family-review','family','review','Ile masz lat?','Родство и возраст','7 карточек · A1','Закрепи родство и вопросы о возрасте',6,'🔄','', '[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}',10,true),
('family-quiz','family','quiz','Quiz: rodzina','Проверка темы','8 вопросов · A1','Проверь лексику семьи, местоимения и числа',5,'🎯','', '[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}',11,true)
on conflict (id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.flashcards (id,polish,translation,example,position,is_active,source_metadata) values
('rodzina','rodzina','семья','To jest moja rodzina.',30,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('mama','mama','мама','Moja mama ma na imię Ewa.',31,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('tata','tata','папа','Mój tata lubi kawę.',32,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('rodzice','rodzice','родители','Moi rodzice mieszkają w Gdańsku.',33,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('brat','brat','брат','Mam jednego brata.',34,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('siostra','siostra','сестра','Moja siostra ma osiemnaście lat.',35,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('syn','syn','сын','Ich syn chodzi do szkoły.',36,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('corka','córka','дочь','Nasza córka ma pięć lat.',37,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('babcia','babcia','бабушка','Babcia mieszka blisko nas.',38,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('dziadek','dziadek','дедушка','Mój dziadek czyta gazetę.',39,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('maz','mąż','муж','Jej mąż ma na imię Adam.',40,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('zona','żona','жена','Jego żona jest lekarką.',41,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('dziecko','dziecko','ребёнок','To dziecko ma dwa lata.',42,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('dzieci','dzieci','дети','Oni mają dwoje dzieci.',43,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}'),
('ile-lat','ile lat?','сколько лет?','Ile lat ma twój brat?',44,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}')
on conflict (id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('family-words','family-review');
insert into public.lesson_flashcards (lesson_id,flashcard_id,position) values
('family-words','rodzina',0),('family-words','mama',1),('family-words','tata',2),('family-words','rodzice',3),('family-words','brat',4),('family-words','siostra',5),('family-words','syn',6),('family-words','corka',7),
('family-review','babcia',0),('family-review','dziadek',1),('family-review','maz',2),('family-review','zona',3),('family-review','dziecko',4),('family-review','dzieci',5),('family-review','ile-lat',6);

delete from public.questions where lesson_id in ('family-grammar','family-quiz');
insert into public.questions (lesson_id,prompt,options,correct,explanation,position) values
('family-grammar','Выберите: ___ tata ma na imię Piotr.','["Mój","Moja","Moje"]',0,'Tata — существительное мужского рода, поэтому mój tata.',0),
('family-grammar','Выберите: ___ siostra ma dwadzieścia lat.','["Mój","Moja","Moi"]',1,'Siostra — женского рода: moja siostra.',1),
('family-grammar','Как сказать «его мама»?','["jego mama","jej mama","mój mama"]',0,'Jego не изменяется по роду и означает «его».',2),
('family-grammar','Как спросить возраст сестры?','["Ile siostra?","Ile lat ma twoja siostra?","Jaki rok siostra?"]',1,'Возраст спрашивают конструкцией Ile lat ma…?',3),
('family-grammar','Ania ma 12 ___. Выберите форму.','["rok","lata","lat"]',2,'После 12 используется форма lat: dwanaście lat.',4),
('family-quiz','Кто такие rodzice?','["дети","родители","бабушка и дедушка"]',1,'Rodzice — родители.',0),
('family-quiz','Выберите «моя мама».','["mój mama","moja mama","moje mama"]',1,'С существительным женского рода употребляется moja.',1),
('family-quiz','Что означает «Mam jednego brata»?','["У меня один брат","У меня одна сестра","Я вижу брата"]',0,'Mam… сообщает, кто есть в семье.',2),
('family-quiz','Как сказать «их дети»?','["ich dzieci","jego dzieci","nasz dzieci"]',0,'Ich означает «их» и не изменяется.',3),
('family-quiz','Ola ma 4 ___. Вставьте форму.','["rok","lata","lat"]',1,'После 2, 3 и 4 употребляется lata: cztery lata.',4),
('family-quiz','Piotr ma 15 ___. Вставьте форму.','["rok","lata","lat"]',2,'После 15 употребляется lat.',5),
('family-quiz','Кто такая córka?','["дочь","жена","бабушка"]',0,'Córka — дочь; syn — сын.',6),
('family-quiz','Как спросить «Сколько лет твоему брату?»','["Ile lat ma twój brat?","Kto jest brat?","Czy brat ma rodzina?"]',0,'Ile lat ma…? — стандартный вопрос о возрасте.',7);

insert into public.reading_texts (id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('niedziela-u-babci','family','Niedziela u babci','Майя рассказывает о семейной встрече','A1',4,'🏡',
'["W niedzielę Maja odwiedza babcię i dziadka. Babcia ma sześćdziesiąt osiem lat, a dziadek siedemdziesiąt. Mieszkają w małym domu blisko Krakowa. Maja bardzo lubi ich ogród.","Na obiad przyjeżdżają też rodzice Mai. Jej mama Ewa jest nauczycielką, a tata Paweł pracuje w banku. Maja ma jednego brata. Kuba ma szesnaście lat i interesuje się sportem.","Przy stole każdy opowiada o swoim tygodniu. Potem Maja pokazuje rodzinne zdjęcia. Na jednym zdjęciu jest jej ciocia z mężem i dwojgiem dzieci. To spokojne, dobre popołudnie razem."]',
'{"niedzielę":"воскресенье","odwiedza":"навещает","ogród":"сад","obiad":"обед","przyjeżdżają":"приезжают","pracuje":"работает","interesuje":"интересуется","stole":"столе","każdy":"каждый","opowiada":"рассказывает","tygodniu":"неделе","pokazuje":"показывает","rodzinne":"семейные","zdjęcia":"фотографии","ciocia":"тётя","dwojgiem":"двумя","spokojne":"спокойное","popołudnie":"вторая половина дня"}',
'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-26"}',2,true)
on conflict (id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
