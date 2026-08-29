insert into public.topics(id,course_id,title,description,emoji,position,is_active) values
('culture-media','a2-independence','Культура и медиа','Пересказываем произведение и выражаем оценку','🎬',7,true)
on conflict(id) do update set course_id=excluded.course_id,title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,position,is_active,theory_title,theory_sections,source_metadata) values
('culture-words','culture-media','words','Film, książka, wystawa','Культура и форматы','8 карточек · A2','Назови произведение и его создателей',8,'🎬',83,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-grammar','culture-media','grammar','Go, ją, je czy ich?','Объектные местоимения','5 заданий · A2','Не повторяй названия людей и произведений',9,'✏️',84,true,'Краткие объектные местоимения','[["Мужской объект","Film или serial заменяем на go: Obejrzałem go."],["Женский объект","Książkę, aktorkę или recenzję заменяем на ją: Czytam ją."],["Множественное число","Неодушевлённые объекты заменяет je, лично-мужскую группу — ich."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-review','culture-media','review','Moja krótka recenzja','Оценка произведения','7 карточек · A2','Повтори лексику пересказа и рекомендации',7,'🔄',85,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-quiz','culture-media','quiz','Quiz: kultura i media','Проверка темы','8 вопросов · A2','Проверь лексику и объектные местоимения',6,'🎯',86,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-reading-check','culture-media','quiz','Czy rozumiesz recenzję?','Понимание текста','5 вопросов · A2','Проверь детали фестиваля Лены и Павла',5,'📖',87,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}')
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('culture-film','film','фильм','Wczoraj obejrzeliśmy ciekawy film.',286,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-serial','serial','сериал','Ten serial ma sześć odcinków.',287,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-powiesc','powieść','роман','Czytam powieść o życiu w Krakowie.',288,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-wystawa','wystawa','выставка','Nowa wystawa opowiada o historii miasta.',289,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-spektakl','spektakl','спектакль','Spektakl trwał prawie dwie godziny.',290,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-rezyser','reżyser','режиссёр','Reżyser spotkał się z publicznością.',291,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-aktor','aktor','актёр','Główny aktor zagrał bardzo naturalnie.',292,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-fabula','fabuła','сюжет','Fabuła była prosta, ale poruszająca.',293,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-bohater','bohater','герой произведения','Bohater wraca do rodzinnego miasta.',294,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-recenzja','recenzja','рецензия','Przeczytałam krótką recenzję filmu.',295,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-odcinek','odcinek','серия','Najnowszy odcinek pojawi się w piątek.',296,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-polecac','polecać','рекомендовать','Polecam ten film całej rodzinie.',297,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-oceniac','oceniać','оценивать','Trudno oceniać książkę po jednym rozdziale.',298,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-wzruszajacy','wzruszający','трогательный','Finał był naprawdę wzruszający.',299,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('culture-nudny','nudny','скучный','Początek był trochę nudny, lecz później akcja przyspieszyła.',300,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('culture-words','culture-review');
insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('culture-words','culture-film',0),('culture-words','culture-serial',1),('culture-words','culture-powiesc',2),('culture-words','culture-wystawa',3),('culture-words','culture-spektakl',4),('culture-words','culture-rezyser',5),('culture-words','culture-aktor',6),('culture-words','culture-fabula',7),
('culture-review','culture-bohater',0),('culture-review','culture-recenzja',1),('culture-review','culture-odcinek',2),('culture-review','culture-polecac',3),('culture-review','culture-oceniac',4),('culture-review','culture-wzruszajacy',5),('culture-review','culture-nudny',6);

delete from public.questions where lesson_id in ('culture-grammar','culture-quiz','culture-reading-check');
insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('culture-grammar','Obejrzałem ten film. Obejrzałem ___ wczoraj.','["go","jej","ich"]',0,'Мужской неодушевлённый объект film заменяется местоимением go.',0),
('culture-grammar','Znam tę aktorkę. Widziałem ___ w teatrze.','["ją","go","im"]',0,'Женский объект tę aktorkę заменяется винительным ją.',1),
('culture-grammar','Czytasz te recenzje? Czytasz ___ regularnie?','["je","go","nią"]',0,'Во множественном числе неодушевлённые объекты заменяет je.',2),
('culture-grammar','Составьте: Я рекомендую его, потому что сюжет интересный.','["Polecam go, bo fabuła jest ciekawa.","Polecam jej, że fabuła ciekawy.","Go polecać dlatego fabuła jest."]',0,'Go относится к фильму, а bo вводит причину рекомендации.',3),
('culture-grammar','Anna przeczytała powieść i potem ___ oceniła.','["ją","go","ich"]',0,'Powieść — женский род, поэтому в винительном падеже используется ją.',4),
('culture-quiz','Что означает fabuła?','["сюжет","режиссёр","выставка"]',0,'Fabuła — последовательность событий произведения.',0),
('culture-quiz','Ten serial jest świetny. Oglądam ___ co tydzień.','["go","ją","je"]',0,'Serial — мужской род: oglądam go.',1),
('culture-quiz','Как сказать «Я рекомендую эту книгу»?','["Polecam tę książkę.","Oceniam tego książka.","Polecam ją książkę jej."]',0,'Polecać + винительный: polecam tę książkę.',2),
('culture-quiz','Widzieliśmy aktorów i później spotkaliśmy ___.','["ich","je","go"]',0,'Лично-мужская группа aktorów заменяется местоимением ich.',3),
('culture-quiz','Что можно назвать wzruszający?','["трогательный финал","цена билета","время начала"]',0,'Wzruszający описывает сильную эмоциональную реакцию на произведение.',4),
('culture-quiz','Film był trochę nudny, ___ zakończenie mi się podobało.','["ale","że","dlatego że"]',0,'Ale противопоставляет две оценки фильма.',5),
('culture-quiz','Przeczytałam recenzję. Autor dobrze ___ napisał.','["ją","go","ich"]',0,'Recenzja — женский род, поэтому: napisał ją.',6),
('culture-quiz','Кто отвечает за постановку фильма?','["reżyser","bohater","publiczność"]',0,'Reżyser руководит созданием фильма.',7),
('culture-reading-check','Na jakie wydarzenie poszli Lena i Paweł?','["Na festiwal krótkich filmów","Na wystawę fotografii","Na koncert rockowy"]',0,'Они выбрали фестиваль короткометражных фильмов.',0),
('culture-reading-check','Który film najbardziej spodobał się Lenie?','["Historia o starszej sąsiadce","Komedia o pracy","Film sportowy"]',0,'Лену тронула история пожилой соседки.',1),
('culture-reading-check','Dlaczego Paweł inaczej ocenił pierwszy film?','["Tempo było dla niego zbyt wolne","Nie rozumiał języka","Nie widział zakończenia"]',0,'Павлу показался слишком медленным темп.',2),
('culture-reading-check','Co zrobili po pokazie?','["Porozmawiali z reżyserką","Kupili książkę","Wrócili bez rozmowy"]',0,'После показа они задали режиссёру вопросы.',3),
('culture-reading-check','Co Lena opublikowała następnego dnia?','["Krótką recenzję","Cały film","Wywiad z aktorem"]',0,'На следующий день Лена опубликовала короткую рецензию.',4);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('wieczor-krotkich-filmow','culture-media','Wieczór krótkich filmów','Фестиваль, разные мнения и короткая рецензия','A2',6,'🎬',
'["W sobotę Lena i Paweł poszli na festiwal krótkich filmów. W programie były trzy historie młodych polskich reżyserów. Pierwszy film opowiadał o starszej sąsiadce, która codziennie pomagała mieszkańcom swojego domu. Lena uznała go za prosty, ale bardzo wzruszający.","Paweł też docenił główną bohaterkę, jednak tempo filmu było dla niego zbyt wolne. Bardziej spodobała mu się lekka komedia o pierwszym dniu w nowej pracy. Oboje zgodzili się, że aktorzy zagrali naturalnie, a dialogi brzmiały wiarygodnie.","Po pokazie widzowie spotkali się z reżyserką pierwszego filmu. Lena zapytała ją o pomysł na fabułę, a Paweł powiedział, dlaczego inaczej ocenił zakończenie. Następnego dnia Lena opublikowała krótką recenzję. Poleciła w niej cały festiwal, bo różne filmy zachęciły ich do ciekawej rozmowy."]',
'{"reżyserów":{"lemma":"reżyser","translation":"режиссёр","part_of_speech":"существительное"},"sąsiadce":{"lemma":"sąsiadka","translation":"соседка","part_of_speech":"существительное"},"uznała":{"lemma":"uznać","translation":"счесть","part_of_speech":"глагол"},"wzruszający":{"lemma":"wzruszający","translation":"трогательный","part_of_speech":"прилагательное"},"docenił":{"lemma":"docenić","translation":"оценить по достоинству","part_of_speech":"глагол"},"wiarygodnie":{"lemma":"wiarygodnie","translation":"правдоподобно","part_of_speech":"наречие"},"widzowie":{"lemma":"widz","translation":"зрители","part_of_speech":"существительное"},"reżyserką":{"lemma":"reżyserka","translation":"режиссёр (женщина)","part_of_speech":"существительное"},"opublikowała":{"lemma":"opublikować","translation":"опубликовать","part_of_speech":"глагол"},"zachęciły":{"lemma":"zachęcić","translation":"побудить","part_of_speech":"глагол"}}',
'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29","comprehension_lesson_id":"culture-reading-check"}',19,true)
on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
