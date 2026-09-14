begin;

update public.questions set explanation = 'Przysłówek „prawdopodobnie” przedstawia przyczynę jako hipotezę, ponieważ nie znamy wszystkich okoliczności.'
where lesson_id = 'b2psych-grammar' and position = 0;

update public.questions set explanation = 'Konstrukcja „wydawało się” opisuje subiektywną ocenę sytuacji z perspektywy konkretnej osoby.'
where lesson_id = 'b2psych-grammar' and position = 1;

update public.questions set explanation = 'Po czasowniku modalnym „mogła” występuje bezokolicznik „powiedzieć”, który nazywa niewykorzystaną możliwość.'
where lesson_id = 'b2psych-grammar' and position = 2;

update public.questions set explanation = 'Wyrażenie „być może” oddziela ostrożne przypuszczenie od pewnego stwierdzenia o cudzych intencjach.'
where lesson_id = 'b2psych-grammar' and position = 3;

update public.questions set explanation = '„Prawdopodobnie” sygnalizuje hipotezę, a „ponieważ” wprowadza możliwą przyczynę jej wycofania.'
where lesson_id = 'b2psych-grammar' and position = 4;

update public.questions set explanation = 'Zwrot „z jego perspektywy” ogranicza ocenę do punktu widzenia jednej osoby.'
where lesson_id = 'b2psych-grammar' and position = 5;

update public.questions set explanation = 'Stawianie granic polega na jasnym komunikowaniu potrzeb i zachowań akceptowanych w relacji.'
where lesson_id = 'b2psych-quiz' and position = 0;

update public.questions set explanation = '„Być może” wyraża możliwość, dlatego nie przedstawia domysłu jako bezspornego faktu.'
where lesson_id = 'b2psych-quiz' and position = 1;

update public.questions set explanation = 'Czasownik „przypisywać” łączy się z celownikiem osoby i biernikiem przypisywanej cechy.'
where lesson_id = 'b2psych-quiz' and position = 2;

update public.questions set explanation = 'Nazwanie emocji i krótka przerwa pomagają obniżyć napięcie przed udzieleniem odpowiedzi.'
where lesson_id = 'b2psych-quiz' and position = 3;

update public.questions set explanation = 'Forma „mogła powiedzieć” wskazuje na alternatywny sposób zachowania dostępny w przeszłości.'
where lesson_id = 'b2psych-quiz' and position = 4;

update public.questions set explanation = '„Prawdopodobnie” wyraźnie ogranicza pewność sądu i pozostawia miejsce na inne wyjaśnienia.'
where lesson_id = 'b2psych-quiz' and position = 5;

update public.questions set explanation = 'Stałe połączenie „dojść do porozumienia” oznacza osiągnąć wspólne stanowisko po rozmowie.'
where lesson_id = 'b2psych-quiz' and position = 6;

update public.questions set explanation = 'Żal wynika z niezauważonej potrzeby, więc zdanie podaje konkretną przyczynę emocji.'
where lesson_id = 'b2psych-quiz' and position = 7;

update public.questions set explanation = 'Empatyczna reakcja nazywa możliwe uczucie rozmówcy bez oceniania go ani narzucania interpretacji.'
where lesson_id = 'b2psych-quiz' and position = 8;

update public.questions set explanation = 'Zwrot „z jej perspektywy” przedstawia sytuację z punktu widzenia wskazanej osoby.'
where lesson_id = 'b2psych-quiz' and position = 9;

update public.questions set explanation = 'Lena czuła żal, ponieważ decyzje dotyczące wspólnego wyjazdu podjęto bez jej udziału.'
where lesson_id = 'b2psych-reading-check' and position = 0;

update public.questions set explanation = 'Tekst ostrożnie sugeruje, że Michał unikał konfrontacji z obawy przed impulsywną reakcją.'
where lesson_id = 'b2psych-reading-check' and position = 1;

update public.questions set explanation = 'Ustalona zasada oddziela obserwację od emocji i potrzeb, ograniczając wzajemne oskarżenia.'
where lesson_id = 'b2psych-reading-check' and position = 2;

update public.questions set explanation = 'Michał przyznał, że nie zapytał Leny o zdanie przed podjęciem wspólnej decyzji.'
where lesson_id = 'b2psych-reading-check' and position = 3;

update public.questions set explanation = 'Lena jasno zakomunikowała potrzebę uczestniczenia w decyzjach dotyczących ich wspólnych planów.'
where lesson_id = 'b2psych-reading-check' and position = 4;

update public.questions set explanation = 'Ostrożna modalność pomaga odróżnić opisane fakty od przypuszczeń o motywach bohaterów.'
where lesson_id = 'b2psych-reading-check' and position = 5;

