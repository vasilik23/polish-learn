-- Sixth original A1 vertical block: food and shopping. Existing RLS/grants remain unchanged.
update public.topics set position=6 where course_id='a1-foundations' and position=5;
insert into public.topics(id,course_id,title,description,emoji,position,is_active) values
('food-shopping','a1-foundations','Еда и магазин','Покупаем продукты, спрашиваем цену и делаем простой заказ','🛒',5,true)
on conflict(id) do update set title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,theory_title,theory_sections,source_metadata,position,is_active) values
('food-words','food-shopping','words','Jedzenie','Еда и напитки','8 карточек · A1','Назови базовые продукты',7,'🍎','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',20,true),
('food-grammar','food-shopping','grammar','Poproszę…','Заказ и покупка','5 заданий · A1','Используй винительный падеж и количества',8,'✏️','Poproszę kawę — kupuję chleb','[["Вежливый заказ","Proszę или poproszę + предмет: Proszę wodę. Poproszę kawę."],["Винительный падеж","После kupuję/proszę женское -a обычно меняется на -ę: kawa → kawę, woda → wodę. Мужской неодушевлённый часто не меняется: chleb."],["Количество","После litr, kilogram и gram форма меняется: litr mleka, kilogram jabłek, dwieście gramów sera."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',21,true),
('food-review','food-shopping','review','W sklepie','В магазине','7 карточек · A1','Спроси цену и собери покупки',6,'🔄','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',22,true),
('food-quiz','food-shopping','quiz','Quiz: zakupy','Проверка темы','8 вопросов · A1','Проверь продукты, заказ и цены',5,'🎯','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',23,true)
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('jedzenie','jedzenie','еда','Kupuję jedzenie na kolację.',75,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('chleb','chleb','хлеб','Proszę jeden chleb.',76,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('bulka','bułka','булочка','Kupuję świeżą bułkę.',77,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('mleko','mleko','молоко','Proszę litr mleka.',78,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('woda','woda','вода','Piję wodę mineralną.',79,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('kawa','kawa','кофе','Poproszę kawę bez cukru.',80,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('ser','ser','сыр','Czy macie żółty ser?',81,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('jablko','jabłko','яблоко','Biorę dwa jabłka.',82,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('warzywa','warzywa','овощи','Kupujemy świeże warzywa.',83,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('owoce','owoce','фрукты','Lubię polskie owoce.',84,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('sklep','sklep','магазин','Sklep jest obok domu.',85,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('kupowac','kupować','покупать','Często kupuję tutaj chleb.',86,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('prosze','proszę','пожалуйста; прошу','Proszę wodę i kawę.',87,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('ile-kosztuje','ile kosztuje?','сколько стоит?','Ile kosztuje ta bułka?',88,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}'),
('kilogram','kilogram','килограмм','Proszę kilogram jabłek.',89,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('food-words','food-review');
insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('food-words','jedzenie',0),('food-words','chleb',1),('food-words','bulka',2),('food-words','mleko',3),('food-words','woda',4),('food-words','kawa',5),('food-words','ser',6),('food-words','jablko',7),
('food-review','warzywa',0),('food-review','owoce',1),('food-review','sklep',2),('food-review','kupowac',3),('food-review','prosze',4),('food-review','ile-kosztuje',5),('food-review','kilogram',6);

delete from public.questions where lesson_id in ('food-grammar','food-quiz');
insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('food-grammar','Proszę ___ wodę.','["zimna","zimną","zimnej"]',1,'После proszę предмет — в винительном падеже: zimną wodę.',0),
('food-grammar','Kupuję ___.','["kawa","kawę","kawy"]',1,'Женские существительные на -a обычно получают -ę: kawę.',1),
('food-grammar','Poproszę ___.','["chleb","chleba","chlebem"]',0,'У неодушевлённых существительных мужского рода форма часто не меняется: chleb.',2),
('food-grammar','Proszę litr ___.','["mleko","mleka","mlekiem"]',1,'После единицы количества употребляем родительный: litr mleka.',3),
('food-grammar','Как вежливо спросить цену?','["Ile kosztuje?","Jaki koszt?","Gdzie płaci?"]',0,'Ile kosztuje? — нейтральный вопрос «Сколько стоит?».',4),
('food-quiz','Выберите «булочка».','["bułka","butelka","woda"]',0,'Bułka — булочка.',0),
('food-quiz','Kupuję ___.','["kawę","kawa","kawie"]',0,'После kupuję нужна форма kawę.',1),
('food-quiz','Как заказать воду?','["Proszę wodę.","Proszę woda.","Jest wodą."]',0,'В заказе естественно: Proszę wodę.',2),
('food-quiz','Ile ___ ta kawa?','["kosztuje","kupuje","proszę"]',0,'О цене спрашиваем Ile kosztuje…?',3),
('food-quiz','Что означает owoce?','["фрукты","овощи","напитки"]',0,'Owoce — фрукты.',4),
('food-quiz','Proszę kilogram ___.','["jabłka","jabłek","jabłko"]',1,'После kilogram нужна форма jabłek.',5),
('food-quiz','Где покупают продукты?','["w sklepie","w sypialni","na balkonie"]',0,'Sklep — магазин.',6),
('food-quiz','Выберите естественный заказ.','["Poproszę kawę bez cukru.","Poproszę kawa bez cukier.","Kawę jest proszę."]',0,'Poproszę + винительный падеж — вежливая формула заказа.',7);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('zakupy-oli','food-shopping','Zakupy Oli','Оля покупает продукты к завтраку','A1',4,'🛒','["W sobotę rano Ola idzie do małego sklepu obok domu. Chce kupić jedzenie na śniadanie. Ma krótką listę: chleb, mleko, ser, jabłka i kawa.","W sklepie Ola mówi: „Dzień dobry. Proszę jeden chleb, litr mleka i dwieście gramów sera”. Potem wybiera cztery czerwone jabłka. Pyta też: „Ile kosztuje kawa?”.","Sprzedawczyni podaje cenę. Ola płaci kartą i pakuje zakupy do torby. Na koniec mówi: „Dziękuję, do widzenia”. W domu robi kawę i kanapki ze świeżym serem."]','{"idzie":{"lemma":"iść","translation":"идти","part_of_speech":"глагол"},"chce":{"lemma":"chcieć","translation":"хотеть","part_of_speech":"глагол"},"kupić":{"lemma":"kupić","translation":"купить","part_of_speech":"глагол"},"krótką":{"lemma":"krótki","translation":"короткий","part_of_speech":"прилагательное"},"dwieście":{"lemma":"dwieście","translation":"двести","part_of_speech":"числительное"},"gramów":{"lemma":"gram","translation":"грамм","part_of_speech":"существительное"},"wybiera":{"lemma":"wybierać","translation":"выбирать","part_of_speech":"глагол"},"pyta":{"lemma":"pytać","translation":"спрашивать","part_of_speech":"глагол"},"sprzedawczyni":{"lemma":"sprzedawczyni","translation":"продавщица","part_of_speech":"существительное"},"podaje":{"lemma":"podawać","translation":"сообщать; подавать","part_of_speech":"глагол"},"płaci":{"lemma":"płacić","translation":"платить","part_of_speech":"глагол"},"pakuje":{"lemma":"pakować","translation":"упаковывать","part_of_speech":"глагол"},"zakupy":{"lemma":"zakupy","translation":"покупки","part_of_speech":"существительное"},"torby":{"lemma":"torba","translation":"сумка","part_of_speech":"существительное"},"świeżym":{"lemma":"świeży","translation":"свежий","part_of_speech":"прилагательное"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-27"}',5,true)
on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
