insert into public.topics (id, course_id, title, description, emoji, position, is_active)
values ('relationships-emotions', 'a2-independence', 'Отношения и эмоции', 'Выражаем чувства, объясняем причины и решаем недопонимание', '💬', 6, true)
on conflict (id) do update set course_id=excluded.course_id, title=excluded.title, description=excluded.description, emoji=excluded.emoji, position=excluded.position, is_active=excluded.is_active;

insert into public.lessons (id, topic_id, kind, title, plan_title, subtitle, description, minutes, emoji, position, is_active, theory_title, theory_sections, source_metadata) values
('rel-words','relationships-emotions','words','Relacje i uczucia','Отношения и чувства','8 карточек · A2','Назови эмоции и важные элементы отношений',8,'💛',78,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-grammar','relationships-emotions','grammar','Że, bo czy dlatego?','Причина, содержание и следствие','5 заданий · A2','Связывай мнение, эмоцию и объяснение',9,'✏️',79,true,'Że, bo, dlatego i dlatego że','[["Содержание мысли или чувства","Że отвечает на вопрос «что?»: Cieszę się, że jesteś tutaj."],["Причина","Bo и dlatego że отвечают на вопрос «почему?»: Nie przyszedł, bo był chory."],["Следствие","Dlatego показывает результат: Był chory, dlatego został w domu."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-review','relationships-emotions','review','Rozmowa po konflikcie','Извинение и примирение','7 карточек · A2','Повтори фразы для спокойного разговора',7,'🔄',80,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-quiz','relationships-emotions','quiz','Quiz: relacje i emocje','Проверка темы','8 вопросов · A2','Проверь лексику и причинные союзы',6,'🎯',81,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-reading-check','relationships-emotions','quiz','Czy rozumiesz rozmowę?','Понимание текста','5 вопросов · A2','Проверь детали истории Марты и Ани',5,'📖',82,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}')
on conflict (id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata;

insert into public.flashcards (id, polish, translation, example, position, is_active, source_metadata) values
('rel-relacja','relacja','отношения','Mamy dobrą relację i często rozmawiamy.',271,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-przyjazn','przyjaźń','дружба','Nasza przyjaźń jest dla mnie ważna.',272,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-zaufanie','zaufanie','доверие','Zaufanie buduje się przez szczere rozmowy.',273,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-wsparcie','wsparcie','поддержка','Dziękuję ci za wsparcie w trudnym tygodniu.',274,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-szczery','szczery','искренний','Chcę być z tobą szczery.',275,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-dumny','dumny','гордый','Jestem dumny, że zdałeś egzamin.',276,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-zmartwiony','zmartwiony','обеспокоенный','Ola jest zmartwiona, bo przyjaciel nie odpowiada.',277,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-zazdrosny','zazdrosny','ревнивый; завистливый','Nie chcę być zazdrosny o jej sukces.',278,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-klocic','kłócić się','ссориться','Nie warto kłócić się o drobiazgi.',279,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-pogodzic','pogodzić się','помириться','Po rozmowie szybko się pogodzili.',280,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-przeprosic','przeprosić','извиниться','Powinienem przeprosić za swoje słowa.',281,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-wybaczyc','wybaczyć','простить','Trudno wybaczyć bez szczerej rozmowy.',282,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-tesknic','tęsknić za','скучать по','Tęsknię za rodziną, dlatego często dzwonię.',283,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-cieszyc','cieszyć się','радоваться','Cieszę się, że możemy się spotkać.',284,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('rel-rozczarowany','rozczarowany','разочарованный','Byłam rozczarowana, bo zmieniłeś plany.',285,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}')
on conflict (id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('rel-words','rel-review');
insert into public.lesson_flashcards (lesson_id, flashcard_id, position) values
('rel-words','rel-relacja',0),('rel-words','rel-przyjazn',1),('rel-words','rel-zaufanie',2),('rel-words','rel-wsparcie',3),('rel-words','rel-szczery',4),('rel-words','rel-dumny',5),('rel-words','rel-zmartwiony',6),('rel-words','rel-zazdrosny',7),
('rel-review','rel-klocic',0),('rel-review','rel-pogodzic',1),('rel-review','rel-przeprosic',2),('rel-review','rel-wybaczyc',3),('rel-review','rel-tesknic',4),('rel-review','rel-cieszyc',5),('rel-review','rel-rozczarowany',6);

delete from public.questions where lesson_id in ('rel-grammar','rel-quiz','rel-reading-check');
insert into public.questions (lesson_id,prompt,options,correct,explanation,position) values
('rel-grammar','Cieszę się, ___ możemy porozmawiać.','["że","bo że","dlatego"]',0,'Że вводит содержание чувства или мнения: cieszę się, że…',0),
('rel-grammar','Ola jest zmartwiona, ___ Marek nie odpowiada.','["bo","że dlatego","ale że"]',0,'Bo вводит причину и соединяет её с главным предложением.',1),
('rel-grammar','Я звоню, потому что скучаю.','["Dzwonię, bo tęsknię.","Dzwonię, że tęsknię.","Dlatego że dzwonię tęsknię."]',0,'После действия причину удобно вводить союзом bo.',2),
('rel-grammar','Составьте: Я рад, что мы помирились.','["Cieszę się, że się pogodziliśmy.","Cieszę, bo my pogodzić się.","Jestem że pogodziliśmy cieszę."]',0,'После cieszę się содержание эмоции вводится через że.',3),
('rel-grammar','Nie miał czasu, ___ napisał krótką wiadomość.','["dlatego","dlatego że","że"]',0,'Dlatego начинает следствие: времени не было, поэтому он написал короткое сообщение.',4),
('rel-quiz','Что означает zaufanie?','["доверие","ссора","встреча"]',0,'Zaufanie — доверие между людьми.',0),
('rel-quiz','Jestem dumny, ___ zdałeś egzamin.','["że","bo dlatego","dlatego że"]',0,'Że вводит факт, который вызывает гордость.',1),
('rel-quiz','Почему она обеспокоена?','["Dlaczego ona jest zmartwiona?","Że ona jest szczera?","Dlatego ona wybaczyć?"]',0,'Dlaczego задаёт вопрос о причине.',2),
('rel-quiz','Nie przyszedł, ___ był chory.','["bo","że","dlatego"]',0,'Bo вводит причину отсутствия.',3),
('rel-quiz','Как сказать «Мы помирились»?','["Pogodziliśmy się.","Kłócimy ich.","Wybaczyli nas."]',0,'Pogodzić się — помириться; в прошедшем времени: pogodziliśmy się.',4),
('rel-quiz','Tęsknię za rodziną, ___ często dzwonię.','["dlatego","że bo","ponieważ że"]',0,'Dlatego соединяет причину с её следствием.',5),
('rel-quiz','Что лучше сказать после обидных слов?','["Przepraszam, nie chciałem cię zranić.","Jestem zazdrosny, dlatego milcz.","Nie wolno mi wybaczyć."]',0,'Конкретное искреннее извинение помогает восстановить разговор.',6),
('rel-quiz','Była ___, bo przyjaciółka odwołała spotkanie.','["rozczarowana","rozczarowany","rozczarowane"]',0,'Форма женского рода: rozczarowana.',7),
('rel-reading-check','Dlaczego Marta była rozczarowana?','["Ania odwołała spotkanie bez wyjaśnienia","Marta nie zdała egzaminu","Telefon Marty się zepsuł"]',0,'Марта ждала встречи, но Аня её отменила без объяснения.',0),
('rel-reading-check','Co Ania napisała w wiadomości?','["Że miała trudny dzień i przeprasza","Że nie chce już rozmawiać","Że wyjeżdża na rok"]',0,'Аня объяснила ситуацию и извинилась.',1),
('rel-reading-check','Dlaczego Marta nie odpowiedziała od razu?','["Potrzebowała czasu, żeby się uspokoić","Nie znała numeru Ani","Była w aptece"]',0,'Марте понадобилось время, чтобы успокоиться.',2),
('rel-reading-check','Co pomogło przyjaciółkom się pogodzić?','["Szczera rozmowa","Nowy prezent","Wspólny egzamin"]',0,'Помириться помогла открытая беседа.',3),
('rel-reading-check','Czego nauczyły się Marta i Ania?','["Że warto mówić o emocjach i słuchać","Że lepiej zawsze milczeć","Że przyjaźń nie wymaga zaufania"]',0,'Они поняли ценность разговора об эмоциях и внимательного слушания.',4);

insert into public.reading_texts (id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('szczera-rozmowa-marty-i-ani','relationships-emotions','Szczera rozmowa Marty i Ani','Недопонимание, извинение и восстановление дружбы','A2',6,'💬',
'["Marta i Ania przyjaźnią się od kilku lat. W piątek miały spotkać się w kawiarni, ale Ania nagle odwołała spotkanie i niczego nie wyjaśniła. Marta była rozczarowana, bo długo czekała na ten wieczór. Pomyślała też, że przyjaciółka nie szanuje jej czasu.","Następnego dnia Ania napisała, że miała bardzo trudny dzień w pracy. Przeprosiła i przyznała, że powinna była wcześniej wszystko wyjaśnić. Marta nadal była zmartwiona, dlatego nie odpowiedziała od razu. Potrzebowała chwili, żeby się uspokoić.","Wieczorem przyjaciółki spokojnie porozmawiały. Marta powiedziała szczerze, co poczuła, a Ania uważnie jej wysłuchała. Obie zrozumiały, że nie chciały się zranić. Pogodziły się i umówiły na nowy termin. Cieszyły się, że szczera rozmowa odbudowała ich zaufanie."]',
'{"przyjaźnią":{"lemma":"przyjaźnić się","translation":"дружить","part_of_speech":"глагол"},"odwołała":{"lemma":"odwołać","translation":"отменить","part_of_speech":"глагол"},"rozczarowana":{"lemma":"rozczarowany","translation":"разочарованная","part_of_speech":"прилагательное"},"szanuje":{"lemma":"szanować","translation":"уважать","part_of_speech":"глагол"},"przyznała":{"lemma":"przyznać","translation":"признать","part_of_speech":"глагол"},"uspokoić":{"lemma":"uspokoić się","translation":"успокоиться","part_of_speech":"глагол"},"poczuła":{"lemma":"poczuć","translation":"почувствовать","part_of_speech":"глагол"},"wysłuchała":{"lemma":"wysłuchać","translation":"выслушать","part_of_speech":"глагол"},"zranić":{"lemma":"zranić","translation":"обидеть; ранить","part_of_speech":"глагол"},"odbudowała":{"lemma":"odbudować","translation":"восстановить","part_of_speech":"глагол"}}',
'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29","comprehension_lesson_id":"rel-reading-check"}',18,true)
on conflict (id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
