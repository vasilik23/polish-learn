-- Twelfth original A1 vertical block: final review. Existing RLS/grants remain unchanged.
update public.topics set position=12 where course_id='a1-foundations' and position=11;
insert into public.topics(id,course_id,title,description,emoji,position,is_active) values
('a1-final-review','a1-foundations','Повторение A1','Соединяем пройденные темы и проверяем готовность к повседневным ситуациям','🏁',11,true)
on conflict(id) do update set title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,theory_title,theory_sections,source_metadata,position,is_active) values
('final-words','a1-final-review','words','A1: najważniejsze','Ключевые слова A1','8 карточек · A1','Повтори опорные слова бытового общения',7,'🏁','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',44,true),
('final-grammar','a1-final-review','grammar','A1 w praktyce','Грамматика в ситуациях','6 заданий · A1','Соедини основные конструкции уровня',9,'✏️','A1 — связываем знакомые конструкции','[["О себе","Согласуй лицо глагола: jestem, mieszkam, pracuję, lubię; для on/ona: jest, mieszka, pracuje, lubi."],["Предметы и места","Проверяй род и падеж: moja siostra, poproszę kawę, w domu, na stole."],["Время, возможность и здоровье","W poniedziałek o ósmej; mogę/muszę + инфинитив; boli + одно, bolą + множественное число."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',45,true),
('final-review','a1-final-review','review','Codzienne sytuacje','Самостоятельное общение','8 карточек · A1','Закрепи действия для реальных задач',7,'🔄','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',46,true),
('final-quiz','a1-final-review','quiz','Diagnoza A1','Итоговая диагностика','12 вопросов · A1','Проверь все темы и готовность к A2',8,'🎯','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',47,true)
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('final-przedstawic','przedstawić się','представиться','Na początku krótko się przedstawiam.',165,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-pochodzic','pochodzić','быть родом','Pochodzę z Ukrainy, ale mieszkam w Polsce.',166,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-rodzina','rodzina','семья','Moja rodzina mieszka blisko.',167,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-codziennie','codziennie','каждый день','Codziennie rano piję herbatę.',168,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-mieszkanie','mieszkanie','квартира','Moje mieszkanie ma dwa pokoje.',169,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-poprosic','poprosić','попросить','Chcę poprosić o wodę.',170,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-droga','droga','дорога; путь','Czy to dobra droga do centrum?',171,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-spotkanie','spotkanie','встреча','Mamy spotkanie o piątej.',172,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-pracowac','pracować','работать','Pracuję od poniedziałku do piątku.',173,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-uczyc','uczyć się','учиться','Wieczorem uczę się polskiego.',174,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-odpoczywac','odpoczywać','отдыхать','W weekend lubię odpoczywać.',175,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-potrzebowac','potrzebować','нуждаться','Potrzebuję pomocy.',176,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-umawiac','umawiać się','договариваться о встрече','Umawiamy się na sobotę.',177,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-czuc','czuć się','чувствовать себя','Dzisiaj czuję się dobrze.',178,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-zalatwic','załatwić','уладить; сделать','Muszę załatwić jedną sprawę.',179,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('final-poradzic','poradzić sobie','справиться','Potrafię poradzić sobie po polsku.',180,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('final-words','final-review');
insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('final-words','final-przedstawic',0),('final-words','final-pochodzic',1),('final-words','final-rodzina',2),('final-words','final-codziennie',3),('final-words','final-mieszkanie',4),('final-words','final-poprosic',5),('final-words','final-droga',6),('final-words','final-spotkanie',7),
('final-review','final-pracowac',0),('final-review','final-uczyc',1),('final-review','final-odpoczywac',2),('final-review','final-potrzebowac',3),('final-review','final-umawiac',4),('final-review','final-czuc',5),('final-review','final-zalatwic',6),('final-review','final-poradzic',7);

delete from public.questions where lesson_id in ('final-grammar','final-quiz');
insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('final-grammar','Ja ___ z Polski.','["jestem","jesteś","są"]',0,'Для ja форма być — jestem.',0),
('final-grammar','To jest ___ siostra.','["mój","moja","moje"]',1,'Siostra — женский род, поэтому moja.',1),
('final-grammar','Codziennie Anna ___ o siódmej.','["wstaję","wstaje","wstajesz"]',1,'Для Anna/ona нужна форма wstaje.',2),
('final-grammar','Poproszę ___.','["kawa","kawę","kawą"]',1,'После poproszę предмет стоит в винительном падеже: kawę.',3),
('final-grammar','Spotykamy się ___ poniedziałek ___ osiemnastej.','["w, o","o, w","na, z"]',0,'С днём употребляем w, со временем — o.',4),
('final-grammar','Boli mnie ___, ale bolą mnie ___.','["głowę, noga","głowa, nogi","głowy, nogę"]',1,'Boli сочетается с единственным числом, bolą — с множественным.',5),
('final-quiz','Как естественно представиться?','["Mam na imię Lena.","Jest imię Lena.","Nazywam do Lena."]',0,'Mam na imię… — базовая форма представления.',0),
('final-quiz','On ___ po polsku.','["mówię","mówisz","mówi"]',2,'Для on форма глагола mówić — mówi.',1),
('final-quiz','To są ___ rodzice.','["mój","moja","moi"]',2,'Во множественном числе о людях: moi rodzice.',2),
('final-quiz','Rano najpierw ___, potem jem śniadanie.','["wstaję","wstaje","wstajesz"]',0,'Для ja употребляем wstaję.',3),
('final-quiz','Książka jest ___ stole.','["w","na","do"]',1,'Предмет находится na stole.',4),
('final-quiz','Poproszę kilogram ___.','["jabłka","jabłek","jabłkami"]',1,'После количества употребляется родительный падеж: kilogram jabłek.',5),
('final-quiz','Как спросить дорогу?','["Jak dojść do dworca?","Jaki dworzec robi?","Gdzie idziesz dworzec?"]',0,'Jak dojść do…? — естественный вопрос о маршруте.',6),
('final-quiz','Spotkanie jest ___ środę ___ piętnastej.','["w, o","o, w","na, od"]',0,'W środę, o piętnastej.',7),
('final-quiz','Muszę ___ raport.','["kończę","skończyć","skończy"]',1,'После muszę ставим инфинитив.',8),
('final-quiz','Lubię ___ książki.','["czytać","czytam","czyta"]',0,'После lubię действие выражается инфинитивом.',9),
('final-quiz','Bolą mnie ___.','["gardło","plecy","głowa"]',1,'Plecy имеют форму множественного числа.',10),
('final-quiz','Что показывает готовность действовать самостоятельно?','["Potrafię poradzić sobie po polsku.","Nie znam żadnego słowa.","Zawsze potrzebuję tłumacza."]',0,'Фраза означает «Я умею справиться на польском».',11);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('samodzielny-dzien-leny','a1-final-review','Samodzielny dzień Leny','Лена решает несколько повседневных задач по-польски','A1',5,'🏁','["Lena pochodzi z Ukrainy i od roku mieszka w Krakowie. Dzisiaj ma dużo planów. Rano dzwoni do przychodni, bo boli ją gardło. Umawia się z lekarzem na czwartek o dziewiątej.","Potem Lena idzie do sklepu. Kupuje chleb, mleko i kilogram jabłek. Pyta też sprzedawcę o aptekę. Apteka jest blisko: trzeba iść prosto, a potem skręcić w lewo.","Po pracy Lena spotyka się z koleżanką w kawiarni. Rozmawiają o rodzinie, pracy i planach na weekend. Lena zamawia herbatę i mówi, że lubi czytać polskie książki. Wieczorem wraca do domu i jest zadowolona: wszystkie sprawy załatwiła po polsku."]','{"pochodzi":{"lemma":"pochodzić","translation":"быть родом","part_of_speech":"глагол"},"przychodni":{"lemma":"przychodnia","translation":"поликлиника","part_of_speech":"существительное"},"umawia":{"lemma":"umawiać się","translation":"договариваться о встрече","part_of_speech":"глагол"},"sprzedawcę":{"lemma":"sprzedawca","translation":"продавец","part_of_speech":"существительное"},"skręcić":{"lemma":"skręcić","translation":"повернуть","part_of_speech":"глагол"},"koleżanką":{"lemma":"koleżanka","translation":"подруга; знакомая","part_of_speech":"существительное"},"zamawia":{"lemma":"zamawiać","translation":"заказывать","part_of_speech":"глагол"},"zadowolona":{"lemma":"zadowolony","translation":"довольный","part_of_speech":"прилагательное"},"sprawy":{"lemma":"sprawa","translation":"дело","part_of_speech":"существительное"},"załatwiła":{"lemma":"załatwić","translation":"уладить; сделать","part_of_speech":"глагол"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',11,true)
on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
