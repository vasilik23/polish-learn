-- Keep the C1 final-project editorial pass rerunnable and content-only.
update public.flashcards as flashcard
set example = editorial.example
from (
  values
    ('c110-1', 'Zakres projektu obejmuje analizę danych, konsultacje z mieszkańcami oraz przygotowanie trzech wersji rekomendacji.'),
    ('c110-2', 'Pytanie przewodnie porządkuje badanie: jak miasto może skutecznie ostrzegać seniorów przed falami upałów?'),
    ('c110-3', 'Triangulacja źródeł ujawniła różnicę między statystykami urzędu, relacjami mieszkańców i obserwacjami terenowymi.'),
    ('c110-4', 'Kryterium oceny prezentacji było jasne: każdy wniosek musiał wynikać z co najmniej dwóch źródeł.'),
    ('c110-5', 'Synteza ustaleń połączyła dane liczbowe z wywiadami, nie zacierając sprzeczności między nimi.'),
    ('c110-6', 'Wersja dla odbiorcy publicznego zastąpiła terminologię badawczą krótkimi instrukcjami i czytelną infografiką.'),
    ('c110-7', 'Obrona projektu rozpoczęła się od przedstawienia metody, a zakończyła odpowiedziami na pytania komisji.'),
    ('c110-8', 'Aby odpowiedzieć na zarzut o małej próbie, badaczka wskazała ograniczenia i zaproponowała kolejne pomiary.'),
    ('c110-9', 'Autorzy postanowili uznać ograniczenie badania, zamiast przedstawiać lokalne wyniki jako uniwersalną prawidłowość.'),
    ('c110-10', 'Wniosek warunkowy zaznaczał, że rozwiązanie zadziała, o ile mieszkańcy otrzymają komunikaty odpowiednio wcześnie.'),
    ('c110-11', 'Materiał pomocniczy zawierał mapę punktów chłodzenia, definicje wskaźników i skróconą bibliografię projektu.'),
    ('c110-12', 'Próba generalna wykazała, że wykres wymaga objaśnienia, a końcowa rekomendacja powinna być krótsza.'),
    ('c110-13', 'Informacja zwrotna od seniorów skłoniła zespół do powiększenia czcionki i uproszczenia instrukcji.'),
    ('c110-14', 'Samoocena pozwoliła każdej osobie nazwać własny wkład, trudność oraz umiejętność wymagającą dalszej pracy.'),
    ('c110-15', 'Dalszy kierunek projektu zakłada test komunikatów z użytkownikami i porównanie reakcji różnych grup odbiorców.')
) as editorial(id, example)
where flashcard.id = editorial.id;

update public.questions as question
set explanation = editorial.explanation
from (
  values
    ('c110-grammar', 0, 'Zakres projektu wyznacza, które problemy, grupy odbiorców i działania należą do badania, a które pozostają poza nim.'),
    ('c110-grammar', 1, 'Pytanie przewodnie skupia cały projekt na jednym rozstrzygalnym problemie i pomaga wybierać tylko potrzebne dane.'),
    ('c110-grammar', 2, 'Triangulacja źródeł polega na zestawieniu różnych rodzajów dowodów, aby sprawdzić zgodność wyników i zauważyć rozbieżności.'),
    ('c110-grammar', 3, 'Kryterium oceny opisuje mierzalny warunek jakości, dzięki któremu autor i odbiorca wiedzą, jak ocenić rezultat.'),
    ('c110-grammar', 4, 'Synteza ustaleń nie jest listą streszczeń: łączy dowody w spójny obraz, zachowując ważne różnice i zastrzeżenia.'),
    ('c110-grammar', 5, 'Wersja dla odbiorcy dostosowuje język, szczegółowość i formę przekazu do wiedzy oraz potrzeb konkretnej grupy.'),
    ('c110-quiz', 0, 'Zakres projektu określa granice przedsięwzięcia: jego temat, działania, odbiorców i kwestie świadomie wyłączone z analizy.'),
    ('c110-quiz', 1, 'Pytanie przewodnie nadaje kierunek zbieraniu materiału i pozwala ocenić, czy poszczególne działania służą celowi projektu.'),
    ('c110-quiz', 2, 'Triangulacja źródeł zwiększa wiarygodność analizy przez porównanie danych, dokumentów i relacji uzyskanych różnymi metodami.'),
    ('c110-quiz', 3, 'Kryterium oceny to wcześniej ustalony standard, według którego można przejrzyście ocenić proces albo końcowy rezultat.'),
    ('c110-quiz', 4, 'Synteza ustaleń zestawia najważniejsze wyniki, wskazuje ich relacje i prowadzi do wniosku odpowiadającego na pytanie przewodnie.'),
    ('c110-quiz', 5, 'Wersja dla odbiorcy przekazuje te same ustalenia w formie odpowiedniej dla danej grupy, bez zniekształcania ich sensu.'),
    ('c110-quiz', 6, 'Obrona projektu wymaga uzasadnienia decyzji, przedstawienia dowodów oraz rzeczowej reakcji na pytania i krytyczne uwagi.'),
    ('c110-quiz', 7, 'Odpowiedzieć na zarzut to odnieść się bezpośrednio do podanej wątpliwości za pomocą argumentu, dowodu albo uczciwego zastrzeżenia.'),
    ('c110-quiz', 8, 'Uznać ograniczenie oznacza jasno wskazać słabość metody lub danych i odpowiednio zawęzić siłę formułowanego wniosku.'),
    ('c110-quiz', 9, 'Wniosek warunkowy obowiązuje tylko przy spełnieniu wskazanego warunku, dlatego unika nieuzasadnionego uogólnienia wyników.'),
    ('c110-reading-check', 0, 'Trzeci akapit wymienia raport analityczny, krótką informację publiczną oraz prezentację przygotowaną specjalnie dla osób starszych.'),
    ('c110-reading-check', 1, 'Pierwszy akapit określa problem projektu: zespół bada sposób jasnego informowania mieszkańców o falach upałów.'),
    ('c110-reading-check', 2, 'Drugi akapit opisuje triangulację: uczestnicy porównują dane, komunikaty i wywiady, zachowując widoczne między nimi rozbieżności.'),
    ('c110-reading-check', 3, 'Trzeci akapit pokazuje mediację wyników przez przygotowanie trzech odmiennych formatów dla różnych sytuacji i odbiorców.'),
    ('c110-reading-check', 4, 'Czwarty akapit przedstawia dojrzałą obronę: zespół odpowiada na zarzut, uznaje ograniczenie i zawęża wniosek.'),
    ('c110-reading-check', 5, 'Piąty akapit podsumowuje samoocenę projektu i wyznacza dalszy kierunek w postaci testów z rzeczywistymi użytkownikami.')
) as editorial(lesson_id, position, explanation)
where question.lesson_id = editorial.lesson_id
  and question.position = editorial.position;
