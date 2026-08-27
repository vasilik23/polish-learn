-- Tenth original A1 vertical block: free time. Existing RLS/grants remain unchanged.
update public.topics set position=10 where course_id='a1-foundations' and position=9;
insert into public.topics(id,course_id,title,description,emoji,position,is_active) values
('free-time','a1-foundations','Свободное время','Рассказываем об интересах, любимых занятиях и планах на выходные','🎨',9,true)
on conflict(id) do update set title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,theory_title,theory_sections,source_metadata,position,is_active) values
('free-words','free-time','words','Czas wolny','Досуг и интересы','8 карточек · A1','Назови занятия и увлечения',7,'🎨','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',36,true),
('free-grammar','free-time','grammar','Co lubisz robić?','Говорим о предпочтениях','5 заданий · A1','Используй lubić с инфинитивом и предметом',8,'✏️','Lubię czytać — lubię muzykę','[["Любимое действие","Lubić + инфинитив: lubię czytać, lubisz oglądać, lubimy grać."],["Любимый предмет","После lubić предмет стоит в винительном падеже: lubię muzykę, książkę, sport."],["Интерес","Interesować się + творительный падеж: interesuję się kinem, muzyką, sportem."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',37,true),
('free-review','free-time','review','Weekend','Любимые занятия','7 карточек · A1','Расскажи, как проводишь свободное время',6,'🔄','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',38,true),
('free-quiz','free-time','quiz','Quiz: czas wolny','Проверка темы','8 вопросов · A1','Проверь досуг и предпочтения',5,'🎯','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',39,true)
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('free-czas','czas wolny','свободное время','W weekend mam czas wolny.',135,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('free-ksiazka','książka','книга','Czytam ciekawą książkę.',136,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('free-film','film','фильм','Wieczorem oglądam film.',137,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('free-muzyka','muzyka','музыка','Lubię polską muzykę.',138,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('free-sport','sport','спорт','Sport daje mi energię.',139,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('free-spacer','spacer','прогулка','Idziemy na spacer do parku.',140,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('free-rower','rower','велосипед','Latem często jeżdżę na rowerze.',141,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('free-przyjaciel','przyjaciel','друг','Spotykam się z przyjacielem.',142,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('free-czytac','czytać','читать','Lubię czytać wieczorem.',143,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('free-ogladac','oglądać','смотреть','Oglądamy nowy film.',144,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('free-sluchac','słuchać','слушать','Słucham muzyki w domu.',145,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('free-grac','grać','играть','Gram w piłkę z kolegami.',146,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('free-jezdzic','jeździć','ездить','W weekend jeżdżę na rowerze.',147,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('free-lubic','lubić','любить; нравиться','Lubię dobrą kawę.',148,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('free-interesowac','interesować się','интересоваться','Interesuję się kinem.',149,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('free-words','free-review');
insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('free-words','free-czas',0),('free-words','free-ksiazka',1),('free-words','free-film',2),('free-words','free-muzyka',3),('free-words','free-sport',4),('free-words','free-spacer',5),('free-words','free-rower',6),('free-words','free-przyjaciel',7),
('free-review','free-czytac',0),('free-review','free-ogladac',1),('free-review','free-sluchac',2),('free-review','free-grac',3),('free-review','free-jezdzic',4),('free-review','free-lubic',5),('free-review','free-interesowac',6);

delete from public.questions where lesson_id in ('free-grammar','free-quiz');
insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('free-grammar','Lubię ___ książki.','["czytać","czytam","czyta"]',0,'После lubię можно поставить инфинитив: lubię czytać.',0),
('free-grammar','Ola lubi ___.','["muzyka","muzykę","muzyki"]',1,'После lubić предмет обычно стоит в винительном падеже: muzykę.',1),
('free-grammar','My lubimy ___ filmy.','["oglądać","oglądamy","ogląda"]',0,'После lubimy действие остаётся в инфинитиве: oglądać.',2),
('free-grammar','Paweł interesuje się ___.','["sport","sportem","sportu"]',1,'Interesować się требует творительного падежа: sportem.',3),
('free-grammar','Как спросить о любимом занятии?','["Co lubisz robić?","Co robisz lubi?","Jaki lubić?"]',0,'Co lubisz robić? — естественный вопрос «Что ты любишь делать?».',4),
('free-quiz','Что означает spacer?','["спорт","прогулка","выходные"]',1,'Spacer — прогулка.',0),
('free-quiz','Lubię ___ muzyki.','["słuchać","słucham","słucha"]',0,'После lubię употребляем инфинитив słuchać.',1),
('free-quiz','Anna lubi ___.','["książka","książkę","książką"]',1,'После lubi нужна форма książkę.',2),
('free-quiz','Как сказать «я играю в футбол»?','["Gram w piłkę.","Jestem piłka.","Gram na piłkę."]',0,'С играми и спортом употребляем grać w: gram w piłkę.',3),
('free-quiz','Interesuję się ___.','["kino","kinem","kina"]',1,'После interesuję się употребляем творительный падеж: kinem.',4),
('free-quiz','Что означает jeździć na rowerze?','["ездить на велосипеде","гулять пешком","смотреть гонки"]',0,'Jeździć na rowerze — регулярно ездить на велосипеде.',5),
('free-quiz','Выберите естественный вопрос.','["Co lubisz robić w weekend?","Co weekend lubi robi?","Jaki ty czas robić?"]',0,'Co lubisz robić…? спрашивает о предпочтениях.',6),
('free-quiz','My ___ oglądać filmy.','["lubicie","lubimy","lubi"]',1,'Для my форма lubić — lubimy.',7);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('wolna-sobota-marka','free-time','Wolna sobota Marka','Марк проводит свободный день с друзьями','A1',4,'🎨','["Marek pracuje od poniedziałku do piątku, dlatego lubi spokojne soboty. Rano długo pije kawę i czyta książkę. Interesuje się historią, ale czasem wybiera też prosty kryminał.","Po południu Marek spotyka się z przyjaciółmi w parku. Kiedy jest ciepło, jeżdżą na rowerach albo grają w piłkę. Dzisiaj pada deszcz, więc idą do małej kawiarni.","Wieczorem wszyscy oglądają film u Marka. Jego przyjaciółka Ania lubi komedie, a Marek woli filmy podróżnicze. Wybierają krótką komedię i zamawiają pizzę. To prosty, ale bardzo dobry weekend."]','{"dlatego":{"lemma":"dlatego","translation":"поэтому","part_of_speech":"наречие"},"spokojne":{"lemma":"spokojny","translation":"спокойный","part_of_speech":"прилагательное"},"wybiera":{"lemma":"wybierać","translation":"выбирать","part_of_speech":"глагол"},"kryminał":{"lemma":"kryminał","translation":"детектив","part_of_speech":"существительное"},"spotyka":{"lemma":"spotykać się","translation":"встречаться","part_of_speech":"глагол"},"przyjaciółmi":{"lemma":"przyjaciel","translation":"друг","part_of_speech":"существительное"},"jeżdżą":{"lemma":"jeździć","translation":"ездить","part_of_speech":"глагол"},"grają":{"lemma":"grać","translation":"играть","part_of_speech":"глагол"},"pada":{"lemma":"padać","translation":"идти (о дожде)","part_of_speech":"глагол"},"wszyscy":{"lemma":"wszyscy","translation":"все","part_of_speech":"местоимение"},"woli":{"lemma":"woleć","translation":"предпочитать","part_of_speech":"глагол"},"podróżnicze":{"lemma":"podróżniczy","translation":"о путешествиях","part_of_speech":"прилагательное"},"zamawiają":{"lemma":"zamawiać","translation":"заказывать","part_of_speech":"глагол"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',9,true)
on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
