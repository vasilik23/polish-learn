-- Original PolskiFlow B2 content. Content-only migration; no schema, grants, or RLS changes.

insert into public.topics(id,course_id,title,description,emoji,position,is_active) values ('b2-professional-communication','b2-advanced','Профессиональная коммуникация','Проводим рабочую встречу и пишем точное деловое сообщение','💼',2,true) on conflict(id) do update set course_id=excluded.course_id,title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,position,is_active,theory_title,theory_sections,source_metadata) values
('b2prof-words','b2-professional-communication','words','Słowa w kontekście','Новая лексика','8 карточек · B2','Проводим рабочую встречу и пишем точное деловое сообщение',10,'💼',178,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-grammar','b2-professional-communication','grammar','Jak to wyrazić?','Языковой фокус','6 заданий · B2','Регистр, номинализация и этикет',13,'✏️',179,true,'Регистр, номинализация и этикет','[["Регистр","В деловой переписке просьбу смягчают формулы Zwracam się z prośbą o… и Czy mogliby Państwo…"],["Номинализация","Существительные на -anie/-enie уплотняют сообщение: omówić plan → omówienie planu."],["Результат встречи","Фиксируй decyzję, osobę odpowiedzialną и termin, используя bezosobowe ustalono/uzgodniono."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-review','b2-professional-communication','review','Powtórka aktywna','Активное повторение','7 карточек · B2','Закрепи лексику темы',9,'🔄',180,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-quiz','b2-professional-communication','quiz','Quiz: Профессиональная коммуникация','Проверка темы','10 вопросов · B2','Проверь лексику и языковой фокус',10,'🎯',181,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-reading-check','b2-professional-communication','quiz','Czy rozumiesz tekst?','Понимание текста','6 вопросов · B2','Найди детали и главный вывод',8,'📖',182,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}')
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('b2prof-1','porządek obrad','повестка встречи','Porządek obrad wysłano dzień wcześniej.',572,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-2','zabrać głos','взять слово','Czy mogę zabrać głos w tej sprawie?',573,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-3','ustalić priorytety','определить приоритеты','Najpierw ustalmy priorytety zespołu.',574,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-4','zgłosić zastrzeżenie','высказать возражение','Aneta zgłosiła zastrzeżenie do harmonogramu.',575,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-5','dojść do porozumienia','достичь соглашения','Po dyskusji doszliśmy do porozumienia.',576,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-6','podsumowanie','резюме, итог','Wyślę krótkie podsumowanie spotkania.',577,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-7','termin realizacji','срок выполнения','Termin realizacji przypada na piątek.',578,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-8','osoba odpowiedzialna','ответственное лицо','Każde zadanie ma osobę odpowiedzialną.',579,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-9','w nawiązaniu do','в продолжение, ссылаясь на','Piszę w nawiązaniu do naszej rozmowy.',580,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-10','zwracać się z prośbą','обращаться с просьбой','Zwracam się z prośbą o potwierdzenie.',581,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-11','uprzejmie przypominać','вежливо напоминать','Uprzejmie przypominam o terminie.',582,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-12','załącznik','вложение','Szczegóły znajdują się w załączniku.',583,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-13','uzgodnienie','согласование','Uzgodnienie warunków zajęło dwa dni.',584,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-14','wdrożenie','внедрение','Wdrożenie rozwiązania rozpocznie się w maju.',585,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2prof-15','pozostawać do dyspozycji','оставаться в распоряжении','W razie pytań pozostaję do dyspozycji.',586,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('b2prof-words','b2prof-review');

insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('b2prof-words','b2prof-1',0),
('b2prof-words','b2prof-2',1),
('b2prof-words','b2prof-3',2),
('b2prof-words','b2prof-4',3),
('b2prof-words','b2prof-5',4),
('b2prof-words','b2prof-6',5),
('b2prof-words','b2prof-7',6),
('b2prof-words','b2prof-8',7),
('b2prof-review','b2prof-9',0),
('b2prof-review','b2prof-10',1),
('b2prof-review','b2prof-11',2),
('b2prof-review','b2prof-12',3),
('b2prof-review','b2prof-13',4),
('b2prof-review','b2prof-14',5),
('b2prof-review','b2prof-15',6);

delete from public.questions where lesson_id in ('b2prof-grammar','b2prof-quiz','b2prof-reading-check');

insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('b2prof-grammar','___ z prośbą o przesłanie poprawionej wersji umowy.','["Zwracam się","Żądam się","Mówię się"]',0,'Zwracam się z prośbą o — нейтральная формальная просьба.',0),
('b2prof-grammar','Czasownik «omówić» można zastąpić nominalizacją ___.','["omówienie","omawiający","omówiony"]',0,'Omówienie — отглагольное существительное, называющее процесс.',1),
('b2prof-grammar','Na spotkaniu ___, że raport przygotuje dział analiz.','["ustalono","ustalił się","ustalając"]',0,'Ustalono — безличная форма на -no, фокусирующая решение, а не исполнителя.',2),
('b2prof-grammar','Proszę ___ potwierdzenie terminu do środy.','["o","na","za"]',0,'Формула prosić o требует винительного падежа.',3),
('b2prof-grammar','Составьте: В продолжение нашей встречи отправляю согласованное резюме.','["W nawiązaniu do naszego spotkania przesyłam uzgodnione podsumowanie.","Nawiązując nasze spotkanie wysyłam podsumowaniem.","Do spotkania przesyłam uzgodnić podsumowanie."]',0,'W nawiązaniu do + родительный задаёт формальную связь с предыдущим контактом.',4),
('b2prof-grammar','Составьте: Было решено перенести внедрение на следующий месяц.','["Ustalono, że wdrożenie zostanie przesunięte na przyszły miesiąc.","Ustalili wdrożenie przesuwa przyszły miesiąc.","Wdrożenie ustalając przesunęło miesiącem."]',0,'Ustalono и пассив zostanie przesunięte сохраняют официальный безличный регистр.',5),
('b2prof-quiz','Что означает porządek obrad?','["повестка встречи","трудовой договор","отпуск"]',0,'Это список вопросов для обсуждения.',0),
('b2prof-quiz','Jak grzecznie wejść do dyskusji?','["Czy mogę zabrać głos?","Przestańcie mówić!","Ja teraz."]',0,'Вопрос уважает очередь и участников.',1),
('b2prof-quiz','Po spotkaniu warto wysłać ___.','["podsumowanie","zastrzeżać","dyspozycję się"]',0,'Резюме фиксирует решения и следующие шаги.',2),
('b2prof-quiz','Uprzejmie ___ o jutrzejszym terminie.','["przypominam","żądam","rozkazuję"]',0,'Uprzejmie przypominam — корректная деловая формула.',3),
('b2prof-quiz','Która forma jest nominalizacją?','["wdrożenie","wdrażać","wdrożony"]',0,'Wdrożenie — существительное, называющее процесс.',4),
('b2prof-quiz','Na końcu protokołu wpisujemy ___.','["osoby odpowiedzialne i terminy","tylko powitanie","prywatne komentarze"]',0,'Так решение становится исполнимым.',5),
('b2prof-quiz','Proszę o przesłanie ___.','["załącznika","załącznikiem","załącznikowi"]',0,'Отглагольное существительное przesłanie управляет родительным: przesłanie czego? załącznika.',6),
('b2prof-quiz','Co znaczy zgłosić zastrzeżenie?','["высказать обоснованное возражение","подтвердить отпуск","закрыть встречу"]',0,'Zastrzeżenie сообщает о риске или несогласии.',7),
('b2prof-quiz','Które zakończenie e-maila jest profesjonalne?','["W razie pytań pozostaję do dyspozycji.","No to pa!","Odpisz natychmiast!!!"]',0,'Первая формула нейтральна и вежлива.',8),
('b2prof-quiz','Uzgodniono nowy termin — na czym skupia się zdanie?','["на достигнутом решении","на имени автора","на эмоциях адресата"]',0,'Безличная форма выдвигает результат на первый план.',9),
('b2prof-reading-check','Co uczestnicy otrzymali przed spotkaniem?','["Porządek obrad i materiały","Gotową umowę z klientem","Prywatny list"]',0,'Материалы позволили подготовиться к решениям.',0),
('b2prof-reading-check','Jakie zastrzeżenie zgłosił dział sprzedaży?','["Za krótki czas na szkolenie","Brak sali","Zbyt długą przerwę"]',0,'Он опасался, что сотрудники не успеют обучиться.',1),
('b2prof-reading-check','Jak rozwiązano problem?','["Podzielono wdrożenie na etapy","Odwołano projekt","Zignorowano uwagę"]',0,'Этапность стала компромиссом.',2),
('b2prof-reading-check','Co przypisano każdemu zadaniu?','["Termin i osobę odpowiedzialną","Kolor i zdjęcie","Tylko tytuł"]',0,'Это два обязательных элемента плана.',3),
('b2prof-reading-check','Dlaczego użyto form bezosobowych?','["Aby podkreślić rezultaty","Aby ukryć wszystkie terminy","Aby zmienić temat"]',0,'Протокол фокусируется на решениях.',4),
('b2prof-reading-check','Czego oczekiwała Maja do środy?','["Uwag do podsumowania","Nowego budżetu","Rezygnacji zespołu"]',0,'Она попросила прислать замечания.',5);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values ('b2prof-spotkanie-ktore-konczy-sie-decyzja','b2-professional-communication','Spotkanie, które kończy się decyzją','Как команда превратила сложное обсуждение в ясный план','B2',10,'💼','["Zespół Mai przygotowywał wdrożenie nowego systemu obsługi klientów. Przed spotkaniem wszyscy otrzymali porządek obrad, projekt harmonogramu oraz pytania wymagające decyzji. Maja, która prowadziła rozmowę, poprosiła uczestników, by najpierw ustalili priorytety, a dopiero później omawiali szczegóły techniczne.","Kiedy przedstawiciel działu sprzedaży zabrał głos, zgłosił zastrzeżenie do terminu realizacji. Uważał, że pracownicy nie zdążą przejść szkolenia. Zamiast odrzucić uwagę, Maja poprosiła o konkretne dane. Po krótkiej analizie uzgodniono podział wdrożenia na dwa etapy, dzięki czemu zespół doszedł do porozumienia.","Na zakończenie Maja przeczytała decyzje na głos. Każde zadanie otrzymało termin realizacji i osobę odpowiedzialną. Ustalono również, że ryzyka zostaną ponownie omówione za tydzień. Takie bezosobowe sformułowania pozwoliły skupić protokół na rezultatach, choć odpowiedzialność poszczególnych osób nadal była wyraźna.","Po spotkaniu Maja wysłała wiadomość: „W nawiązaniu do dzisiejszej rozmowy przesyłam podsumowanie. Uprzejmie proszę o zgłoszenie uwag do środy”. Dołączyła harmonogram w załączniku i zakończyła e-mail formułą „W razie pytań pozostaję do dyspozycji”. Dzięki temu uczestnicy wiedzieli nie tylko, co ustalono, lecz także jaki jest kolejny krok."]','{"wdrożenie":{"lemma":"wdrożenie","translation":"внедрение","part_of_speech":"существительное"},"obsługi":{"lemma":"obsługa","translation":"обслуживание","part_of_speech":"существительное"},"porządek":{"lemma":"porządek","translation":"порядок","part_of_speech":"существительное"},"wymagające":{"lemma":"wymagać","translation":"требующие","part_of_speech":"причастие"},"prowadziła":{"lemma":"prowadzić","translation":"вела","part_of_speech":"глагол"},"ustalili":{"lemma":"ustalić","translation":"определили","part_of_speech":"глагол"},"zastrzeżenie":{"lemma":"zastrzeżenie","translation":"возражение","part_of_speech":"существительное"},"zdążą":{"lemma":"zdążyć","translation":"успеют","part_of_speech":"глагол"},"odrzucić":{"lemma":"odrzucić","translation":"отклонить","part_of_speech":"глагол"},"uzgodniono":{"lemma":"uzgodnić","translation":"согласовали","part_of_speech":"глагол"},"etapy":{"lemma":"etap","translation":"этапы","part_of_speech":"существительное"},"doszedł":{"lemma":"dojść","translation":"достиг","part_of_speech":"глагол"},"zakończenie":{"lemma":"zakończenie","translation":"завершение","part_of_speech":"существительное"},"odpowiedzialną":{"lemma":"odpowiedzialny","translation":"ответственную","part_of_speech":"прилагательное"},"ryzyka":{"lemma":"ryzyko","translation":"риски","part_of_speech":"существительное"},"sformułowania":{"lemma":"sformułowanie","translation":"формулировки","part_of_speech":"существительное"},"poszczególnych":{"lemma":"poszczególny","translation":"отдельных","part_of_speech":"прилагательное"},"przesyłam":{"lemma":"przesyłać","translation":"отправляю","part_of_speech":"глагол"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30","comprehension_lesson_id":"b2prof-reading-check"}',38,true) on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
