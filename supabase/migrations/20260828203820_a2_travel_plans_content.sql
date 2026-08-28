-- Second original A2 topic. Existing public-content RLS and grants apply unchanged.
insert into public.topics(id,course_id,title,description,emoji,position,is_active) values
('travel-plans','a2-independence','Планы и поездки','Планируем маршрут и говорим о будущих действиях','🧳',1,true)
on conflict(id) do update set course_id=excluded.course_id,title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,theory_title,theory_sections,source_metadata,position,is_active) values
('travel-words','travel-plans','words','Planujemy podróż','План поездки','8 карточек · A2','Назови транспорт, билеты и багаж',7,'🧳','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',53,true),
('travel-grammar','travel-plans','grammar','Co będziemy robić?','Планы на будущее','5 заданий · A2','Различай составное и простое будущее время',9,'✏️','Będę podróżować czy pojadę?','[["Процесс в будущем","С несовершенным глаголом: личная форма być + инфинитив — będę podróżować, będziemy wracać."],["Результат в будущем","Совершенный глагол имеет простую форму: kupię bilet, zarezerwujemy nocleg, pojedziemy."],["Намерение","Используй zamierzam, mam zamiar или chcę + инфинитив: zamierzam odwiedzić Gdańsk."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',54,true),
('travel-review','travel-plans','review','W drogę!','Маршрут и намерения','7 карточек · A2','Повтори действия перед поездкой и в пути',7,'🔄','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',55,true),
('travel-quiz','travel-plans','quiz','Quiz: plany i podróże','Проверка темы','8 вопросов · A2','Проверь лексику и формы будущего времени',6,'🎯','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',56,true),
('travel-reading-check','travel-plans','quiz','Czy rozumiesz plan?','Понимание текста','5 вопросов · A2','Проверь детали поездки Марты и Кубы',5,'📖','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',57,true)
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('travel-planowac','planować','планировать','Planujemy wyjazd nad morze.',196,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('travel-podroz','podróż','путешествие','Podróż pociągiem potrwa pięć godzin.',197,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('travel-wyjazd','wyjazd','поездка; отъезд','Wyjazd jest w sobotę rano.',198,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('travel-bilet','bilet','билет','Kupię bilet przez internet.',199,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('travel-nocleg','nocleg','ночлег','Zarezerwowaliśmy nocleg blisko centrum.',200,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('travel-walizka','walizka','чемодан','Wieczorem spakuję walizkę.',201,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('travel-pociag','pociąg','поезд','Pociąg odjeżdża o siódmej.',202,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('travel-samolot','samolot','самолёт','Samolot ląduje w Gdańsku.',203,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('travel-zamierzac','zamierzać','намереваться','Zamierzam odwiedzić Gdańsk.',204,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('travel-rezerwowac','rezerwować','бронировать','Musimy zarezerwować hotel.',205,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('travel-pakowac','pakować się','собирать вещи','Będę się pakować w piątek.',206,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('travel-wyruszyc','wyruszyć','отправиться в путь','Wyruszymy wcześnie rano.',207,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('travel-dojechac','dojechać','доехать','Jak dojedziemy na dworzec?',208,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('travel-przesiasc','przesiąść się','пересесть','W Warszawie przesiądziemy się do innego pociągu.',209,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('travel-wracac','wracać','возвращаться','Będziemy wracać w niedzielę.',210,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('travel-words','travel-review');
insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('travel-words','travel-planowac',0),('travel-words','travel-podroz',1),('travel-words','travel-wyjazd',2),('travel-words','travel-bilet',3),('travel-words','travel-nocleg',4),('travel-words','travel-walizka',5),('travel-words','travel-pociag',6),('travel-words','travel-samolot',7),
('travel-review','travel-zamierzac',0),('travel-review','travel-rezerwowac',1),('travel-review','travel-pakowac',2),('travel-review','travel-wyruszyc',3),('travel-review','travel-dojechac',4),('travel-review','travel-przesiasc',5),('travel-review','travel-wracac',6);

delete from public.questions where lesson_id in ('travel-grammar','travel-quiz','travel-reading-check');
insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('travel-grammar','Завтра я буду паковать чемодан.','["Jutro będę pakować walizkę.","Jutro pakowałem walizkę.","Jutro będę pakowałeś walizkę."]',0,'Для длительного будущего действия: личная форма być + инфинитив: będę pakować.',0),
('travel-grammar','My ___ wracać w niedzielę.','["będziemy","będziecie","będą"]',0,'Для my используется форма będziemy: będziemy wracać.',1),
('travel-grammar','Ola ___ bilet wieczorem.','["kupi","kupowała","kupuje wczoraj"]',0,'Совершенный глагол kupić образует простое будущее: Ola kupi.',2),
('travel-grammar','Мы намерены посетить Гданьск.','["Zamierzamy odwiedzić Gdańsk.","Zamierzacie odwiedzili Gdańsk.","Zamierzamy odwiedzamy Gdańsk."]',0,'После zamierzać нужен инфинитив: zamierzamy odwiedzić.',3),
('travel-grammar','W Warszawie ___ się do innego pociągu.','["przesiądziemy","przesiadaliśmy","przesiada"]',0,'Совершенная форма przesiądziemy обозначает однократное будущее действие.',4),
('travel-quiz','Что означает planować?','["опаздывать","планировать","возвращаться"]',1,'Planować — планировать.',0),
('travel-quiz','Ja ___ podróżować latem.','["będę","będzie","będziemy"]',0,'Для ja: będę podróżować.',1),
('travel-quiz','Kasia ___ nocleg jutro.','["zarezerwowała wczoraj","zarezerwuje","rezerwować"]',1,'Zarezerwuje — совершенная форма будущего времени.',2),
('travel-quiz','Как спросить, каким путём добраться до вокзала?','["Jak dojedziemy na dworzec?","Kiedy jest walizka?","Dlaczego bilet wraca?"]',0,'Jak dojedziemy na dworzec? — Как мы доберёмся до вокзала?',3),
('travel-quiz','После zamierzam употребляется…','["инфинитив","только прошедшее время","существительное в творительном падеже"]',0,'Намерение выражается конструкцией zamierzam + инфинитив.',4),
('travel-quiz','Pociąg ___ o siódmej.','["odjeżdża","pakuje","nocuje"]',0,'Odjeżdża — отправляется по расписанию.',5),
('travel-quiz','My ___ wcześnie rano.','["wyruszymy","wyruszy","wyruszycie"]',0,'Для my: wyruszymy — мы отправимся.',6),
('travel-quiz','W niedzielę ___ wracać do domu.','["będziemy","byliśmy","jesteśmy wczoraj"]',0,'Будущее длительное действие: będziemy wracać.',7),
('travel-reading-check','Kiedy Marta i Kuba wyjadą z Krakowa?','["W piątek wieczorem","W sobotę po południu","W niedzielę rano"]',0,'Они планируют выехать из Кракова в пятницу вечером.',0),
('travel-reading-check','Gdzie przesiądą się do innego pociągu?','["W Krakowie","W Warszawie","W Gdańsku"]',1,'Пересадка запланирована в Варшаве.',1),
('travel-reading-check','Dlaczego kupią bilety przez internet?','["Żeby nie stać w kolejce","Żeby zmienić hotel","Żeby zabrać dwie walizki"]',0,'Они купят билеты онлайн, чтобы не стоять в очереди.',2),
('travel-reading-check','Co zrobią, jeśli pogoda będzie dobra?','["Wrócą do Krakowa","Zjedzą obiad na plaży","Zostaną na dworcu"]',1,'При хорошей погоде они пообедают на пляже.',3),
('travel-reading-check','Dlaczego spakują tylko jedną walizkę?','["Bo lecą samolotem","Bo hotel jest zamknięty","Bo podróż potrwa dwa dni"]',2,'Им достаточно одного чемодана, потому что поездка продлится два дня.',4);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('plan-wyjazdu-do-gdanska','travel-plans','Plan wyjazdu do Gdańska','Маршрут, планы и решения перед поездкой','A2',5,'🧳','["W przyszły weekend Marta i Kuba pojadą do Gdańska. Zamierzają wyjechać z Krakowa w piątek wieczorem. Najpierw dojadą tramwajem na dworzec, a potem wsiądą do pociągu. W Warszawie przesiądą się do innego pociągu. Bilety kupią przez internet, żeby nie stać w kolejce.","W sobotę będą spacerować po centrum i odwiedzą Europejskie Centrum Solidarności. Po południu pojadą nad morze. Jeśli pogoda będzie dobra, zjedzą obiad na plaży. Nocleg zarezerwują w małym hotelu blisko starówki.","W niedzielę Marta chce zwiedzić muzeum, a Kuba planuje spotkać się z kolegą. Wieczorem będą wracać do Krakowa. Spakują tylko jedną walizkę, bo podróż potrwa dwa dni. Oboje cieszą się na wyjazd."]','{"pojadą":{"lemma":"pojechać","translation":"поехать","part_of_speech":"глагол"},"zamierzają":{"lemma":"zamierzać","translation":"намереваться","part_of_speech":"глагол"},"dojadą":{"lemma":"dojechać","translation":"доехать","part_of_speech":"глагол"},"wsiądą":{"lemma":"wsiąść","translation":"сесть в транспорт","part_of_speech":"глагол"},"przesiądą":{"lemma":"przesiąść się","translation":"пересесть","part_of_speech":"глагол"},"kolejce":{"lemma":"kolejka","translation":"очередь","part_of_speech":"существительное"},"odwiedzą":{"lemma":"odwiedzić","translation":"посетить","part_of_speech":"глагол"},"zarezerwują":{"lemma":"zarezerwować","translation":"забронировать","part_of_speech":"глагол"},"starówki":{"lemma":"starówka","translation":"старый город","part_of_speech":"существительное"},"potrwa":{"lemma":"potrwać","translation":"продлиться","part_of_speech":"глагол"},"cieszą":{"lemma":"cieszyć się","translation":"радоваться","part_of_speech":"глагол"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28","comprehension_lesson_id":"travel-reading-check"}',13,true)
on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
