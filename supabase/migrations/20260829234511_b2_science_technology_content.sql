-- Original PolskiFlow B2 content. Content-only migration; no schema, grants, or RLS changes.

insert into public.topics(id,course_id,title,description,emoji,position,is_active) values ('b2-science-technology','b2-advanced','Наука и технологии','Доступно объясняем процесс, идею и границы технологического решения','🔬',3,true) on conflict(id) do update set course_id=excluded.course_id,title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,position,is_active,theory_title,theory_sections,source_metadata) values
('b2tech-words','b2-science-technology','words','Słowa w kontekście','Новая лексика','8 карточек · B2','Доступно объясняем процесс, идею и границы технологического решения',10,'🔬',183,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-grammar','b2-science-technology','grammar','Jak to wyrazić?','Языковой фокус','6 заданий · B2','Определения и безличное описание процесса',13,'✏️',184,true,'Определения и безличное описание процесса','[["Определение","X to urządzenie/proces, który… сначала называет класс, затем отличительный признак."],["Пассив","Формы jest wykorzystywany / został opracowany выдвигают объект и результат на первый план."],["Безличность","Конструкции bada się, można zmierzyć и zaobserwowano описывают общий метод без ненужного исполнителя."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-review','b2-science-technology','review','Powtórka aktywna','Активное повторение','7 карточек · B2','Закрепи лексику темы',9,'🔄',185,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-quiz','b2-science-technology','quiz','Quiz: Наука и технологии','Проверка темы','10 вопросов · B2','Проверь лексику и языковой фокус',10,'🎯',186,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-reading-check','b2-science-technology','quiz','Czy rozumiesz tekst?','Понимание текста','6 вопросов · B2','Найди детали и главный вывод',8,'📖',187,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}')
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('b2tech-1','zjawisko','явление','Badacze obserwują niezwykłe zjawisko.',587,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-2','założenie','предположение, исходная посылка','Model opiera się na prostym założeniu.',588,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-3','hipoteza','гипотеза','Eksperyment potwierdził hipotezę.',589,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-4','przeprowadzić badanie','провести исследование','Zespół przeprowadził badanie w dwóch szkołach.',590,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-5','próbka','образец, выборка','Próbka była zbyt mała na pewny wniosek.',591,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-6','wynik','результат','Wynik trzeba powtórnie sprawdzić.',592,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-7','wiarygodny','достоверный','Potrzebujemy wiarygodnych danych.',593,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-8','ograniczenie','ограничение','Autorzy opisali ograniczenia metody.',594,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-9','przetwarzać dane','обрабатывать данные','Program przetwarza dane z czujników.',595,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-10','algorytm','алгоритм','Algorytm rozpoznaje powtarzalne wzorce.',596,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-11','czujnik','датчик','Czujnik mierzy temperaturę co minutę.',597,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-12','zastosowanie','применение','Technologia ma zastosowanie w medycynie.',598,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-13','opracować','разработать','Inżynierowie opracowali nową metodę.',599,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-14','wykrywać','обнаруживать','System pomaga wykrywać awarie.',600,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b2tech-15','na podstawie','на основании','Decyzję podjęto na podstawie danych.',601,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('b2tech-words','b2tech-review');

insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('b2tech-words','b2tech-1',0),
('b2tech-words','b2tech-2',1),
('b2tech-words','b2tech-3',2),
('b2tech-words','b2tech-4',3),
('b2tech-words','b2tech-5',4),
('b2tech-words','b2tech-6',5),
('b2tech-words','b2tech-7',6),
('b2tech-words','b2tech-8',7),
('b2tech-review','b2tech-9',0),
('b2tech-review','b2tech-10',1),
('b2tech-review','b2tech-11',2),
('b2tech-review','b2tech-12',3),
('b2tech-review','b2tech-13',4),
('b2tech-review','b2tech-14',5),
('b2tech-review','b2tech-15',6);

delete from public.questions where lesson_id in ('b2tech-grammar','b2tech-quiz','b2tech-reading-check');

insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('b2tech-grammar','Czujnik to urządzenie, ___ mierzy zmiany temperatury.','["które","który","którego"]',0,'Urządzenie — средний род, поэтому które.',0),
('b2tech-grammar','Dane są ___ przez algorytm co kilka sekund.','["przetwarzane","przetwarzać","przetworzyły"]',0,'Пассив: są + причастие, согласованное с dane во множественном числе.',1),
('b2tech-grammar','W laboratorium ___ wpływ światła na rośliny.','["bada się","badają siebie","jest badać"]',0,'Bada się — безличная возвратная конструкция для общего процесса.',2),
('b2tech-grammar','Podczas testu ___ niewielką różnicę między grupami.','["zaobserwowano","obserwując się","został obserwować"]',0,'Форма на -no сообщает наблюдение без указания исследователя.',3),
('b2tech-grammar','Составьте: Алгоритм — это набор правил, который используется для обработки данных.','["Algorytm to zbiór reguł, który jest wykorzystywany do przetwarzania danych.","Algorytm jest reguły, które wykorzystuje przetwarzać dane.","Zbiór algorytmem został danych przetwarzać."]',0,'Определение строится через to, а пассив jest wykorzystywany согласуется с zbiór.',4),
('b2tech-grammar','Составьте: На основании результатов было разработано новое решение.','["Na podstawie wyników opracowano nowe rozwiązanie.","Podstawą wyniki opracował się nowe rozwiązaniem.","Wyniki zostały opracować rozwiązanie."]',0,'Na podstawie требует родительного, opracowano — безличная форма.',5),
('b2tech-quiz','Что означает próbka в исследовании?','["образец или группа для анализа","готовый вывод","название прибора"]',0,'Próbka — часть материала или наблюдений.',0),
('b2tech-quiz','Hipotezę należy ___.','["sprawdzić","założyć wynik","ukryć ograniczenie"]',0,'Гипотеза требует проверки данными.',1),
('b2tech-quiz','Które zdanie zawiera definicję?','["Czujnik to urządzenie, które rejestruje zmiany.","Czujnik leży tutaj.","Lubię czujniki."]',0,'Указан класс и отличительная функция.',2),
('b2tech-quiz','Dane zostały ___ przez niezależny zespół.','["zweryfikowane","weryfikować","weryfikując"]',0,'Пассив требует причастия zweryfikowane.',3),
('b2tech-quiz','Co zwiększa wiarygodność wyniku?','["powtórzenie badania na większej próbce","pominięcie danych","brak opisu metody"]',0,'Повторяемость и выборка укрепляют вывод.',4),
('b2tech-quiz','W tym laboratorium ___ nowe materiały.','["testuje się","testuje siebie","jest testować"]',0,'Безличное się описывает регулярный процесс.',5),
('b2tech-quiz','Algorytm ___ wzorce w danych.','["wykrywa","próbkuje się do","wiarygodni"]',0,'Wykrywać wzorce — естественное сочетание.',6),
('b2tech-quiz','Dlaczego podaje się ograniczenia badania?','["Чтобы показать границы вывода","Чтобы скрыть метод","Чтобы заменить результаты"]',0,'Ограничения помогают правильно интерпретировать данные.',7),
('b2tech-quiz','Na podstawie ___ sformułowano wniosek.','["wyników","wyniki","wynikami"]',0,'Na podstawie требует родительного падежа.',8),
('b2tech-quiz','Która forma skupia uwagę na rezultacie?','["Rozwiązanie zostało opracowane w maju.","Inżynierowie lubią maj.","My coś robimy."]',0,'Пассив выдвигает решение и факт разработки.',9),
('b2tech-reading-check','Co mierzy czujnik?','["Wilgotność gleby","Liczbę gości","Cenę wody"]',0,'Датчик измеряет влажность почвы.',0),
('b2tech-reading-check','Kiedy system uruchamia podlewanie?','["Po wykryciu dłuższego niedoboru wody","Zawsze o tej samej godzinie","Gdy gleba jest mokra"]',0,'Решение зависит от фактических условий.',1),
('b2tech-reading-check','Gdzie przeprowadzono badanie?','["W sześciu ogrodach","W jednej fabryce","W stu mieszkaniach"]',0,'В тексте указаны шесть садов.',2),
('b2tech-reading-check','Jaki był średni wynik?','["Osiemnaście procent oszczędności","Osiemdziesiąt procent","Brak zmiany"]',0,'Средняя экономия составила 18%.',3),
('b2tech-reading-check','Jakie ograniczenie wskazali autorzy?','["Małą próbkę i badanie tylko latem","Brak czujników","Zbyt wiele zimowych danych"]',0,'Оба ограничения названы прямо.',4),
('b2tech-reading-check','Jak należy jasno wyjaśniać technologię?','["Definicja, proces, wyniki i granice wniosku","Tylko lista terminów","Wyłącznie obietnice korzyści"]',0,'Финал текста предлагает эту структуру.',5);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values ('b2tech-czujniki-ktore-oszczedzaja-wode','b2-science-technology','Czujniki, które pomagają oszczędzać wodę','Как объяснить принцип системы и не скрыть ограничения исследования','B2',11,'🔬','["Grupa studentów opracowała system, który pomaga ograniczyć zużycie wody w miejskich ogrodach. Jego podstawowym elementem jest czujnik, czyli urządzenie mierzące wilgotność gleby. Dane są przesyłane do programu, gdzie co kilka minut przetwarza je algorytm.","Algorytm to zbiór reguł, na podstawie których podejmowana jest decyzja o podlewaniu. Jeżeli gleba pozostaje wilgotna, zawór nie zostaje otwarty. Gdy czujnik wykrywa dłuższy niedobór wody, system uruchamia podlewanie tylko w wybranej części ogrodu. Dzięki temu nie działa według stałego harmonogramu, lecz reaguje na rzeczywiste warunki.","Przed wdrożeniem przeprowadzono badanie w sześciu ogrodach. Zużycie wody porównywano przez dwa miesiące, a wynik wskazywał na średnią oszczędność wynoszącą osiemnaście procent. Podobne zjawisko zaobserwowano w większości lokalizacji, dlatego wstępna hipoteza została uznana za wiarygodną.","Autorzy podkreślili jednak ograniczenia. Próbka była niewielka, a badanie prowadzono tylko latem. Nie wiadomo więc, czy taki sam wynik uzyska się przy innej glebie albo częstszych opadach. Zanim rozwiązanie znajdzie szersze zastosowanie, należy powtórzyć pomiary w różnych warunkach.","Projekt pokazuje, że technologię można wyjaśnić bez nadmiaru terminów: najpierw definiuje się elementy, potem opisuje proces, wyniki i granice wniosku. Tak przedstawiona informacja pozwala odbiorcy zrozumieć zarówno korzyści, jak i niepewność związaną z nową metodą."]','{"opracowała":{"lemma":"opracować","translation":"разработала","part_of_speech":"глагол"},"zużycie":{"lemma":"zużycie","translation":"потребление","part_of_speech":"существительное"},"wilgotność":{"lemma":"wilgotność","translation":"влажность","part_of_speech":"существительное"},"gleby":{"lemma":"gleba","translation":"почва","part_of_speech":"существительное"},"przesyłane":{"lemma":"przesyłać","translation":"передаваемые","part_of_speech":"причастие"},"podejmowana":{"lemma":"podejmować","translation":"принимаемая","part_of_speech":"причастие"},"podlewaniu":{"lemma":"podlewanie","translation":"полив","part_of_speech":"существительное"},"zawór":{"lemma":"zawór","translation":"клапан","part_of_speech":"существительное"},"niedobór":{"lemma":"niedobór","translation":"недостаток","part_of_speech":"существительное"},"uruchamia":{"lemma":"uruchamiać","translation":"запускает","part_of_speech":"глагол"},"rzeczywiste":{"lemma":"rzeczywisty","translation":"фактические","part_of_speech":"прилагательное"},"wdrożeniem":{"lemma":"wdrożenie","translation":"внедрение","part_of_speech":"существительное"},"oszczędność":{"lemma":"oszczędność","translation":"экономия","part_of_speech":"существительное"},"wstępna":{"lemma":"wstępny","translation":"предварительная","part_of_speech":"прилагательное"},"ograniczenia":{"lemma":"ograniczenie","translation":"ограничения","part_of_speech":"существительное"},"opadach":{"lemma":"opad","translation":"осадки","part_of_speech":"существительное"},"pomiary":{"lemma":"pomiar","translation":"измерения","part_of_speech":"существительное"},"niepewność":{"lemma":"niepewność","translation":"неопределённость","part_of_speech":"существительное"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30","comprehension_lesson_id":"b2tech-reading-check"}',39,true) on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