update public.questions set explanation = 'Konstrukcja „odczytać jako” służy przedstawieniu uzasadnionej interpretacji obrazu lub motywu.'
where lesson_id = 'b2lit-grammar' and position = 0;

update public.questions set explanation = 'W mowie zależnej zmieniamy „nie znam” na formę „nie zna” zgodną z narratorką.'
where lesson_id = 'b2lit-grammar' and position = 1;

update public.questions set explanation = 'Spójnik „aby” wprowadza cel przywołania obrazu pustego peronu przez reżysera.'
where lesson_id = 'b2lit-grammar' and position = 2;

update public.questions set explanation = 'Wyrażenie „dzięki temu” wskazuje skutek niejednoznacznego finału: możliwość własnej interpretacji.'
where lesson_id = 'b2lit-grammar' and position = 3;

update public.questions set explanation = 'Zwrot „można odczytać jako” ostrożnie proponuje symboliczne znaczenie obrazu, nie ogłasza pewnika.'
where lesson_id = 'b2lit-grammar' and position = 4;

update public.questions set explanation = 'Mowa zależna zachowuje zapowiedź powrotu, a „poddaje w wątpliwość” sygnalizuje dystans narratora.'
where lesson_id = 'b2lit-grammar' and position = 5;

update public.questions set explanation = 'Fabuła to uporządkowany ciąg wydarzeń przedstawionych w dziele literackim albo filmowym.'
where lesson_id = 'b2lit-quiz' and position = 0;

update public.questions set explanation = 'Zdanie o pustym peronie wyjaśnia możliwe znaczenie obrazu, dlatego jest interpretacją.'
where lesson_id = 'b2lit-quiz' and position = 1;

update public.questions set explanation = 'Cytat wspiera argument tylko wtedy, gdy recenzent objaśnia jego znaczenie w kontekście.'
where lesson_id = 'b2lit-quiz' and position = 2;

update public.questions set explanation = 'Tempo, montaż i ograniczanie informacji sterują oczekiwaniami widza, dzięki czemu budują napięcie.'
where lesson_id = 'b2lit-quiz' and position = 3;

update public.questions set explanation = 'Niejednoznaczny finał pozostawia kilka interpretacji, o ile każdą można uzasadnić elementami dzieła.'
where lesson_id = 'b2lit-quiz' and position = 4;

update public.questions set explanation = 'Czasownik „odwoływać się” wymaga przyimka „do” i wskazuje świadome nawiązanie do legendy.'
where lesson_id = 'b2lit-quiz' and position = 5;

update public.questions set explanation = 'W mowie zależnej forma „nie wróci” zachowuje przyszłe znaczenie pierwotnej wypowiedzi bohatera.'
where lesson_id = 'b2lit-quiz' and position = 6;

update public.questions set explanation = 'Przekonująca recenzja łączy tezę z przykładami oraz wyjaśnia podstawę sformułowanej oceny.'
where lesson_id = 'b2lit-quiz' and position = 7;

update public.questions set explanation = 'Warstwa wizualna obejmuje kolor, kadr, światło i kompozycję widocznego obrazu filmowego.'
where lesson_id = 'b2lit-quiz' and position = 8;

update public.questions set explanation = 'Formuła „można interpretować jako” zaznacza, że proponowane odczytanie nie jest jedynym możliwym.'
where lesson_id = 'b2lit-quiz' and position = 9;

update public.questions set explanation = 'Ida wraca do miasta, aby uporządkować mieszkanie pozostałe po zmarłym dziadku.'
where lesson_id = 'b2lit-reading-check' and position = 0;

update public.questions set explanation = 'Powracające światło na peronie można odczytać jako oczekiwanie i próbę nawiązania kontaktu.'
where lesson_id = 'b2lit-reading-check' and position = 1;

update public.questions set explanation = 'Film buduje napięcie krótkimi rozmowami oraz wiadomościami urwanymi przed pełnym wyjaśnieniem.'
where lesson_id = 'b2lit-reading-check' and position = 2;

update public.questions set explanation = 'Wiadomość ujawnia, że siostra również próbowała nawiązać kontakt, co zmienia ocenę milczenia.'
where lesson_id = 'b2lit-reading-check' and position = 3;

update public.questions set explanation = 'Finał pozostaje otwarty, ponieważ widz nie dowiaduje się, kto nadchodzi w ciemności.'
where lesson_id = 'b2lit-reading-check' and position = 4;

update public.questions set explanation = 'Recenzent uznaje zakończenie za spójne z powracającymi obrazami oraz głównym tematem pamięci.'
where lesson_id = 'b2lit-reading-check' and position = 5;

commit;
