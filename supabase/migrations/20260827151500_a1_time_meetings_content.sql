-- Eighth original A1 vertical block: time and meetings. Existing RLS/grants remain unchanged.
update public.topics set position=8 where course_id='a1-foundations' and position=7;
insert into public.topics(id,course_id,title,description,emoji,position,is_active) values
('time-meetings','a1-foundations','Время и встречи','Называем время и дни недели, договариваемся о встрече','🕒',7,true)
on conflict(id) do update set title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,theory_title,theory_sections,source_metadata,position,is_active) values
('time-words','time-meetings','words','Dni i godziny','Дни и время','8 карточек · A1','Назови дни и единицы времени',7,'📅','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',28,true),
('time-grammar','time-meetings','grammar','O której?','Договариваемся','5 заданий · A1','Используй o, w и we со временем',8,'✏️','O szóstej — w poniedziałek — we wtorek','[["Точное время","Перед часом используем o: o szóstej, o ósmej, o dziesiątej."],["Дни недели","W poniedziałek, w środę, w piątek, но we wtorek. Для выходных: w weekend."],["Договорённость","Спрашиваем: O której się spotykamy? Czy pasuje ci piątek? Отвечаем: Tak, pasuje mi."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',29,true),
('time-review','time-meetings','review','Kiedy się spotykamy?','Планы на неделю','7 карточек · A1','Предложи время встречи',6,'🔄','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',30,true),
('time-quiz','time-meetings','quiz','Quiz: czas','Проверка темы','8 вопросов · A1','Проверь время, дни и договорённости',5,'🎯','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',31,true)
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('time-godzina','godzina','час; время','Która jest godzina?',105,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('time-minuta','minuta','минута','Spotkanie zaczyna się za pięć minut.',106,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('time-poniedzialek','poniedziałek','понедельник','W poniedziałek pracuję.',107,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('time-wtorek','wtorek','вторник','We wtorek mam kurs.',108,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('time-sroda','środa','среда','W środę spotykam się z Olą.',109,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('time-czwartek','czwartek','четверг','W czwartek jestem w domu.',110,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('time-piatek','piątek','пятница','W piątek idziemy do kina.',111,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('time-weekend','weekend','выходные','W weekend mam czas.',112,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('time-dzisiaj','dzisiaj','сегодня','Dzisiaj jest środa.',113,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('time-jutro','jutro','завтра','Jutro mam spotkanie.',114,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('time-rano','rano','утром','Rano piję kawę.',115,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('time-wieczorem','wieczorem','вечером','Wieczorem czytam książkę.',116,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('time-spotkanie','spotkanie','встреча','Spotkanie jest o szóstej.',117,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('time-o-ktorej','o której?','в котором часу?','O której zaczynamy?',118,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('time-pasowac','pasować','подходить; быть удобным','Czy pasuje ci piątek?',119,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('time-words','time-review');
insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('time-words','time-godzina',0),('time-words','time-minuta',1),('time-words','time-poniedzialek',2),('time-words','time-wtorek',3),('time-words','time-sroda',4),('time-words','time-czwartek',5),('time-words','time-piatek',6),('time-words','time-weekend',7),
('time-review','time-dzisiaj',0),('time-review','time-jutro',1),('time-review','time-rano',2),('time-review','time-wieczorem',3),('time-review','time-spotkanie',4),('time-review','time-o-ktorej',5),('time-review','time-pasowac',6);

delete from public.questions where lesson_id in ('time-grammar','time-quiz');
insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('time-grammar','Spotkanie jest ___ szóstej.','["w","o","na"]',1,'Точное время вводим предлогом o: o szóstej.',0),
('time-grammar','Kurs jest ___ poniedziałek.','["o","w","na"]',1,'С днями недели употребляем w: w poniedziałek.',1),
('time-grammar','Spotykamy się ___ wtorek.','["we","o","do"]',0,'Перед wtorek для удобства произношения употребляем we: we wtorek.',2),
('time-grammar','Как спросить время встречи?','["Który spotkanie?","O której się spotykamy?","Gdzie godzina?"]',1,'O której się spotykamy? — естественный вопрос «Во сколько встречаемся?».',3),
('time-grammar','Czy pasuje ci piątek?','["Тебе подходит пятница?","Ты работаешь в пятницу?","Сегодня пятница?"]',0,'Pasować в договорённостях означает «подходить, быть удобным».',4),
('time-quiz','Что означает jutro?','["сегодня","завтра","утром"]',1,'Jutro — завтра.',0),
('time-quiz','Film zaczyna się ___ ósmej.','["o","w","we"]',0,'Перед точным временем используем o.',1),
('time-quiz','___ wtorek mam lekcję.','["O","We","Na"]',1,'Говорим we wtorek.',2),
('time-quiz','Как сказать «в среду»?','["o środzie","w środę","na środa"]',1,'Устойчивое сочетание — w środę.',3),
('time-quiz','O ___ zaczynamy?','["której","który","która"]',0,'О времени спрашиваем o której?',4),
('time-quiz','Что означает spotkanie?','["расписание","встреча","опоздание"]',1,'Spotkanie — встреча.',5),
('time-quiz','Выберите естественный ответ на предложение встретиться.','["Tak, pasuje mi.","Tak, jestem godzina.","Tak, spotkanie robi."]',0,'Pasuje mi — «мне подходит».',6),
('time-quiz','Dzisiaj jest czwartek, a ___ piątek.','["rano","jutro","wieczorem"]',1,'Если сегодня четверг, завтра — пятница: jutro.',7);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('spotkanie-w-piatek','time-meetings','Spotkanie w piątek','Марта и Павел договариваются встретиться после работы','A1',4,'🕒','["W środę Marta pisze do Pawła. Chce spotkać się z nim w tym tygodniu. Pyta: „Czy pasuje ci czwartek wieczorem?”. Paweł odpowiada, że w czwartek ma kurs języka polskiego.","Paweł proponuje piątek. Marta ma czas, więc pyta: „O której się spotykamy?”. Ustalają spotkanie o szóstej. Chcą wypić kawę w małej kawiarni obok parku.","W piątek Marta kończy pracę o piątej. Jedzie autobusem do centrum i przychodzi pięć minut wcześniej. Paweł już czeka przy wejściu. Oboje cieszą się, że zaczynają weekend razem."]','{"pisze":{"lemma":"pisać","translation":"писать","part_of_speech":"глагол"},"spotkać":{"lemma":"spotkać się","translation":"встретиться","part_of_speech":"глагол"},"tygodniu":{"lemma":"tydzień","translation":"неделя","part_of_speech":"существительное"},"odpowiada":{"lemma":"odpowiadać","translation":"отвечать","part_of_speech":"глагол"},"proponuje":{"lemma":"proponować","translation":"предлагать","part_of_speech":"глагол"},"ustalają":{"lemma":"ustalać","translation":"договариваться; определять","part_of_speech":"глагол"},"wypić":{"lemma":"wypić","translation":"выпить","part_of_speech":"глагол"},"kończy":{"lemma":"kończyć","translation":"заканчивать","part_of_speech":"глагол"},"jedzie":{"lemma":"jechać","translation":"ехать","part_of_speech":"глагол"},"przychodzi":{"lemma":"przychodzić","translation":"приходить","part_of_speech":"глагол"},"wcześniej":{"lemma":"wcześnie","translation":"раньше","part_of_speech":"наречие"},"czeka":{"lemma":"czekać","translation":"ждать","part_of_speech":"глагол"},"cieszą":{"lemma":"cieszyć się","translation":"радоваться","part_of_speech":"глагол"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',7,true)
on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
