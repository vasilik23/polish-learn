-- Fourth original A1 vertical block: daily routine.
-- Existing RLS policies and grants remain unchanged; no new tables are exposed.
update public.topics set position=4 where course_id='a1-foundations' and position=3;
insert into public.topics (id,course_id,title,description,emoji,position,is_active) values
('daily-routine','a1-foundations','Мой день','Описываем распорядок дня и частые действия','☀️',3,true)
on conflict (id) do update set title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons (id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,theory_title,theory_sections,source_metadata,position,is_active) values
('daily-routine-words','daily-routine','words','Mój dzień','Распорядок дня','8 карточек · A1','Назови главные действия своего дня',7,'☀️','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',12,true),
('daily-routine-grammar','daily-routine','grammar','Co robisz codziennie?','Настоящее время','5 заданий · A1','Используй личные формы и наречия частоты',8,'✏️','Настоящее время в распорядке дня','[["Личные формы","Глагол меняется по лицам: ja wstaję, ty wstajesz, on/ona wstaje; ja czytam, ty czytasz, ona czyta."],["Частотность","zawsze — всегда, często — часто, czasem — иногда, nigdy — никогда. С nigdy говорим: nigdy nie pracuję."],["Время и порядок","O której? — O siódmej. Сначала: najpierw, затем: potem, вечером: wieczorem."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',13,true),
('daily-routine-review','daily-routine','review','Rano i wieczorem','Утро и вечер','7 карточек · A1','Закрепи последовательность ежедневных действий',6,'🔄','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',14,true),
('daily-routine-quiz','daily-routine','quiz','Quiz: mój dzień','Проверка темы','8 вопросов · A1','Проверь глаголы, порядок дня и частотность',5,'🎯','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',15,true)
on conflict (id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.flashcards (id,polish,translation,example,position,is_active,source_metadata) values
('wstawac','wstawać','вставать','Wstaję o siódmej.',45,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('budzic-sie','budzić się','просыпаться','Budzę się wcześnie.',46,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('myc-sie','myć się','мыться','Rano myję się i ubieram.',47,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('ubierac-sie','ubierać się','одеваться','Ubieram się szybko.',48,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('jesc-sniadanie','jeść śniadanie','завтракать','Jem śniadanie w domu.',49,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('isc-do-pracy','iść do pracy','идти на работу','O ósmej idę do pracy.',50,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('zaczynac','zaczynać','начинать','Zaczynam pracę o dziewiątej.',51,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('konczyc','kończyć','заканчивать','Kończę pracę o siedemnastej.',52,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('wracac','wracać','возвращаться','Wieczorem wracam do domu.',53,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('gotowac','gotować','готовить','Często gotuję kolację.',54,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('odpoczywac','odpoczywać','отдыхать','Po pracy odpoczywam.',55,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('czytac','czytać','читать','Czasem czytam książkę.',56,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('klasc-sie-spac','kłaść się spać','ложиться спать','Kładę się spać o jedenastej.',57,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('codziennie','codziennie','каждый день','Codziennie piję rano kawę.',58,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('czasem','czasem','иногда','Czasem jadę do pracy rowerem.',59,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}')
on conflict (id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('daily-routine-words','daily-routine-review');
insert into public.lesson_flashcards (lesson_id,flashcard_id,position) values
('daily-routine-words','wstawac',0),('daily-routine-words','budzic-sie',1),('daily-routine-words','myc-sie',2),('daily-routine-words','ubierac-sie',3),('daily-routine-words','jesc-sniadanie',4),('daily-routine-words','isc-do-pracy',5),('daily-routine-words','zaczynac',6),('daily-routine-words','konczyc',7),
('daily-routine-review','wracac',0),('daily-routine-review','gotowac',1),('daily-routine-review','odpoczywac',2),('daily-routine-review','czytac',3),('daily-routine-review','klasc-sie-spac',4),('daily-routine-review','codziennie',5),('daily-routine-review','czasem',6);

delete from public.questions where lesson_id in ('daily-routine-grammar','daily-routine-quiz');
insert into public.questions (lesson_id,prompt,options,correct,explanation,position) values
('daily-routine-grammar','Ja ___ o siódmej. Выберите форму wstawać.','["wstaję","wstajesz","wstaje"]',0,'Для ja употребляется форма wstaję.',0),
('daily-routine-grammar','Ty ___ śniadanie w domu. Выберите форму jeść.','["jem","jesz","je"]',1,'Для ty глагол jeść имеет форму jesz.',1),
('daily-routine-grammar','Ona ___ pracę o dziewiątej. Выберите форму zaczynać.','["zaczynam","zaczynasz","zaczyna"]',2,'Для ona используется форма zaczyna.',2),
('daily-routine-grammar','Как сказать «Я часто читаю вечером»?','["Często czytam wieczorem.","Czytać często wieczór.","Wieczorem często czytasz."]',0,'Наречие często можно поставить перед глаголом.',3),
('daily-routine-grammar','Выберите естественную фразу.','["Nigdy nie piję kawy wieczorem.","Nigdy piję nie kawę.","Nie nigdy kawa piję."]',0,'С nigdy отрицание оформляется конструкцией nigdy nie + глагол.',4),
('daily-routine-quiz','Что означает wstawać?','["вставать","работать","возвращаться"]',0,'Wstawać — вставать.',0),
('daily-routine-quiz','Выберите «Я завтракаю дома».','["Jem śniadanie w domu.","Gotuję dom rano.","Idę śniadanie."]',0,'Jeść śniadanie — завтракать.',1),
('daily-routine-quiz','My ___ do domu o szóstej. Форма wracać.','["wracam","wracacie","wracamy"]',2,'Для my используется окончание -my: wracamy.',2),
('daily-routine-quiz','Как сказать «иногда»?','["zawsze","czasem","codziennie"]',1,'Czasem означает «иногда».',3),
('daily-routine-quiz','Что происходит раньше?','["kładę się spać","budzę się","wracam wieczorem"]',1,'Сначала человек просыпается: budzę się.',4),
('daily-routine-quiz','Выберите правильную фразу с nigdy.','["Nigdy nie pracuję w niedzielę.","Nigdy pracuję w niedzielę.","Nie pracować nigdy niedziela."]',0,'После nigdy используется nie перед личной формой глагола.',5),
('daily-routine-quiz','O której zaczynasz pracę? — ___','["O dziewiątej.","Codziennie.","Do domu."]',0,'На вопрос o której? отвечают временем с o.',6),
('daily-routine-quiz','Выберите логичный порядок.','["wstaję → jem śniadanie → idę do pracy","idę spać → wstaję → jem kolację","wracam → budzę się → zaczynam dzień"]',0,'Обычный утренний порядок: встать, позавтракать, пойти на работу.',7);

insert into public.reading_texts (id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('zwykly-dzien-oli','daily-routine','Zwykły dzień Oli','Оля рассказывает о своём обычном дне','A1',4,'☀️',
'["Ola budzi się o szóstej trzydzieści, ale wstaje o siódmej. Najpierw myje się i ubiera. Potem je śniadanie. Zwykle pije herbatę i je kanapkę z serem.","O ósmej Ola idzie do pracy. Pracę zaczyna o dziewiątej. W południe je obiad z koleżanką. Kończy pracę o siedemnastej i wraca autobusem do domu.","Wieczorem Ola gotuje kolację, a potem odpoczywa. Czasem czyta książkę, a czasem rozmawia z rodziną. Nigdy nie pracuje w nocy. O jedenastej kładzie się spać."]',
'{"budzi":{"lemma":"budzić się","translation":"просыпаться","part_of_speech":"глагол"},"najpierw":{"lemma":"najpierw","translation":"сначала","part_of_speech":"наречие"},"myje":{"lemma":"myć się","translation":"мыться","part_of_speech":"глагол"},"ubiera":{"lemma":"ubierać się","translation":"одеваться","part_of_speech":"глагол"},"zwykle":{"lemma":"zwykle","translation":"обычно","part_of_speech":"наречие"},"kanapkę":{"lemma":"kanapka","translation":"бутерброд","part_of_speech":"существительное"},"serem":{"lemma":"ser","translation":"сыр","part_of_speech":"существительное"},"południe":{"lemma":"południe","translation":"полдень","part_of_speech":"существительное"},"koleżanką":{"lemma":"koleżanka","translation":"коллега","part_of_speech":"существительное"},"kończy":{"lemma":"kończyć","translation":"заканчивать","part_of_speech":"глагол"},"wraca":{"lemma":"wracać","translation":"возвращаться","part_of_speech":"глагол"},"gotuje":{"lemma":"gotować","translation":"готовить","part_of_speech":"глагол"},"odpoczywa":{"lemma":"odpoczywać","translation":"отдыхать","part_of_speech":"глагол"},"rozmawia":{"lemma":"rozmawiać","translation":"разговаривать","part_of_speech":"глагол"},"kładzie":{"lemma":"kłaść się","translation":"ложиться","part_of_speech":"глагол"}}',
'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',3,true)
on conflict (id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

-- Backfill canonical forms for frequent inflections in previously published readings.
update public.reading_texts set glossary = glossary ||
'{"odwiedza":{"lemma":"odwiedzać","translation":"навещать","part_of_speech":"глагол"},"przyjeżdżają":{"lemma":"przyjeżdżać","translation":"приезжать","part_of_speech":"глагол"},"pracuje":{"lemma":"pracować","translation":"работать","part_of_speech":"глагол"},"interesuje":{"lemma":"interesować się","translation":"интересоваться","part_of_speech":"глагол"},"stole":{"lemma":"stół","translation":"стол","part_of_speech":"существительное"},"tygodniu":{"lemma":"tydzień","translation":"неделя","part_of_speech":"существительное"},"pokazuje":{"lemma":"pokazywać","translation":"показывать","part_of_speech":"глагол"},"zdjęcia":{"lemma":"zdjęcie","translation":"фотография","part_of_speech":"существительное"},"dwojgiem":{"lemma":"dwoje","translation":"двое","part_of_speech":"числительное"}}'::jsonb
where id='niedziela-u-babci';
update public.reading_texts set glossary = glossary ||
'{"międzynarodowa":{"lemma":"międzynarodowy","translation":"международный","part_of_speech":"прилагательное"},"pochodzi":{"lemma":"pochodzić","translation":"быть родом","part_of_speech":"глагол"},"rozmawia":{"lemma":"rozmawiać","translation":"разговаривать","part_of_speech":"глагол"},"pomaga":{"lemma":"pomagać","translation":"помогать","part_of_speech":"глагол"},"każdego":{"lemma":"każdy","translation":"каждый","part_of_speech":"местоимение"},"jakimi":{"lemma":"jaki","translation":"какой","part_of_speech":"местоимение"}}'::jsonb
where id='rozmowa-w-miedzynarodowej-grupie';
update public.reading_texts set glossary = glossary ||
'{"przedstawia":{"lemma":"przedstawiać","translation":"представляться","part_of_speech":"глагол"},"mówi":{"lemma":"mówić","translation":"говорить","part_of_speech":"глагол"},"pochodzi":{"lemma":"pochodzić","translation":"быть родом","part_of_speech":"глагол"},"mieszka":{"lemma":"mieszkać","translation":"жить","part_of_speech":"глагол"}}'::jsonb
where id='pierwszy-dzien-na-kursie';
