-- Eleventh original A1 vertical block: health. Existing RLS/grants remain unchanged.
update public.topics set position=11 where course_id='a1-foundations' and position=10;
insert into public.topics(id,course_id,title,description,emoji,position,is_active) values
('health','a1-foundations','Здоровье','Описываем самочувствие, симптомы и простой визит к врачу','🩺',10,true)
on conflict(id) do update set title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,theory_title,theory_sections,source_metadata,position,is_active) values
('health-words','health','words','Zdrowie','Самочувствие','8 карточек · A1','Назови части тела и места помощи',7,'🩺','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',40,true),
('health-grammar','health','grammar','Co cię boli?','Описываем симптомы','5 заданий · A1','Используй boli, bolą и конструкции с mam',8,'✏️','Boli mnie głowa — bolą mnie plecy','[["Одна часть тела","Boli + место в единственном числе: boli mnie głowa, gardło, brzuch."],["Несколько или форма множественного числа","Bolą + множественное число: bolą mnie nogi, oczy, plecy."],["Симптом как состояние","С mam называем симптом: mam katar, kaszel; mam gorączkę, temperaturę."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',41,true),
('health-review','health','review','U lekarza','Визит к врачу','7 карточек · A1','Расскажи о самочувствии и рекомендации',6,'🔄','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',42,true),
('health-quiz','health','quiz','Quiz: zdrowie','Проверка темы','8 вопросов · A1','Проверь симптомы и полезные фразы',5,'🎯','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',43,true)
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('health-zdrowie','zdrowie','здоровье','Zdrowie jest bardzo ważne.',150,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('health-lekarz','lekarz','врач','Idę dziś do lekarza.',151,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('health-apteka','apteka','аптека','Apteka jest obok przychodni.',152,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('health-gardlo','gardło','горло','Boli mnie gardło.',153,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('health-glowa','głowa','голова','Boli mnie głowa.',154,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('health-brzuch','brzuch','живот','Po obiedzie boli mnie brzuch.',155,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('health-temperatura','temperatura','температура','Mam wysoką temperaturę.',156,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('health-lekarstwo','lekarstwo','лекарство','Biorę lekarstwo po jedzeniu.',157,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('health-bolec','boleć','болеть','Co cię boli?',158,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('health-kaszlec','kaszleć','кашлять','Od rana kaszlę.',159,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('health-katar','katar','насморк','Mam katar i źle się czuję.',160,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('health-goraczka','gorączka','жар; высокая температура','Dziecko ma gorączkę.',161,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('health-chory','chory','больной','Piotr jest chory i zostaje w domu.',162,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('health-odpoczywac','odpoczywać','отдыхать','Musisz dużo odpoczywać.',163,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('health-czuc','czuć się','чувствовать себя','Dziś czuję się lepiej.',164,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('health-words','health-review');
insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('health-words','health-zdrowie',0),('health-words','health-lekarz',1),('health-words','health-apteka',2),('health-words','health-gardlo',3),('health-words','health-glowa',4),('health-words','health-brzuch',5),('health-words','health-temperatura',6),('health-words','health-lekarstwo',7),
('health-review','health-bolec',0),('health-review','health-kaszlec',1),('health-review','health-katar',2),('health-review','health-goraczka',3),('health-review','health-chory',4),('health-review','health-odpoczywac',5),('health-review','health-czuc',6);

delete from public.questions where lesson_id in ('health-grammar','health-quiz');
insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('health-grammar','Boli mnie ___.','["głowa","głowę","głowy"]',0,'С одним больным местом используем boli и именительный падеж: boli mnie głowa.',0),
('health-grammar','Bolą mnie ___.','["oko","plecy","gardło"]',1,'С формой множественного числа употребляем bolą: bolą mnie plecy.',1),
('health-grammar','Mam wysoką ___.','["temperatura","temperaturę","temperaturą"]',1,'После mam нужен винительный падеж: mam temperaturę.',2),
('health-grammar','Ola ma ___.','["katar","katarem","kataru"]',0,'У существительного мужского рода katar форма после ma не меняется.',3),
('health-grammar','Как спросить пациента о самочувствии?','["Jak się pan czuje?","Gdzie pan jest?","Co pan lubi?"]',0,'Jak się pan czuje? — вежливый вопрос «Как вы себя чувствуете?».',4),
('health-quiz','Что означает gardło?','["голова","горло","живот"]',1,'Gardło — горло.',0),
('health-quiz','___ mnie brzuch.','["Boli","Bolą","Mam"]',0,'Brzuch — единственное число, поэтому boli mnie brzuch.',1),
('health-quiz','___ mnie plecy.','["Boli","Bolą","Jest"]',1,'Plecy имеют форму множественного числа: bolą mnie plecy.',2),
('health-quiz','Mam ___.','["gorączka","gorączkę","gorączką"]',1,'После mam употребляем винительный падеж: gorączkę.',3),
('health-quiz','Где покупают лекарство?','["W aptece.","W parku.","W szkole."]',0,'Lekarstwo kupujemy w aptece.',4),
('health-quiz','Как сказать «я плохо себя чувствую»?','["Źle się czuję.","Źle się boli.","Mam źle."]',0,'Czuć się описывает самочувствие: źle się czuję.',5),
('health-quiz','Lekarz mówi: musisz dużo ___.','["odpoczywać","odpoczywasz","odpoczywa"]',0,'После musisz ставим инфинитив: odpoczywać.',6),
('health-quiz','У пациента кашель. Что он скажет?','["Kaszlę.","Czytam.","Gotuję."]',0,'Kaszlę — «я кашляю».',7);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('ola-u-lekarza','health','Ola u lekarza','Оля рассказывает врачу о самочувствии','A1',4,'🩺','["Ola źle się dziś czuje. Boli ją gardło i głowa, ma też katar. Rano mierzy temperaturę. Ma trzydzieści osiem stopni, dlatego nie idzie do pracy i dzwoni do przychodni.","Po południu Ola jest u lekarza. Lekarz pyta: „Co panią boli?”. Ola odpowiada, że boli ją gardło i że od wczoraj kaszle. Lekarz bada Olę i mówi, że musi zostać w domu.","Ola dostaje receptę. W drodze do domu idzie do apteki po lekarstwo. Potem pije ciepłą herbatę, bierze tabletkę i odpoczywa. Wieczorem czuje się trochę lepiej."]','{"czuje":{"lemma":"czuć się","translation":"чувствовать себя","part_of_speech":"глагол"},"boli":{"lemma":"boleć","translation":"болеть","part_of_speech":"глагол"},"mierzy":{"lemma":"mierzyć","translation":"измерять","part_of_speech":"глагол"},"stopni":{"lemma":"stopień","translation":"градус","part_of_speech":"существительное"},"przychodni":{"lemma":"przychodnia","translation":"поликлиника","part_of_speech":"существительное"},"pyta":{"lemma":"pytać","translation":"спрашивать","part_of_speech":"глагол"},"odpowiada":{"lemma":"odpowiadać","translation":"отвечать","part_of_speech":"глагол"},"kaszle":{"lemma":"kaszleć","translation":"кашлять","part_of_speech":"глагол"},"bada":{"lemma":"badać","translation":"осматривать","part_of_speech":"глагол"},"receptę":{"lemma":"recepta","translation":"рецепт","part_of_speech":"существительное"},"lekarstwo":{"lemma":"lekarstwo","translation":"лекарство","part_of_speech":"существительное"},"tabletkę":{"lemma":"tabletka","translation":"таблетка","part_of_speech":"существительное"},"odpoczywa":{"lemma":"odpoczywać","translation":"отдыхать","part_of_speech":"глагол"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',10,true)
on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
