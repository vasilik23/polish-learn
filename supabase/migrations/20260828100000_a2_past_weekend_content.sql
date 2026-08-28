-- First original A2 vertical block: past weekend. Existing RLS/grants remain unchanged.
insert into public.courses(id,title,description,level,position,is_active) values
('a2-independence','Самостоятельность','Связное общение в знакомых повседневных ситуациях','A2',1,true)
on conflict(id) do update set title=excluded.title,description=excluded.description,level=excluded.level,position=excluded.position,is_active=excluded.is_active;
update public.topics set position=1 where course_id='a2-independence' and position=0;
insert into public.topics(id,course_id,title,description,emoji,position,is_active) values
('past-weekend','a2-independence','Прошедшие выходные','Рассказываем о завершённых событиях и впечатлениях','📆',0,true)
on conflict(id) do update set course_id=excluded.course_id,title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,theory_title,theory_sections,source_metadata,position,is_active) values
('past-words','past-weekend','words','Miniony weekend','События выходных','8 карточек · A2','Назови время, места и впечатления',7,'📆','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',48,true),
('past-grammar','past-weekend','grammar','Co robiłeś?','Прошедшее время','5 заданий · A2','Согласуй прошедшую форму с родом и группой',9,'✏️','Byłem, byłam — что происходило раньше','[["Он и она","В единственном числе форма показывает род: on pracował/był, ona pracowała/była."],["Я","Говорящий выбирает форму по своему роду: robiłem/byłem или robiłam/byłam."],["Мы и они","Для группы с мужчиной: byliśmy, robili; для группы только из женщин/предметов: byłyśmy, robiły."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',49,true),
('past-review','past-weekend','review','Jak było?','Рассказ о прошлом','7 карточек · A2','Расскажи, куда ездил и что делал',7,'🔄','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',50,true),
('past-quiz','past-weekend','quiz','Quiz: miniony weekend','Проверка темы','8 вопросов · A2','Проверь формы прошедшего времени',6,'🎯','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',51,true)
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('past-weekend','weekend','выходные','W weekend byliśmy poza miastem.',181,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('past-wczoraj','wczoraj','вчера','Wczoraj długo pracowałam.',182,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('past-przedwczoraj','przedwczoraj','позавчера','Przedwczoraj spotkałem znajomych.',183,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('past-ostatnio','ostatnio','в последнее время','Ostatnio często chodziliśmy do kina.',184,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('past-wycieczka','wycieczka','экскурсия; поездка','Wycieczka była bardzo udana.',185,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('past-koncert','koncert','концерт','W sobotę byliśmy na koncercie.',186,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('past-muzeum','muzeum','музей','W niedzielę zwiedziliśmy muzeum.',187,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('past-odpoczynek','odpoczynek','отдых','Po podróży potrzebowałam odpoczynku.',188,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('past-spedzic','spędzić','провести (время)','Spędziliśmy weekend w górach.',189,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('past-pojechac','pojechać','поехать','Rano pojechaliśmy pociągiem.',190,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('past-odwiedzic','odwiedzić','навестить; посетить','Odwiedziłam babcię w sobotę.',191,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('past-zobaczyc','zobaczyć','увидеть','Zobaczyliśmy stary zamek.',192,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('past-spotkac','spotkać się','встретиться','Wieczorem spotkałem się z kolegą.',193,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('past-wrocic','wrócić','вернуться','Wróciliśmy późno do domu.',194,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}'),
('past-wydarzyc','wydarzyć się','произойти','Co wydarzyło się w weekend?',195,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('past-words','past-review');
insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('past-words','past-weekend',0),('past-words','past-wczoraj',1),('past-words','past-przedwczoraj',2),('past-words','past-ostatnio',3),('past-words','past-wycieczka',4),('past-words','past-koncert',5),('past-words','past-muzeum',6),('past-words','past-odpoczynek',7),
('past-review','past-spedzic',0),('past-review','past-pojechac',1),('past-review','past-odwiedzic',2),('past-review','past-zobaczyc',3),('past-review','past-spotkac',4),('past-review','past-wrocic',5),('past-review','past-wydarzyc',6);

delete from public.questions where lesson_id in ('past-grammar','past-quiz');
insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('past-grammar','В субботу Марек работал дома.','["W sobotę Marek pracował w domu.","W sobotę Marek pracowała w domu.","W sobotę Marek pracuje w domu."]',0,'В мужском роде прошедшее время имеет окончание -ł: pracował.',0),
('past-grammar','Ania __ do kina.','["poszedł","poszła","poszli"]',1,'Для Ania нужна женская форма poszła.',1),
('past-grammar','My (мужчина и женщина) ___ w Krakowie.','["byliśmy","byłyśmy","byłem"]',0,'Для смешанной группы употребляется форма męskoosobowa: byliśmy.',2),
('past-grammar','Kasia i Ola ___ muzeum.','["zwiedzili","zwiedziły","zwiedziła"]',1,'Для группы только из женщин нужна форма niemęskoosobowa: zwiedziły.',3),
('past-grammar','Ja (женщина) długo ___.','["odpoczywałem","odpoczywałam","odpoczywali"]',1,'Говорящая женщина выбирает форму odpoczywałam.',4),
('past-quiz','Что означает przedwczoraj?','["завтра","позавчера","недавно"]',1,'Przedwczoraj — позавчера.',0),
('past-quiz','Paweł ___ film.','["oglądał","oglądała","oglądali"]',0,'Paweł — мужской род: oglądał.',1),
('past-quiz','Ewa ___ książkę.','["czytał","czytała","czytali"]',1,'Ewa — женский род: czytała.',2),
('past-quiz','Tomek i Adam ___ na koncert.','["poszły","poszli","poszedł"]',1,'Группа мужчин: poszli.',3),
('past-quiz','Mama i córka ___ w domu.','["zostały","zostali","została"]',0,'Группа женщин: zostały.',4),
('past-quiz','Как спросить о прошлых выходных?','["Co robiłeś w weekend?","Co robisz jutro?","Gdzie robi weekend?"]',0,'Co robiłeś/robiłaś w weekend? — вопрос о завершённом прошлом.',5),
('past-quiz','My (смешанная группа) ___ późno.','["wróciliśmy","wróciłyśmy","wróciłem"]',0,'Для смешанной группы: wróciliśmy.',6),
('past-quiz','Ja (мужчина) ___ weekend w domu.','["spędziłam","spędziłem","spędzili"]',1,'Мужская форма первого лица: spędziłem.',7);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('weekend-kasi-i-pawla','past-weekend','Weekend Kasi i Pawła','Два разных рассказа о прошедших выходных','A2',5,'📆','["W piątek po pracy Kasia pojechała pociągiem do Wrocławia. Odwiedziła koleżankę ze studiów. Wieczorem poszły razem na mały koncert, a potem długo rozmawiały w kawiarni.","W sobotę Kasia i jej koleżanka zwiedziły muzeum i zobaczyły rynek. Pogoda była słoneczna, więc dużo spacerowały. Kasia wróciła do Krakowa w niedzielę wieczorem. Była zmęczona, ale bardzo zadowolona.","Paweł spędził weekend inaczej. Został w domu, ugotował obiad i obejrzał dwa filmy. W niedzielę spotkał się z bratem i razem pojechali na rowerach do parku. Paweł odpoczął i w poniedziałek miał dużo energii."]','{"pojechała":{"lemma":"pojechać","translation":"поехать","part_of_speech":"глагол"},"odwiedziła":{"lemma":"odwiedzić","translation":"навестить","part_of_speech":"глагол"},"poszły":{"lemma":"pójść","translation":"пойти","part_of_speech":"глагол"},"zwiedziły":{"lemma":"zwiedzić","translation":"осмотреть; посетить","part_of_speech":"глагол"},"rynek":{"lemma":"rynek","translation":"рыночная площадь","part_of_speech":"существительное"},"spacerowały":{"lemma":"spacerować","translation":"гулять","part_of_speech":"глагол"},"zmęczona":{"lemma":"zmęczony","translation":"уставший","part_of_speech":"прилагательное"},"spędził":{"lemma":"spędzić","translation":"провести (время)","part_of_speech":"глагол"},"ugotował":{"lemma":"ugotować","translation":"приготовить","part_of_speech":"глагол"},"obejrzał":{"lemma":"obejrzeć","translation":"посмотреть","part_of_speech":"глагол"},"odpoczął":{"lemma":"odpocząć","translation":"отдохнуть","part_of_speech":"глагол"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',12,true)
on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
