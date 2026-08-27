-- Fifth original A1 vertical block: home. Existing RLS/grants remain unchanged.
update public.topics set position=5 where course_id='a1-foundations' and position=4;
insert into public.topics(id,course_id,title,description,emoji,position,is_active) values ('home','a1-foundations','Дом','Называем комнаты и описываем расположение предметов','🏠',4,true)
on conflict(id) do update set title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,theory_title,theory_sections,source_metadata,position,is_active) values
('home-words','home','words','Mój dom','Комнаты и дом','8 карточек · A1','Назови помещения в доме',7,'🏠','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',16,true),
('home-grammar','home','grammar','Gdzie to jest?','Где находится?','5 заданий · A1','Используй jest/są и w/na',8,'✏️','Gdzie? — w domu, na stole','[["Jest или są","Jest użyваем с одним предметом: W pokoju jest stół. Są — с несколькими: W pokoju są krzesła."],["Внутри: w","На вопрос gdzie? говорим: w domu, w pokoju, w kuchni, w łazience, w szafie."],["На поверхности: na","Na stole, na łóżku, na balkonie. После w/na форма существительного меняется."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',17,true),
('home-review','home','review','W pokoju','Мебель и предметы','7 карточек · A1','Закрепи предметы и их расположение',6,'🔄','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',18,true),
('home-quiz','home','quiz','Quiz: dom','Проверка темы','8 вопросов · A1','Проверь комнаты, мебель и местонахождение',5,'🎯','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',19,true)
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('mieszkanie','mieszkanie','квартира','Moje mieszkanie jest małe, ale jasne.',60,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('dom','dom','дом','Mieszkamy w domu pod Warszawą.',61,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('pokoj','pokój','комната','W pokoju jest duże okno.',62,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('kuchnia','kuchnia','кухня','W kuchni gotujemy obiad.',63,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('lazienka','łazienka','ванная','Łazienka jest obok sypialni.',64,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('sypialnia','sypialnia','спальня','W sypialni stoi łóżko.',65,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('salon','salon','гостиная','W salonie odpoczywamy razem.',66,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('balkon','balkon','балкон','Na balkonie są kwiaty.',67,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('stol','stół','стол','Na stole jest lampa.',68,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('krzeslo','krzesło','стул','Krzesło stoi przy stole.',69,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('lozko','łóżko','кровать','Kot śpi na łóżku.',70,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('szafa','szafa','шкаф','Ubrania są w szafie.',71,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('okno','okno','окно','Przy oknie stoi biurko.',72,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('drzwi','drzwi','дверь','Drzwi do kuchni są otwarte.',73,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('gdzie','gdzie?','где?','Gdzie jest klucz?',74,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('home-words','home-review');
insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('home-words','mieszkanie',0),('home-words','dom',1),('home-words','pokoj',2),('home-words','kuchnia',3),('home-words','lazienka',4),('home-words','sypialnia',5),('home-words','salon',6),('home-words','balkon',7),
('home-review','stol',0),('home-review','krzeslo',1),('home-review','lozko',2),('home-review','szafa',3),('home-review','okno',4),('home-review','drzwi',5),('home-review','gdzie',6);

delete from public.questions where lesson_id in ('home-grammar','home-quiz');
insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('home-grammar','___ kuchni jest stół.','["W","Na","Do"]',0,'Для положения внутри кухни используем w: w kuchni.',0),
('home-grammar','Książka leży ___ stole.','["w","na","do"]',1,'На поверхности — na + miejscownik: na stole.',1),
('home-grammar','W salonie ___ sofa.','["jest","są","mam"]',0,'С одним предметом употребляется jest.',2),
('home-grammar','W sypialni ___ dwa okna.','["jest","są","to"]',1,'С несколькими предметами употребляется są.',3),
('home-grammar','Как спросить «Где ванная?»','["Gdzie jest łazienka?","Co łazienka jest?","Dokąd łazienkę?"]',0,'О местонахождении спрашиваем Gdzie jest…?',4),
('home-quiz','Где обычно готовят?','["w kuchni","w sypialni","na balkonie"]',0,'Kuchnia — кухня.',0),
('home-quiz','Выберите «на балконе».','["w balkonu","na balkonie","do balkon"]',1,'Устойчиво: na balkonie.',1),
('home-quiz','W pokoju ___ trzy krzesła.','["jest","są","ma"]',1,'Три стула — множественное число, поэтому są.',2),
('home-quiz','Что означает szafa?','["шкаф","стол","окно"]',0,'Szafa — шкаф.',3),
('home-quiz','Ubrania są ___ szafie.','["w","na","z"]',0,'Одежда находится внутри шкафа: w szafie.',4),
('home-quiz','Выберите правильное описание.','["Na stole jest lampa.","W stole są lampa.","Do stół jest lampa."]',0,'Предмет на поверхности: na stole.',5),
('home-quiz','Как спросить о ключе?','["Gdzie jest klucz?","Jaki jest gdzie klucz?","Czy gdzie klucza?"]',0,'Gdzie jest…? — где находится…?',6),
('home-quiz','Где спят?','["w sypialni","w kuchni","na stole"]',0,'Sypialnia — спальня.',7);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('nowe-mieszkanie-marty','home','Nowe mieszkanie Marty','Марта показывает друзьям новую квартиру','A1',4,'🏠','["Marta mieszka teraz w nowym mieszkaniu. Mieszkanie jest na drugim piętrze i ma trzy pokoje. Przy wejściu jest mały przedpokój, a obok niego jasna kuchnia.","W salonie stoją sofa, stół i cztery krzesła. Na stole leżą książki. Przy oknie jest zielona roślina. Z salonu można wyjść na balkon.","Sypialnia Marty jest spokojna. W sypialni stoi łóżko i duża szafa. Naprzeciwko jest łazienka. Marta lubi swoje mieszkanie, bo wszystko ma tutaj swoje miejsce."]','{"nowym":{"lemma":"nowy","translation":"новый","part_of_speech":"прилагательное"},"piętrze":{"lemma":"piętro","translation":"этаж","part_of_speech":"существительное"},"wejściu":{"lemma":"wejście","translation":"вход","part_of_speech":"существительное"},"przedpokój":{"lemma":"przedpokój","translation":"прихожая","part_of_speech":"существительное"},"stoją":{"lemma":"stać","translation":"стоять","part_of_speech":"глагол"},"leżą":{"lemma":"leżeć","translation":"лежать","part_of_speech":"глагол"},"roślina":{"lemma":"roślina","translation":"растение","part_of_speech":"существительное"},"wyjść":{"lemma":"wyjść","translation":"выйти","part_of_speech":"глагол"},"spokojna":{"lemma":"spokojny","translation":"спокойный","part_of_speech":"прилагательное"},"naprzeciwko":{"lemma":"naprzeciwko","translation":"напротив","part_of_speech":"наречие"},"wszystko":{"lemma":"wszystko","translation":"всё","part_of_speech":"местоимение"},"miejsce":{"lemma":"miejsce","translation":"место","part_of_speech":"существительное"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',4,true)
on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
