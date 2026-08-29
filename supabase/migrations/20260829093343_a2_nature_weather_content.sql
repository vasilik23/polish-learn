insert into public.topics(id,course_id,title,description,emoji,position,is_active) values
('weather-nature','a2-independence','Природа и погода','Обсуждаем прогноз, безопасность и заботу о природе','🌦️',9,true)
on conflict(id) do update set course_id=excluded.course_id,title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,position,is_active,theory_title,theory_sections,source_metadata) values
('weather-words','weather-nature','words','Pogoda wokół nas','Погода','8 карточек · A2','Опиши прогноз и погодные явления',8,'🌦️',93,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-grammar','weather-nature','grammar','Trzeba czy można?','Необходимость и возможность','5 заданий · A2','Говори о правилах, советах и вероятности',9,'✏️',94,true,'Необходимость, совет, запрет и возможность','[["Необходимость","Trzeba/należy + инфинитив: Trzeba zabrać wodę."],["Совет и запрет","Warto советует, а nie wolno запрещает действие."],["Возможность","Można говорит о доступной возможности, а może — о вероятности."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-review','weather-nature','review','Dbamy o przyrodę','Природа и экология','7 карточек · A2','Повтори действия для защиты природы',7,'🌿',95,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-quiz','weather-nature','quiz','Quiz: natura i pogoda','Проверка темы','8 вопросов · A2','Проверь лексику и конструкции темы',6,'🎯',96,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-reading-check','weather-nature','quiz','Czy rozumiesz wycieczkę?','Понимание текста','5 вопросов · A2','Проверь детали поездки Лены и Кубы',5,'📖',97,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}')
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('weather-prognoza','prognoza pogody','прогноз погоды','Sprawdzam prognozę pogody przed wycieczką.',316,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-temperatura','temperatura','температура','Temperatura spadnie dziś w nocy.',317,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-upal','upał','жара','Podczas upału trzeba pić dużo wody.',318,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-mroz','mróz','мороз','Rano był silny mróz.',319,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-burza','burza','гроза','Nad miastem zbliża się burza.',320,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-wiatr','wiatr','ветер','Silny wiatr łamie gałęzie.',321,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-chmura','chmura','облако','Ciemne chmury zapowiadają deszcz.',322,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-tecza','tęcza','радуга','Po deszczu pojawiła się tęcza.',323,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-srodowisko','środowisko','окружающая среда','Warto dbać o środowisko.',324,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-segregowac','segregować odpady','сортировать отходы','W domu segregujemy odpady.',325,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-oszczedzac','oszczędzać wodę','экономить воду','Należy oszczędzać wodę podczas suszy.',326,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-zanieczyszczenie','zanieczyszczenie','загрязнение','Zanieczyszczenie powietrza szkodzi zdrowiu.',327,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-szlak','szlak','туристический маршрут','Ten szlak prowadzi przez las.',328,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-krajobraz','krajobraz','пейзаж','Ze szczytu widać piękny krajobraz.',329,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('weather-chronić','chronić przyrodę','защищать природу','Musimy chronić przyrodę w parku narodowym.',330,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('weather-words','weather-review');
insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('weather-words','weather-prognoza',0),('weather-words','weather-temperatura',1),('weather-words','weather-upal',2),('weather-words','weather-mroz',3),('weather-words','weather-burza',4),('weather-words','weather-wiatr',5),('weather-words','weather-chmura',6),('weather-words','weather-tecza',7),
('weather-review','weather-srodowisko',0),('weather-review','weather-segregowac',1),('weather-review','weather-oszczedzac',2),('weather-review','weather-zanieczyszczenie',3),('weather-review','weather-szlak',4),('weather-review','weather-krajobraz',5),('weather-review','weather-chronić',6);

delete from public.questions where lesson_id in ('weather-grammar','weather-quiz','weather-reading-check');
insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('weather-grammar','Kiedy jest upał, ___ pić dużo wody.','["trzeba","może","wolno"]',0,'Trzeba + инфинитив выражает общую необходимость.',0),
('weather-grammar','Przed wycieczką ___ sprawdzić prognozę.','["warto","nie wolno","udało się"]',0,'Warto + инфинитив означает полезную рекомендацию.',1),
('weather-grammar','W rezerwacie nie ___ schodzić ze szlaku.','["wolno","trzeba","warto"]',0,'Nie wolno + инфинитив выражает запрет.',2),
('weather-grammar','Jutro ___ padać, więc zabierz parasol.','["może","musi","należy"]',0,'Może + инфинитив сообщает о возможности или вероятности.',3),
('weather-grammar','Составьте: Во время засухи необходимо экономить воду.','["Podczas suszy należy oszczędzać wodę.","Podczas suszy może oszczędza wodę.","Suszę należy woda oszczędzać."]',0,'Należy + инфинитив выражает безличную необходимость; podczas требует родительного падежа.',4),
('weather-quiz','Что означает prognoza pogody?','["прогноз погоды","температура воды","горный маршрут"]',0,'Prognoza pogody сообщает об ожидаемой погоде.',0),
('weather-quiz','Po burzy na niebie może pojawić się ___.','["tęcza","mróz","upał"]',0,'После дождя и грозы иногда появляется радуга.',1),
('weather-quiz','Как сказать «сортировать отходы»?','["segregować odpady","chronić krajobraz","oszczędzać wiatr"]',0,'Segregować odpady — разделять мусор по видам.',2),
('weather-quiz','W parku narodowym nie ___ hałasować.','["wolno","warto","może"]',0,'Nie wolno выражает запрет.',3),
('weather-quiz','Что может вредить воздуху?','["zanieczyszczenie","tęcza","szlak"]',0,'Zanieczyszczenie — загрязнение среды.',4),
('weather-quiz','Silny ___ może łamać gałęzie.','["wiatr","krajobraz","mróz"]',0,'Сильный ветер может ломать ветки.',5),
('weather-quiz','Как дать мягкий совет проверить прогноз?','["Warto sprawdzić prognozę.","Nie wolno prognoza.","Prognoza trzeba sprawdziła."]',0,'Warto + инфинитив — мягкая рекомендация.',6),
('weather-quiz','Ten ___ prowadzi na szczyt góry.','["szlak","upał","odpad"]',0,'Szlak — обозначенный туристический маршрут.',7),
('weather-reading-check','Dokąd pojechali Lena i Kuba?','["Do parku narodowego","Nad morze","Do centrum handlowego"]',0,'Они отправились в национальный парк.',0),
('weather-reading-check','Co zapowiadała prognoza?','["Słońce rano i burzę po południu","Mróz przez cały dzień","Silny śnieg rano"]',0,'Утром ожидалось солнце, а после обеда — гроза.',1),
('weather-reading-check','Dlaczego zmienili trasę?','["Nadchodziła burza","Zgubili mapę","Szlak był zamknięty od rana"]',0,'Они увидели тёмные облака и услышали гром.',2),
('weather-reading-check','Co zrobili z butelką?','["Wrzucili ją do odpowiedniego pojemnika","Zostawili ją w lesie","Wyrzucili ją do rzeki"]',0,'Бутылку отсортировали в подходящий контейнер.',3),
('weather-reading-check','Co zobaczyli po deszczu?','["Tęczę nad lasem","Śnieg na szlaku","Pożar w parku"]',0,'После дождя над лесом появилась радуга.',4);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('weather-wycieczka-przed-burza','weather-nature','Wycieczka przed burzą','Прогноз, безопасный маршрут и забота о природе','A2',6,'🌦️',
'["W sobotę Lena i Kuba pojechali do parku narodowego. Prognoza pogody zapowiadała słońce rano, ale po południu mogła nadejść burza. Dlatego zabrali lekkie kurtki, wodę i mapę. Przed wejściem na szlak przeczytali też zasady dla turystów.","Na początku było ciepło i bezwietrznie. Ze wzgórza podziwiali zielony krajobraz, lecz później zobaczyli ciemne chmury i usłyszeli grzmot. Uznali, że nie należy iść dalej. Mogli wrócić krótszą trasą, więc spokojnie zeszli do schroniska przed silnym deszczem.","Po drodze znaleźli pustą plastikową butelkę. Zabrali ją i wrzucili do odpowiedniego pojemnika obok parkingu, ponieważ warto segregować odpady i chronić przyrodę. Gdy deszcz się skończył, nad lasem pojawiła się tęcza. Wycieczka była krótsza, ale bezpieczna i udana."]',
'{"zapowiadała":{"lemma":"zapowiadać","translation":"предвещать; прогнозировать","part_of_speech":"глагол"},"nadejść":{"lemma":"nadejść","translation":"наступить; приблизиться","part_of_speech":"глагол"},"szlak":{"lemma":"szlak","translation":"туристический маршрут","part_of_speech":"существительное"},"bezwietrznie":{"lemma":"bezwietrznie","translation":"безветренно","part_of_speech":"наречие"},"wzgórza":{"lemma":"wzgórze","translation":"холм","part_of_speech":"существительное"},"krajobraz":{"lemma":"krajobraz","translation":"пейзаж","part_of_speech":"существительное"},"grzmot":{"lemma":"grzmot","translation":"гром","part_of_speech":"существительное"},"schroniska":{"lemma":"schronisko","translation":"туристический приют","part_of_speech":"существительное"},"pojemnika":{"lemma":"pojemnik","translation":"контейнер","part_of_speech":"существительное"},"chronić":{"lemma":"chronić","translation":"защищать","part_of_speech":"глагол"}}',
'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29","comprehension_lesson_id":"weather-reading-check"}',21,true)
on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
