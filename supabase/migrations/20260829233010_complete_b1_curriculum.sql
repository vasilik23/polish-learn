insert into public.topics(id,course_id,title,description,emoji,position,is_active) values ('b1-society','b1-independent','Общество','Обсуждаем знакомую общественную тему и аргументируем мнение','🤝',8,true) on conflict(id) do update set course_id=excluded.course_id,title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,position,is_active,theory_title,theory_sections,source_metadata) values
('b1soc-words','b1-society','words','Słowa w kontekście','Новая лексика','8 карточек · B1','Обсуждаем знакомую общественную тему и аргументируем мнение',9,'🤝',148,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-grammar','b1-society','grammar','Jak to wyrazić?','Языковой фокус','6 заданий · B1','Аргумент и уступка',12,'✏️',149,true,'Аргумент и уступка','[["Причина","Ponieważ вводит причину, а więc — логическое следствие."],["Уступка","Chociaż показывает контраст между ожидаемым и реальным."],["Позиция","Начни с moim zdaniem, добавь причину и конкретный пример."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-review','b1-society','review','Powtórka aktywna','Активное повторение','7 карточек · B1','Закрепи лексику темы',8,'🔄',150,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-quiz','b1-society','quiz','Quiz: Общество','Проверка темы','10 вопросов · B1','Проверь лексику и связность',9,'🎯',151,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-reading-check','b1-society','quiz','Czy rozumiesz tekst?','Понимание текста','6 вопросов · B1','Найди детали и главный вывод',7,'📖',152,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}')
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('b1soc-1','społeczność','сообщество','Lokalna społeczność zorganizowała spotkanie.',482,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-2','mieszkaniec','житель','Każdy mieszkaniec mógł zabrać głos.',483,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-3','wolontariat','волонтёрство','Wolontariat pomaga poznać sąsiadów.',484,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-4','inicjatywa','инициатива','Poparliśmy inicjatywę młodzieży.',485,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-5','potrzeba','потребность','Projekt odpowiada na potrzeby mieszkańców.',486,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-6','dostępny','доступный','Transport powinien być dostępny dla wszystkich.',487,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-7','wspierać','поддерживать','Miasto wspiera lokalne organizacje.',488,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-8','uczestniczyć','участвовать','Warto uczestniczyć w konsultacjach.',489,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-9','odpowiedzialność','ответственность','Wspólna przestrzeń to nasza odpowiedzialność.',490,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-10','rozwiązanie','решение','Szukamy praktycznego rozwiązania.',491,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-11','korzyść','польза','Zmiana przyniesie korzyść całej dzielnicy.',492,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-12','wada','недостаток','Każde rozwiązanie ma także wady.',493,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-13','opinia','мнение','Szanuję twoją opinię.',494,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-14','przekonać','убедить','Ten przykład może przekonać niezdecydowanych.',495,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1soc-15','dojść do porozumienia','договориться','Po dyskusji doszliśmy do porozumienia.',496,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('b1soc-words','b1soc-review');

insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('b1soc-words','b1soc-1',0),
('b1soc-words','b1soc-2',1),
('b1soc-words','b1soc-3',2),
('b1soc-words','b1soc-4',3),
('b1soc-words','b1soc-5',4),
('b1soc-words','b1soc-6',5),
('b1soc-words','b1soc-7',6),
('b1soc-words','b1soc-8',7),
('b1soc-review','b1soc-9',0),
('b1soc-review','b1soc-10',1),
('b1soc-review','b1soc-11',2),
('b1soc-review','b1soc-12',3),
('b1soc-review','b1soc-13',4),
('b1soc-review','b1soc-14',5),
('b1soc-review','b1soc-15',6);

delete from public.questions where lesson_id in ('b1soc-grammar','b1soc-quiz','b1soc-reading-check');

insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('b1soc-grammar','Popieram projekt, ___ ułatwi życie starszym mieszkańcom.','["ponieważ","chociaż","więc"]',0,'Ponieważ вводит причину поддержки.',0),
('b1soc-grammar','Pomysł jest kosztowny, ___ może przynieść długoterminowe korzyści.','["chociaż","ponieważ","dlatego"]',0,'Chociaż выражает уступку.',1),
('b1soc-grammar','Brakuje bezpiecznych przejść, ___ mieszkańcy proszą o zmiany.','["więc","mimo że","ponieważ"]',0,'Więc вводит следствие.',2),
('b1soc-grammar','Moim zdaniem warto działać, ___ mały krok też ma znaczenie.','["ponieważ","więc","chociaż"]',0,'Здесь требуется обоснование позиции.',3),
('b1soc-grammar','Составьте: Хотя мнения различаются, мы можем найти решение.','["Chociaż opinie są różne, możemy znaleźć rozwiązanie.","Ponieważ opinie różne, więc rozwiązanie.","Opinie chociaż są, znaleźć rozwiązaniem."]',0,'Chociaż открывает придаточное уступки.',4),
('b1soc-grammar','Составьте: Району нужен парк, поэтому я поддерживаю инициативу.','["Dzielnica potrzebuje parku, więc popieram inicjatywę.","Dzielnica potrzebuje park, ponieważ popieram inicjatywą.","Chociaż park potrzebuje, popieram."]',0,'Więc логично соединяет проблему и позицию.',5),
('b1soc-quiz','Что означает społeczność lokalna?','["местное сообщество","городской транспорт","частное мнение"]',0,'Это люди, объединённые местом и общими делами.',0),
('b1soc-quiz','Warto ___ w konsultacjach społecznych.','["uczestniczyć","przekonywać się","wynikać"]',0,'Uczestniczyć w — участвовать в.',1),
('b1soc-quiz','Projekt ma zalety, ___ wymaga dużego budżetu.','["chociaż","więc","ponieważ"]',0,'Нужна уступка.',2),
('b1soc-quiz','Brakuje zieleni, ___ proponujemy nowy park.','["więc","mimo że","chociaż"]',0,'Предложение является следствием.',3),
('b1soc-quiz','Как вежливо начать мнение?','["Moim zdaniem…","To oczywiste dla każdego…","Nie masz racji."]',0,'Moim zdaniem нейтрально обозначает позицию.',4),
('b1soc-quiz','Które połączenie jest naturalne?','["dojść do porozumienia","zrobić społeczność","uczestniczyć opinię"]',0,'Устойчивое выражение — dojść do porozumienia.',5),
('b1soc-quiz','Inicjatywa przyniesie ___ mieszkańcom.','["korzyści","wadywać","odpowiedzialni"]',0,'Przynosić korzyści — приносить пользу.',6),
('b1soc-quiz','Что усиливает аргумент?','["конкретный пример","повтор одного мнения","нападение на собеседника"]',0,'Пример показывает практическое основание.',7),
('b1soc-quiz','Szanuję twoją ___, ale widzę problem inaczej.','["opinię","potrzebą","rozwiązaniem"]',0,'Szanuję kogo/co требует винительного падежа.',8),
('b1soc-quiz','Które zdanie zawiera argument?','["Popieram zmianę, ponieważ zwiększy bezpieczeństwo.","Zmiana, zmiana, zmiana.","Każdy musi się zgodzić."]',0,'Есть позиция и причина.',9),
('b1soc-reading-check','Co znajdowało się na osiedlu?','["Niewykorzystany plac","Nowa szkoła","Duży dworzec"]',0,'На районе была пустующая площадка.',0),
('b1soc-reading-check','Jakie były dwie propozycje?','["Parking i ogród społeczny","Basen i kino","Sklep i urząd"]',0,'Спор касался парковки и сада.',1),
('b1soc-reading-check','Jaką rolę miała Maja?','["Zapisywała argumenty jako wolontariuszka","Projektowała parking","Prowadziła sklep"]',0,'Она фиксировала аргументы.',2),
('b1soc-reading-check','Na czym polegał kompromis?','["Plac podzielono między parking i ogród","Zrezygnowano z obu planów","Zbudowano tylko parking"]',0,'Пространство разделили.',3),
('b1soc-reading-check','Co dał wspólny projekt?','["Korzyści i lepsze porozumienie","Więcej konfliktów","Brak dostępu do placu"]',0,'Он объединил соседей.',4),
('b1soc-reading-check','Jaki jest wniosek?','["Kompromis wymaga słuchania i konkretów","Najgłośniejsza osoba zawsze wygrywa","Konsultacje nie mają sensu"]',0,'Вывод прямо дан в конце.',5);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values ('b1soc-sasiedzki-ogrod','b1-society','Ogród, który połączył sąsiadów','Как общественная инициатива привела к компромиссу','B1',8,'🤝','["Na osiedlu Mai stał pusty plac, którego od lat nikt nie wykorzystywał. Część mieszkańców chciała parkingu, ponieważ wieczorami brakowało miejsc. Inni proponowali ogród społeczny dostępny dla dzieci i seniorów.","Rada dzielnicy zaprosiła mieszkańców na konsultacje. Chociaż opinie były bardzo różne, każdy mógł przedstawić potrzeby i wady obu pomysłów. Maja uczestniczyła w spotkaniu jako wolontariuszka i zapisywała najważniejsze argumenty.","Po długiej rozmowie pojawiło się rozwiązanie: połowę placu przeznaczono na mały parking, a resztę na ogród. Miasto obiecało wspierać inicjatywę, więc społeczność przygotowała plan prac i podzieliła odpowiedzialność.","Pierwszej wiosny sąsiedzi wspólnie posadzili rośliny. Projekt nie spełnił wszystkich oczekiwań, ale przyniósł wyraźne korzyści i pomógł ludziom dojść do porozumienia. Maja przekonała się, że kompromis wymaga słuchania, konkretnych przykładów i cierpliwości."]','{"osiedlu":{"lemma":"osiedle","translation":"жилой район","part_of_speech":"существительное"},"plac":{"lemma":"plac","translation":"площадка","part_of_speech":"существительное"},"wykorzystywał":{"lemma":"wykorzystywać","translation":"использовать","part_of_speech":"глагол"},"brakowało":{"lemma":"brakować","translation":"не хватать","part_of_speech":"глагол"},"dostępny":{"lemma":"dostępny","translation":"доступный","part_of_speech":"прилагательное"},"konsultacje":{"lemma":"konsultacja","translation":"общественные обсуждения","part_of_speech":"существительное"},"wady":{"lemma":"wada","translation":"недостаток","part_of_speech":"существительное"},"wolontariuszka":{"lemma":"wolontariuszka","translation":"волонтёрка","part_of_speech":"существительное"},"przeznaczono":{"lemma":"przeznaczyć","translation":"выделить","part_of_speech":"глагол"},"resztę":{"lemma":"reszta","translation":"остаток","part_of_speech":"существительное"},"podzieliła":{"lemma":"podzielić","translation":"разделить","part_of_speech":"глагол"},"posadzili":{"lemma":"posadzić","translation":"посадить","part_of_speech":"глагол"},"oczekiwań":{"lemma":"oczekiwanie","translation":"ожидание","part_of_speech":"существительное"},"cierpliwości":{"lemma":"cierpliwość","translation":"терпение","part_of_speech":"существительное"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30","comprehension_lesson_id":"b1soc-reading-check"}',32,true) on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.topics(id,course_id,title,description,emoji,position,is_active) values ('b1-ecology','b1-independent','Природа и экология','Объясняем причины, последствия и реалистичные экологические решения','🌱',9,true) on conflict(id) do update set course_id=excluded.course_id,title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,position,is_active,theory_title,theory_sections,source_metadata) values
('b1eco-words','b1-ecology','words','Słowa w kontekście','Новая лексика','8 карточек · B1','Объясняем причины, последствия и реалистичные экологические решения',9,'🌱',153,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-grammar','b1-ecology','grammar','Jak to wyrazić?','Языковой фокус','6 заданий · B1','Причина, следствие и решение',12,'✏️',154,true,'Причина, следствие и решение','[["Причина","Z powodu + родительный и ponieważ называют причину."],["Следствие","Dlatego, wskutek tego и prowadzić do показывают результат."],["Решение","Żeby + прошедшая форма выражает цель действия."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-review','b1-ecology','review','Powtórka aktywna','Активное повторение','7 карточек · B1','Закрепи лексику темы',8,'🔄',155,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-quiz','b1-ecology','quiz','Quiz: Природа и экология','Проверка темы','10 вопросов · B1','Проверь лексику и связность',9,'🎯',156,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-reading-check','b1-ecology','quiz','Czy rozumiesz tekst?','Понимание текста','6 вопросов · B1','Найди детали и главный вывод',7,'📖',157,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}')
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('b1eco-1','środowisko','окружающая среда','Dbamy o środowisko w naszej gminie.',497,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-2','zanieczyszczenie','загрязнение','Zanieczyszczenie powietrza spadło.',498,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-3','odpady','отходы','Segregujemy odpady w domu.',499,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-4','susza','засуха','Długa susza niszczy rośliny.',500,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-5','powódź','наводнение','Po ulewie groziła nam powódź.',501,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-6','gatunek','вид','Ten gatunek ptaka potrzebuje ochrony.',502,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-7','chronić','защищать','Musimy chronić lokalny las.',503,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-8','ograniczyć','ограничить','Chcemy ograniczyć zużycie plastiku.',504,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-9','zużycie','потребление','Zużycie wody latem rośnie.',505,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-10','odnawialny','возобновляемый','Energia odnawialna zmniejsza emisje.',506,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-11','emisja','выброс','Transport odpowiada za część emisji.',507,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-12','ponownie wykorzystać','использовать повторно','Słoik można ponownie wykorzystać.',508,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-13','oszczędzać','экономить','Oszczędzamy wodę i energię.',509,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-14','skutek','последствие','Skutki suszy odczuli rolnicy.',510,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1eco-15','rozwiązanie','решение','Potrzebujemy trwałego rozwiązania.',511,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('b1eco-words','b1eco-review');

insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('b1eco-words','b1eco-1',0),
('b1eco-words','b1eco-2',1),
('b1eco-words','b1eco-3',2),
('b1eco-words','b1eco-4',3),
('b1eco-words','b1eco-5',4),
('b1eco-words','b1eco-6',5),
('b1eco-words','b1eco-7',6),
('b1eco-words','b1eco-8',7),
('b1eco-review','b1eco-9',0),
('b1eco-review','b1eco-10',1),
('b1eco-review','b1eco-11',2),
('b1eco-review','b1eco-12',3),
('b1eco-review','b1eco-13',4),
('b1eco-review','b1eco-14',5),
('b1eco-review','b1eco-15',6);

delete from public.questions where lesson_id in ('b1eco-grammar','b1eco-quiz','b1eco-reading-check');

insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('b1eco-grammar','Z powodu długiej suszy ___ poziom rzeki.','["obniżył się","ochronił","wykorzystał"]',0,'Z powodu называет причину снижения.',0),
('b1eco-grammar','Padało przez wiele godzin, ___ część ulic została zalana.','["dlatego","chociaż","żeby"]',0,'Dlatego вводит следствие.',1),
('b1eco-grammar','Nadmierne zużycie plastiku prowadzi ___ większej ilości odpadów.','["do","dla","nad"]',0,'Prowadzić do требует родительного падежа.',2),
('b1eco-grammar','Mieszkańcy zbierają deszczówkę, ___ oszczędzać wodę.','["żeby","ponieważ","wskutek"]',0,'Żeby + инфинитив выражает цель при одном субъекте.',3),
('b1eco-grammar','Составьте: Из-за загрязнения город ограничил движение автомобилей.','["Z powodu zanieczyszczenia miasto ograniczyło ruch samochodów.","Dlatego zanieczyszczenie ograniczył miastem ruch.","Żeby zanieczyszczenia miasto ruch ogranicza."]',0,'Z powodu требует родительного падежа.',4),
('b1eco-grammar','Составьте: Мы повторно используем вещи, чтобы уменьшить количество отходов.','["Ponownie wykorzystujemy rzeczy, żeby ograniczyć ilość odpadów.","Odpady prowadzą rzeczy ponownie wykorzystać.","Ponieważ wykorzystać rzeczy, dlatego odpady."]',0,'Żeby корректно вводит цель.',5),
('b1eco-quiz','Что означает odpady?','["отходы","осадки","растения"]',0,'Odpady — ненужные материалы и мусор.',0),
('b1eco-quiz','Długa ___ spowodowała brak wody.','["susza","emisja","powódź"]',0,'Susza — длительный период без дождя.',1),
('b1eco-quiz','Które źródło energii jest odnawialne?','["wiatr","węgiel","benzyna"]',0,'Ветер восстанавливается естественным образом.',2),
('b1eco-quiz','Zanieczyszczenie prowadzi ___ problemów zdrowotnych.','["do","na","przy"]',0,'Управление prowadzić do.',3),
('b1eco-quiz','Jak ograniczyć odpady?','["Ponownie wykorzystywać rzeczy","Kupować więcej opakowań","Wyrzucać szkło do lasu"]',0,'Повторное использование уменьшает отходы.',4),
('b1eco-quiz','Padało intensywnie, ___ rzeka wystąpiła z brzegów.','["dlatego","żeby","chociaż"]',0,'Нужно следствие.',5),
('b1eco-quiz','Что называет skutek?','["последствие","причину","вид животного"]',0,'Skutek — результат причины.',6),
('b1eco-quiz','Oszczędzamy wodę, ___ chronić jej zasoby.','["żeby","z powodu","mimo"]',0,'Żeby вводит цель.',7),
('b1eco-quiz','Выберите естественное сочетание.','["ograniczyć emisję","chronić zużyciem","odnawiać suszę"]',0,'Ograniczyć emisję — сократить выбросы.',8),
('b1eco-quiz','Które zdanie pokazuje przyczynę i skutek?','["Z powodu suszy zużywamy mniej wody.","Woda jest wodą.","Las, ale miasto."]',0,'Конструкция ясно называет оба элемента.',9),
('b1eco-reading-check','Gdzie wcześniej płynęła rzeka?','["W betonowym kanale","Przez naturalny las","Pod szkołą"]',0,'Река была заключена в бетонный канал.',0),
('b1eco-reading-check','Jaki problem pojawiał się podczas opadów?','["Rosło ryzyko powodzi","Brakowało energii","Znikały drogi"]',0,'Вода быстро стекала в центр.',1),
('b1eco-reading-check','Dlaczego potrzebne były rośliny?','["Zatrzymują wodę i wspierają gatunki","Produkują beton","Zwiększają emisję"]',0,'Они замедляют воду и создают среду.',2),
('b1eco-reading-check','Jak ochroniono ptaki?','["Odsunięto ścieżkę od gniazd","Usunięto wszystkie drzewa","Zamknięto cały park"]',0,'Маршрут отвели от гнёзд.',3),
('b1eco-reading-check','Co ponownie wykorzystano?','["Stare kamienie","Plastikowe butelki","Samochody"]',0,'В проекте повторно применили камни.',4),
('b1eco-reading-check','Jaki jest główny wniosek?','["Rozwiązanie może łączyć naturę i potrzeby ludzi","Jedna inwestycja kończy zmianę klimatu","Beton zawsze chroni przed powodzią"]',0,'Финал подчёркивает баланс.',5);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values ('b1eco-rzeka-wraca-do-miasta','b1-ecology','Rzeka wraca do miasta','Как жители нашли решение экологической проблемы','B1',9,'🌱','["Przez wiele lat mała rzeka w mieście była ukryta w betonowym kanale. Z powodu zanieczyszczenia i braku roślin prawie nie żyły w niej ryby ani owady. Podczas intensywnych opadów woda szybko spływała do centrum i zwiększała ryzyko powodzi.","Samorząd zaproponował przywrócenie naturalnych brzegów. Chociaż inwestycja była kosztowna, naukowcy wyjaśnili, że beton prowadzi do szybszego przepływu, natomiast rośliny zatrzymują część wody i tworzą miejsce dla różnych gatunków.","Mieszkańcy poparli projekt, ale poprosili o ścieżkę i ławki. Żeby chronić najcenniejszy fragment, trasę poprowadzono dalej od gniazd ptaków. Wykorzystano też stare kamienie ponownie, dzięki czemu ograniczono ilość odpadów.","Po dwóch latach jakość wody się poprawiła, a nad rzeką pojawiły się nowe gatunki. Park nie rozwiązał całego problemu zmian klimatu, jednak zmniejszył skutki upałów i ulew. Projekt pokazał, że trwałe rozwiązanie może łączyć ochronę środowiska z potrzebami ludzi."]','{"ukryta":{"lemma":"ukryć","translation":"скрытая","part_of_speech":"причастие"},"kanale":{"lemma":"kanał","translation":"канал","part_of_speech":"существительное"},"owady":{"lemma":"owad","translation":"насекомое","part_of_speech":"существительное"},"opadów":{"lemma":"opad","translation":"осадки","part_of_speech":"существительное"},"spływała":{"lemma":"spływać","translation":"стекать","part_of_speech":"глагол"},"przywrócenie":{"lemma":"przywrócenie","translation":"восстановление","part_of_speech":"существительное"},"brzegów":{"lemma":"brzeg","translation":"берег","part_of_speech":"существительное"},"przepływu":{"lemma":"przepływ","translation":"течение","part_of_speech":"существительное"},"zatrzymują":{"lemma":"zatrzymywać","translation":"удерживать","part_of_speech":"глагол"},"najcenniejszy":{"lemma":"cenny","translation":"самый ценный","part_of_speech":"прилагательное"},"gniazd":{"lemma":"gniazdo","translation":"гнездо","part_of_speech":"существительное"},"ograniczono":{"lemma":"ograniczyć","translation":"ограничить","part_of_speech":"глагол"},"upałów":{"lemma":"upał","translation":"жара","part_of_speech":"существительное"},"ulew":{"lemma":"ulewa","translation":"ливень","part_of_speech":"существительное"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30","comprehension_lesson_id":"b1eco-reading-check"}',33,true) on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.topics(id,course_id,title,description,emoji,position,is_active) values ('b1-poland-regions','b1-independent','Польша и регионы','Представляем регион и сравниваем сведения из разных источников','🗺️',10,true) on conflict(id) do update set course_id=excluded.course_id,title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,position,is_active,theory_title,theory_sections,source_metadata) values
('b1region-words','b1-poland-regions','words','Słowa w kontekście','Новая лексика','8 карточек · B1','Представляем регион и сравниваем сведения из разных источников',9,'🗺️',158,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-grammar','b1-poland-regions','grammar','Jak to wyrazić?','Языковой фокус','6 заданий · B1','Связное сравнение источников',12,'✏️',159,true,'Связное сравнение источников','[["Сходство","Zarówno… jak i… объединяет общие признаки."],["Различие","Natomiast, w przeciwieństwie do и podczas gdy показывают контраст."],["Источник","Według + родительный сообщает, откуда взяты сведения."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-review','b1-poland-regions','review','Powtórka aktywna','Активное повторение','7 карточек · B1','Закрепи лексику темы',8,'🔄',160,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-quiz','b1-poland-regions','quiz','Quiz: Польша и регионы','Проверка темы','10 вопросов · B1','Проверь лексику и связность',9,'🎯',161,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-reading-check','b1-poland-regions','quiz','Czy rozumiesz tekst?','Понимание текста','6 вопросов · B1','Найди детали и главный вывод',7,'📖',162,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}')
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('b1region-1','region','регион','Każdy region ma własne tradycje.',512,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-2','województwo','воеводство','Miasto leży w tym województwie.',513,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-3','krajobraz','ландшафт','Krajobraz zmienia się za przełęczą.',514,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-4','dziedzictwo','наследие','Muzeum chroni lokalne dziedzictwo.',515,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-5','gwara','диалект','Starsze osoby nadal mówią gwarą.',516,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-6','rzemiosło','ремесло','Region słynie z tradycyjnego rzemiosła.',517,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-7','szlak','маршрут','Szlak prowadzi przez trzy wsie.',518,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-8','przełęcz','горный перевал','Z przełęczy widać dolinę.',519,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-9','według','согласно','Według przewodnika trasa ma osiem kilometrów.',520,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-10','natomiast','в то время как','Centrum jest gwarne, natomiast okolica spokojna.',521,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-11','w przeciwieństwie do','в отличие от','W przeciwieństwie do lata zimą jest tu cicho.',522,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-12','zarówno','как… так и','Zarówno historia, jak i przyroda przyciągają gości.',523,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-13','wyróżniać się','выделяться','Miasteczko wyróżnia się drewnianą zabudową.',524,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-14','graniczyć','граничить','Region graniczy z Czechami.',525,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1region-15','zachować','сохранить','Mieszkańcy chcą zachować tradycję.',526,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('b1region-words','b1region-review');

insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('b1region-words','b1region-1',0),
('b1region-words','b1region-2',1),
('b1region-words','b1region-3',2),
('b1region-words','b1region-4',3),
('b1region-words','b1region-5',4),
('b1region-words','b1region-6',5),
('b1region-words','b1region-7',6),
('b1region-words','b1region-8',7),
('b1region-review','b1region-9',0),
('b1region-review','b1region-10',1),
('b1region-review','b1region-11',2),
('b1region-review','b1region-12',3),
('b1region-review','b1region-13',4),
('b1region-review','b1region-14',5),
('b1region-review','b1region-15',6);

delete from public.questions where lesson_id in ('b1region-grammar','b1region-quiz','b1region-reading-check');

insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('b1region-grammar','Według ___ ten szlak jest dostępny także zimą.','["przewodnika","przewodnik","przewodnikiem"]',0,'Według требует родительного падежа.',0),
('b1region-grammar','Zarówno muzeum, ___ stary rynek opowiadają historię miasta.','["jak i","natomiast","według"]',0,'Парная конструкция zarówno… jak i.',1),
('b1region-grammar','Północ regionu jest płaska, ___ południe ma górski krajobraz.','["natomiast","zarówno","według"]',0,'Natomiast вводит контраст.',2),
('b1region-grammar','W przeciwieństwie ___ popularnego kurortu ta wieś jest spokojna.','["do","z","od"]',0,'Устойчивое управление w przeciwieństwie do.',3),
('b1region-grammar','Составьте: Согласно музею ремесло сохранилось благодаря местным семьям.','["Według muzeum rzemiosło zachowało się dzięki lokalnym rodzinom.","Według muzeum rzemiosłem zachowali lokalne rodziny.","Muzeum natomiast zachować rzemiosło rodzin."]',0,'Według + родительный и dzięki + дательный.',4),
('b1region-grammar','Составьте: Как природа, так и наследие выделяют этот регион.','["Zarówno przyroda, jak i dziedzictwo wyróżniają ten region.","Natomiast przyroda według dziedzictwa region.","Zarówno przyrodę i dziedzictwem wyróżnia."]',0,'Оба подлежащих соединены zarówno… jak i.',5),
('b1region-quiz','Что такое województwo?','["административный регион Польши","горный маршрут","народный костюм"]',0,'Это крупнейшая административная единица.',0),
('b1region-quiz','Region ___ z Czechami.','["graniczy","wyróżnia","zachowuje się do"]',0,'Graniczyć z — граничить с.',1),
('b1region-quiz','Według ___ muzeum otwarto w 1920 roku.','["kroniki","kronika","kroniką"]',0,'Według требует родительного.',2),
('b1region-quiz','Zarówno góry, ___ jeziora przyciągają turystów.','["jak i","natomiast","podczas"]',0,'Правильная парная конструкция.',3),
('b1region-quiz','Что означает dziedzictwo?','["наследие","граница","погода"]',0,'Это культурные и исторические ценности.',4),
('b1region-quiz','Centrum jest ruchliwe, ___ wsie są spokojne.','["natomiast","zarówno","według"]',0,'Нужен контраст.',5),
('b1region-quiz','Które połączenie jest naturalne?','["zachować tradycję","graniczyć krajobraz","wyróżniać gwarą do"]',0,'Zachować tradycję — сохранить традицию.',6),
('b1region-quiz','Как корректно сослаться на источник?','["Według lokalnego archiwum…","Każdy na pewno wie…","Bez żadnych danych…"]',0,'Первый вариант прозрачно называет источник.',7),
('b1region-quiz','W przeciwieństwie ___ miasta wieś nie ma tramwajów.','["do","dla","nad"]',0,'Фиксированное управление do.',8),
('b1region-quiz','Które zdanie porównuje dwa źródła?','["Przewodnik podkreśla krajobraz, natomiast muzeum opisuje rzemiosło.","Źródło jest źródłem.","Region leży."]',0,'Первый вариант сопоставляет акценты.',9),
('b1region-reading-check','Gdzie planowała wyjazd Kasia?','["W Beskid Niski","Nad Bałtyk","Do Warszawy"]',0,'Она выбрала Бескид Ниски.',0),
('b1region-reading-check','Co podkreślał przewodnik?','["Szlaki i krajobraz","Wyłącznie przemysł","Ceny mieszkań"]',0,'Путеводитель был ориентирован на маршруты.',1),
('b1region-reading-check','Na czym skupiało się muzeum?','["Na dziedzictwie i rzemiośle","Na rozkładzie pociągów","Na pogodzie"]',0,'Музей рассказывал о наследии.',2),
('b1region-reading-check','Kogo spotkała Kasia?','["Rzemieślniczkę","Burmistrza Warszawy","Pilota"]',0,'Она посетила семейную мастерскую.',3),
('b1region-reading-check','Dlaczego oba źródła były przydatne?','["Miały różne, uzupełniające się cele","Powtarzały dokładnie to samo","Nie zawierały informacji"]',0,'Источники дополняли друг друга.',4),
('b1region-reading-check','Jaki jest wniosek?','["Pełny obraz wymaga kilku perspektyw","Wystarcza jeden nagłówek","Tradycje nie mają znaczenia"]',0,'Вывод — сравнивать перспективы.',5);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values ('b1region-dwa-spojrzenia-na-beskid','b1-poland-regions','Dwa spojrzenia na Beskid Niski','Как сопоставить путеводитель и местный музей','B1',9,'🗺️','["Kasia planowała weekend w Beskidzie Niskim, regionie, który graniczy ze Słowacją. Według internetowego przewodnika jego największą zaletą są spokojne szlaki, łagodne przełęcze i krajobraz bez dużych kurortów. Autor polecał przede wszystkim długie wycieczki piesze.","Kasia sprawdziła też stronę lokalnego muzeum. W przeciwieństwie do przewodnika muzeum mniej pisało o trasach, natomiast dokładnie przedstawiało dziedzictwo mieszkańców: drewnianą zabudowę, dawne rzemiosło oraz słowa zachowane w miejscowej gwarze.","Na miejscu odwiedziła zarówno małą wystawę, jak i rodzinny warsztat. Rzemieślniczka wyjaśniła, że region wyróżnia się nie tylko krajobrazem. Ważne są również historie rodzin, które przez pokolenia zachowywały umiejętności i dzieliły się nimi z młodszymi.","Oba źródła okazały się przydatne, chociaż każde miało inny cel. Przewodnik pomógł zaplanować szlak, podczas gdy muzeum pozwoliło lepiej zrozumieć ludzi i tradycje. Kasia uznała, że pełny obraz regionu powstaje dopiero wtedy, gdy porównuje się informacje z kilku perspektyw."]','{"graniczy":{"lemma":"graniczyć","translation":"граничит","part_of_speech":"глагол"},"zaletą":{"lemma":"zaleta","translation":"преимущество","part_of_speech":"существительное"},"łagodne":{"lemma":"łagodny","translation":"пологий","part_of_speech":"прилагательное"},"kurortów":{"lemma":"kurort","translation":"курорт","part_of_speech":"существительное"},"dawne":{"lemma":"dawny","translation":"старинный","part_of_speech":"прилагательное"},"zabudowę":{"lemma":"zabudowa","translation":"застройка","part_of_speech":"существительное"},"zachowane":{"lemma":"zachować","translation":"сохранённые","part_of_speech":"причастие"},"gwarze":{"lemma":"gwara","translation":"диалект","part_of_speech":"существительное"},"warsztat":{"lemma":"warsztat","translation":"мастерская","part_of_speech":"существительное"},"rzemieślniczka":{"lemma":"rzemieślniczka","translation":"мастерица","part_of_speech":"существительное"},"pokolenia":{"lemma":"pokolenie","translation":"поколение","part_of_speech":"существительное"},"umiejętności":{"lemma":"umiejętność","translation":"умение","part_of_speech":"существительное"},"perspektyw":{"lemma":"perspektywa","translation":"перспектива","part_of_speech":"существительное"},"pełny":{"lemma":"pełny","translation":"полный","part_of_speech":"прилагательное"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30","comprehension_lesson_id":"b1region-reading-check"}',34,true) on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;

insert into public.topics(id,course_id,title,description,emoji,position,is_active) values ('b1-final-project','b1-independent','Проект B1','Интегрируем рассказ, письмо, чтение и аргументированное обсуждение','🏁',11,true) on conflict(id) do update set course_id=excluded.course_id,title=excluded.title,description=excluded.description,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active;

insert into public.lessons(id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,position,is_active,theory_title,theory_sections,source_metadata) values
('b1final-words','b1-final-project','words','Słowa w kontekście','Новая лексика','8 карточек · B1','Интегрируем рассказ, письмо, чтение и аргументированное обсуждение',9,'🏁',163,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-grammar','b1-final-project','grammar','Jak to wyrazić?','Языковой фокус','6 заданий · B1','Связный проект B1',12,'✏️',164,true,'Связный проект B1','[["Структура","Сначала обозначь цель, затем аргументы и пример, в конце — вывод."],["Письмо","Соблюдай обращение, абзацы, нейтральный регистр и заключительную формулу."],["Самопроверка","Проверь времена, связки, падежи и то, отвечает ли текст задаче."]]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-review','b1-final-project','review','Powtórka aktywna','Активное повторение','7 карточек · B1','Закрепи лексику темы',8,'🔄',165,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-quiz','b1-final-project','quiz','Quiz: Проект B1','Проверка темы','10 вопросов · B1','Проверь лексику и связность',9,'🎯',166,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-reading-check','b1-final-project','quiz','Czy rozumiesz tekst?','Понимание текста','6 вопросов · B1','Найди детали и главный вывод',7,'📖',167,true,'','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}')
on conflict(id) do update set topic_id=excluded.topic_id,kind=excluded.kind,title=excluded.title,plan_title=excluded.plan_title,subtitle=excluded.subtitle,description=excluded.description,minutes=excluded.minutes,emoji=excluded.emoji,position=excluded.position,is_active=excluded.is_active,theory_title=excluded.theory_title,theory_sections=excluded.theory_sections,source_metadata=excluded.source_metadata;

insert into public.flashcards(id,polish,translation,example,position,is_active,source_metadata) values
('b1final-1','cel','цель','Najpierw określ cel wypowiedzi.',527,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-2','odbiorca','адресат','Dostosuj styl do odbiorcy.',528,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-3','wstęp','введение','Krótki wstęp przedstawia temat.',529,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-4','argument','аргумент','Każdy argument poprzyj przykładem.',530,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-5','przykład','пример','Konkretny przykład wzmacnia opinię.',531,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-6','wniosek','вывод','Na końcu sformułuj wniosek.',532,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-7','akapit','абзац','Nowa myśl zaczyna nowy akapit.',533,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-8','spójny','связный','Tekst jest spójny i logiczny.',534,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-9','uzasadnić','обосновать','Uzasadnij swoją propozycję.',535,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-10','podsumować','подвести итог','Podsumuj najważniejsze informacje.',536,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-11','odnieść się do','сослаться на','Odnieś się do opinii rozmówcy.',537,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-12','zaproponować','предложить','Zaproponuj realistyczne rozwiązanie.',538,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-13','formalny','официальный','W urzędzie wybierz formalny styl.',539,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-14','poprawić','исправить','Przeczytaj tekst i popraw błędy.',540,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}'),
('b1final-15','kryterium','критерий','Każde kryterium jest jasno opisane.',541,true,'{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30"}')
on conflict(id) do update set polish=excluded.polish,translation=excluded.translation,example=excluded.example,position=excluded.position,is_active=excluded.is_active,source_metadata=excluded.source_metadata;

delete from public.lesson_flashcards where lesson_id in ('b1final-words','b1final-review');

insert into public.lesson_flashcards(lesson_id,flashcard_id,position) values
('b1final-words','b1final-1',0),
('b1final-words','b1final-2',1),
('b1final-words','b1final-3',2),
('b1final-words','b1final-4',3),
('b1final-words','b1final-5',4),
('b1final-words','b1final-6',5),
('b1final-words','b1final-7',6),
('b1final-words','b1final-8',7),
('b1final-review','b1final-9',0),
('b1final-review','b1final-10',1),
('b1final-review','b1final-11',2),
('b1final-review','b1final-12',3),
('b1final-review','b1final-13',4),
('b1final-review','b1final-14',5),
('b1final-review','b1final-15',6);

delete from public.questions where lesson_id in ('b1final-grammar','b1final-quiz','b1final-reading-check');

insert into public.questions(lesson_id,prompt,options,correct,explanation,position) values
('b1final-grammar','Dobre wystąpienie zaczyna się od jasnego ___.','["celu","celem","cel"]',0,'Od требует родительного падежа.',0),
('b1final-grammar','Najpierw przedstaw problem, ___ podaj argument i przykład.','["następnie","ponieważ","chociaż"]',0,'Następnie организует последовательность.',1),
('b1final-grammar','W oficjalnym e-mailu napisz: ___.','["Szanowni Państwo, zwracam się z prośbą…","Hej, zróbcie to szybko!","No więc mam sprawę."]',0,'Первый вариант соответствует официальному регистру.',2),
('b1final-grammar','Odniosę się ___ argumentu poprzedniej osoby.','["do","na","z"]',0,'Odnieść się do требует родительного.',3),
('b1final-grammar','Составьте: В заключение я предлагаю решение, которое принесёт пользу жителям.','["Podsumowując, proponuję rozwiązanie, które przyniesie korzyść mieszkańcom.","Podsumowanie proponuje mieszkańcy korzyścią rozwiązanie.","Chociaż rozwiązanie, więc mieszkańcom."]',0,'Podsumowując вводит вывод, a które связывает описание.',4),
('b1final-grammar','Составьте: Прежде чем отправить письмо, проверь структуру и исправь ошибки.','["Zanim wyślesz wiadomość, sprawdź strukturę i popraw błędy.","Zanim wysłać wiadomość, poprawił struktury błędy.","Po wysłaniu zanim wiadomość sprawdza."]',0,'После zanim используются личные формы будущего/настоящего.',5),
('b1final-quiz','Что должно быть во введении?','["тема и цель","все детали сразу","только прощание"]',0,'Введение ориентирует адресата.',0),
('b1final-quiz','Każdy argument warto poprzeć ___.','["przykładem","odbiorcy","akapitu"]',0,'Poprzeć czym требует творительного.',1),
('b1final-quiz','Jak zakończyć formalny e-mail?','["Z poważaniem","Pa!","Do zobaczyska"]',0,'Z poważaniem — нейтральная формальная формула.',2),
('b1final-quiz','Odnieść się ___ opinii rozmówcy.','["do","za","przez"]',0,'Правильное управление do.',3),
('b1final-quiz','Co oznacza spójny tekst?','["мысли логически связаны","в нём нет абзацев","он состоит из одного слова"]',0,'Связность — логическая связь частей.',4),
('b1final-quiz','Najpierw cel, ___ argumenty, na końcu wniosek.','["następnie","mimo że","ponieważ"]',0,'Маркер последовательности.',5),
('b1final-quiz','Który element wzmacnia opinię?','["konkretny przykład","повтор без причины","смена темы"]',0,'Пример поддерживает аргумент.',6),
('b1final-quiz','Какое действие относится к самопроверке?','["poprawić błędy","usunąć wniosek","pominąć zadanie"]',0,'Нужно исправить ошибки.',7),
('b1final-quiz','Dostosuj styl do ___.','["odbiorcy","odbiorcą","odbiorcę"]',0,'Do требует родительного.',8),
('b1final-quiz','Który wniosek jest dobry?','["Podsumowując, rozwiązanie jest możliwe, jeśli podzielimy zadania.","To wszystko, bo tak.","Nie pamiętam tematu."]',0,'Первый вывод резюмирует и уточняет условие.',9),
('b1final-reading-check','Jaki temat wybrała Marta?','["Miejsce spotkań dla młodych","Budowę lotniska","Recenzję filmu"]',0,'Это тема итогового проекта.',0),
('b1final-reading-check','Jakie źródła przeczytała?','["Raport i artykuł o podobnej inicjatywie","Tylko komentarze","Powieść i wiersz"]',0,'Она использовала два разных источника.',1),
('b1final-reading-check','Jak zbudowała e-mail?','["Cel, argumenty z przykładami i prośba","Jedno zdanie bez celu","Same pytania"]',0,'Письмо имело ясную структуру.',2),
('b1final-reading-check','Co zrobiła przed wysłaniem?','["Sprawdziła kryteria i poprawiła błędy","Usunęła wniosek","Zmieniła temat"]',0,'Она провела самопроверку.',3),
('b1final-reading-check','Jak zareagowała na sprzeciw?','["Spokojnie odpowiedziała i zaproponowała porównanie","Przerwała prezentację","Zignorowała rozmówcę"]',0,'Она вступила в конструктивное обсуждение.',4),
('b1final-reading-check','Co łączy spójna wypowiedź?','["Źródła, strukturę i dialog","Tylko trudne słowa","Brak przykładów"]',0,'Это итоговый вывод текста.',5);

insert into public.reading_texts(id,topic_id,title,description,level,minutes,emoji,paragraphs,glossary,source_metadata,position,is_active) values ('b1final-projekt-marty','b1-final-project','Projekt Marty: miejsce dla młodych','Итоговый проект: от чтения источников до письма и обсуждения','B1',10,'🏁','["Marta przygotowywała projekt końcowy kursu. Wybrała temat miejsca spotkań dla młodych mieszkańców. Jej celem było nie tylko opisanie problemu, lecz także zaproponowanie rozwiązania, które można przedstawić radzie dzielnicy.","Najpierw przeczytała dwa źródła: raport o potrzebach młodzieży i artykuł o podobnej inicjatywie w innym mieście. W osobnych akapitach podsumowała najważniejsze dane, porównała opinie i odniosła się do argumentu o kosztach.","Następnie napisała formalny e-mail. We wstępie określiła cel, później uzasadniła propozycję konkretnymi przykładami, a w ostatnim akapicie poprosiła o spotkanie. Przed wysłaniem sprawdziła każde kryterium, poprawiła błędy i uprościła zbyt długie zdania.","Podczas prezentacji jedna osoba nie zgodziła się z lokalizacją. Marta spokojnie odniosła się do tej opinii i zaproponowała wspólne porównanie dwóch miejsc. W podsumowaniu grupa przyjęła realistyczny plan. Projekt pokazał Marcie, że spójna wypowiedź łączy źródła, jasną strukturę i gotowość do rozmowy."]','{"końcowy":{"lemma":"końcowy","translation":"итоговый","part_of_speech":"прилагательное"},"lecz":{"lemma":"lecz","translation":"но","part_of_speech":"союз"},"radzie":{"lemma":"rada","translation":"совет","part_of_speech":"существительное"},"raport":{"lemma":"raport","translation":"отчёт","part_of_speech":"существительное"},"podsumowała":{"lemma":"podsumować","translation":"подвела итог","part_of_speech":"глагол"},"odniosła się":{"lemma":"odnieść się","translation":"сослалась","part_of_speech":"глагол"},"kosztach":{"lemma":"koszt","translation":"расходы","part_of_speech":"существительное"},"określiła":{"lemma":"określić","translation":"определила","part_of_speech":"глагол"},"uzasadniła":{"lemma":"uzasadnić","translation":"обосновала","part_of_speech":"глагол"},"kryterium":{"lemma":"kryterium","translation":"критерий","part_of_speech":"существительное"},"uprościła":{"lemma":"uprościć","translation":"упростила","part_of_speech":"глагол"},"lokalizacją":{"lemma":"lokalizacja","translation":"местоположение","part_of_speech":"существительное"},"przyjęła":{"lemma":"przyjąć","translation":"приняла","part_of_speech":"глагол"},"gotowość":{"lemma":"gotowość","translation":"готовность","part_of_speech":"существительное"}}','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-30","comprehension_lesson_id":"b1final-reading-check"}',35,true) on conflict(id) do update set topic_id=excluded.topic_id,title=excluded.title,description=excluded.description,level=excluded.level,minutes=excluded.minutes,emoji=excluded.emoji,paragraphs=excluded.paragraphs,glossary=excluded.glossary,source_metadata=excluded.source_metadata,position=excluded.position,is_active=excluded.is_active;
