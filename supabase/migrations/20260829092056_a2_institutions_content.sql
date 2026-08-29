insert into public.topics(id,course_id,title,description,emoji,position,is_active) values
('institutions','a2-independence','Учреждения','Заполняем форму и вежливо решаем вопрос в учреждении','🏛️',8,true)
on conflict(id) do update set course_id=excluded.course_id,title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,position,is_active,theory_title,theory_sections,source_metadata) values
('office-words','institutions','words','W urzędzie','Документы и форма','8 карточек · A2','Назови части заявления и необходимые документы',8,'🏛️',88,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-grammar','institutions','grammar','Uprzejmie i konkretnie','Формальный регистр и даты','5 заданий · A2','Проси вежливо и правильно называй сроки',9,'✏️',89,true,'Вежливые просьбы, инструкции и даты','[["Вежливая просьба","Chciałbym/chciałabym… и Czy może pan/pani… смягчают официальный вопрос."],["Инструкция","Proszę + инфинитив: Proszę podpisać formularz."],["Срок и дата","Do + родительный задаёт крайний срок: do piętnastego maja."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-review','institutions','review','Od wniosku do odbioru','Подача и получение','7 карточек · A2','Повтори действия и статусы обращения',7,'🔄',90,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-quiz','institutions','quiz','Quiz: w urzędzie','Проверка темы','8 вопросов · A2','Проверь лексику, даты и вежливые просьбы',6,'🎯',91,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-reading-check','institutions','quiz','Czy rozumiesz procedurę?','Понимание текста','5 вопросов · A2','Проверь детали визита Наталии',5,'📖',92,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}')
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('office-urzad','urząd','государственное учреждение','Jutro idę do urzędu miasta.',301,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-wniosek','wniosek','заявление','Wniosek można złożyć przez internet.',302,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-formularz','formularz','бланк; форма','Proszę wypełnić ten formularz.',303,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-dokument','dokument tożsamości','документ, удостоверяющий личность','Trzeba okazać dokument tożsamości.',304,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-rubryka','rubryka','поле формы','W tej rubryce wpisuje się adres.',305,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-podpis','podpis','подпись','Na końcu potrzebny jest czytelny podpis.',306,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-zalacznik','załącznik','приложение к документу','Do wniosku brakuje jednego załącznika.',307,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-termin','termin','срок; назначенное время','Najbliższy wolny termin jest w środę.',308,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-zlozyc','złożyć wniosek','подать заявление','Chciałbym złożyć wniosek o kartę mieszkańca.',309,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-odebrac','odebrać dokument','получить готовый документ','Dokument będzie można odebrać za tydzień.',310,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-potwierdzenie','potwierdzenie','подтверждение','Proszę zachować potwierdzenie złożenia wniosku.',311,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-numer','numer sprawy','номер дела','Numer sprawy znajduje się na potwierdzeniu.',312,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-dane','dane osobowe','персональные данные','Proszę sprawdzić, czy dane osobowe są poprawne.',313,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-wazny','ważny','действительный','Paszport jest ważny do przyszłego roku.',314,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}'),
('office-brakowac','brakować','не хватать','W formularzu brakuje daty urodzenia.',315,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('office-words','office-review');
insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('office-words','office-urzad',0),('office-words','office-wniosek',1),('office-words','office-formularz',2),('office-words','office-dokument',3),('office-words','office-rubryka',4),('office-words','office-podpis',5),('office-words','office-zalacznik',6),('office-words','office-termin',7),
('office-review','office-zlozyc',0),('office-review','office-odebrac',1),('office-review','office-potwierdzenie',2),('office-review','office-numer',3),('office-review','office-dane',4),('office-review','office-wazny',5),('office-review','office-brakowac',6);

delete from public.questions where lesson_id in ('office-grammar','office-quiz','office-reading-check');
insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('office-grammar','Как вежливо сказать «Я хотел бы подать заявление»?','["Chciałbym złożyć wniosek.","Chcę wniosek dawaj.","Złożyłem by formularz."]',0,'Chciałbym/chciałabym — стандартная вежливая форма просьбы.',0),
('office-grammar','___ mi powiedzieć, gdzie jest pokój numer pięć?','["Czy może pani","Pani musi","Czy pani daj"]',0,'Czy może pani…? — нейтральная официальная просьба.',1),
('office-grammar','Data 12.03.2026 to:','["dwunasty marca dwa tysiące dwudziestego szóstego roku","dwanaście marzec dwa tysiące dwadzieścia sześć","dwunasta marcem dwa tysiące szósty"]',0,'В датах день — порядковое числительное, месяц обычно в родительном падеже.',2),
('office-grammar','Составьте: Пожалуйста, подпишите форму здесь.','["Proszę podpisać formularz tutaj.","Proszę podpisuje tutaj formularzem.","Tutaj proszę formularz podpisany."]',0,'Формальная инструкция строится как proszę + инфинитив.',3),
('office-grammar','Wniosek należy złożyć do ___ maja.','["piętnastego","piętnaście","piętnasty"]',0,'После do в обозначении срока используется родительный: do piętnastego maja.',4),
('office-quiz','Что означает załącznik?','["приложение к документу","очередь","подпись"]',0,'Załącznik — дополнительный документ, приложенный к заявлению.',0),
('office-quiz','Gdzie wpisuje się adres?','["w odpowiedniej rubryce","na bilecie","w recepcie"]',0,'Rubryka — отдельное поле формы.',1),
('office-quiz','Как вежливо попросить повторить?','["Czy może pan powtórzyć?","Powtarzaj natychmiast.","Pan powtórzyłby jest."]',0,'Czy może pan…? сохраняет нейтральный официальный тон.',2),
('office-quiz','Dokument można odebrać ___ 20 kwietnia.','["od","o","do"]',0,'Od + дата обозначает начало доступного периода.',3),
('office-quiz','Что подтверждает подачу заявления?','["potwierdzenie złożenia wniosku","numer pokoju","ważny paszport"]',0,'После подачи выдают или отправляют подтверждение.',4),
('office-quiz','В форме не хватает подписи.','["W formularzu brakuje podpisu.","Formularz podpis jest brak.","Podpis brakuje formularzem."]',0,'Brakować требует родительного: brakuje podpisu.',5),
('office-quiz','Termin wizyty jest ___ 8 maja.','["na","w","z"]',0,'Назначенный срок оформляется: termin na + дата.',6),
('office-quiz','Что нужно проверить перед подачей?','["czy dane są poprawne","czy film jest ciekawy","czy pogoda się zmieni"]',0,'В заявлении важно проверить корректность данных.',7),
('office-reading-check','Po co Natalia przyszła do urzędu?','["Złożyć wniosek o kartę mieszkańca","Odebrać receptę","Kupić bilet"]',0,'Наталия пришла подать заявление на карту жителя.',0),
('office-reading-check','Czego brakowało w formularzu?','["Daty urodzenia","Adresu urzędu","Numeru pokoju"]',0,'Сотрудница заметила отсутствие даты рождения.',1),
('office-reading-check','Jaki dokument Natalia okazała?','["Paszport","Bilet miesięczny","Legitymację biblioteczną"]',0,'Для подтверждения личности Наталия показала паспорт.',2),
('office-reading-check','Kiedy karta ma być gotowa?','["Po około dwóch tygodniach","Tego samego dnia","Za pół roku"]',0,'Изготовление карты займёт около двух недель.',3),
('office-reading-check','Po co Natalia zachowała potwierdzenie?','["Jest na nim numer sprawy","Daje zniżkę w kinie","Zastępuje paszport"]',0,'В подтверждении указан номер дела для проверки статуса.',4);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values
('natalia-sklada-wniosek','institutions','Natalia składa wniosek','Форма, документы и получение подтверждения','A2',6,'🏛️',
'["Natalia umówiła wizytę w urzędzie miasta, ponieważ chciała złożyć wniosek o kartę mieszkańca. W domu pobrała formularz, wpisała dane osobowe i przygotowała wymagany załącznik. Przed wyjściem sprawdziła też termin ważności paszportu.","W urzędzie pracownica poprosiła Natalię o dokument tożsamości. Potem razem przejrzały formularz. W jednej rubryce brakowało daty urodzenia, więc Natalia ją dopisała. Następnie podpisała wniosek i zapytała, kiedy karta będzie gotowa.","Pracownica wyjaśniła, że dokument będzie można odebrać po około dwóch tygodniach. Natalia dostała potwierdzenie z numerem sprawy. Zachowała je, ponieważ dzięki temu numerowi może sprawdzić status wniosku przez internet i nie musi ponownie podawać wszystkich danych."]',
'{"umówiła":{"lemma":"umówić","translation":"назначить","part_of_speech":"глагол"},"pobrała":{"lemma":"pobrać","translation":"скачать; получить","part_of_speech":"глагол"},"wymagany":{"lemma":"wymagany","translation":"обязательный","part_of_speech":"прилагательное"},"ważności":{"lemma":"ważność","translation":"срок действия","part_of_speech":"существительное"},"przejrzały":{"lemma":"przejrzeć","translation":"просмотреть","part_of_speech":"глагол"},"rubryce":{"lemma":"rubryka","translation":"поле формы","part_of_speech":"существительное"},"dopisała":{"lemma":"dopisać","translation":"дописать","part_of_speech":"глагол"},"odebrać":{"lemma":"odebrać","translation":"получить","part_of_speech":"глагол"},"potwierdzenie":{"lemma":"potwierdzenie","translation":"подтверждение","part_of_speech":"существительное"},"wniosku":{"lemma":"wniosek","translation":"заявление","part_of_speech":"существительное"}}',
'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-29","comprehension_lesson_id":"office-reading-check"}',20,true)
on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
