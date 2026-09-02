-- Keep the C1 professional-expertise editorial pass rerunnable and content-only.
update public.flashcards as flashcard
set example = editorial.example
from (values
  ('c16-1', 'Przed rozpoczęciem negocjacji kierowniczka jasno określiła zakres odpowiedzialności każdego zespołu za migrację danych.'),
  ('c16-2', 'Brak dostępu do archiwalnego systemu stanowił warunek brzegowy, który wykluczał wdrożenie w pierwotnym terminie.'),
  ('c16-3', 'Najpoważniejsze ryzyko operacyjne polegało na przerwaniu obsługi klientów podczas przełączania serwerów.'),
  ('c16-4', 'Eksperci ocenili wykonalność planu dopiero po sprawdzeniu dostępnych zasobów, terminów i zależności technicznych.'),
  ('c16-5', 'Obie strony musiały uzgodnić kryteria odbioru, zanim wykonawca rozpoczął prace nad kolejnym etapem.'),
  ('c16-6', 'Aby przedstawić rekomendację zarządowi, analityczka porównała koszty, korzyści oraz ryzyka trzech wariantów.'),
  ('c16-7', 'Prawniczka poprosiła, by w umowie zastrzec poufność danych ujawnianych podczas audytu bezpieczeństwa.'),
  ('c16-8', 'Zespół przygotował wariant awaryjny na wypadek, gdyby testy wydajnościowe nie spełniły ustalonego progu.'),
  ('c16-9', 'Przed zatwierdzeniem harmonogramu trzeba oszacować nakład pracy potrzebny na migrację i kontrolę jakości.'),
  ('c16-10', 'Rozbieżność między raportem finansowym a danymi operacyjnymi wymagała wspólnego sprawdzenia założeń obu działów.'),
  ('c16-11', 'Partnerom udało się wynegocjować dodatkowy tydzień testów bez przesuwania daty uruchomienia usługi.'),
  ('c16-12', 'Niejasny podział zadań mógł doprowadzić do eskalacji konfliktu między dostawcą a zespołem klienta.'),
  ('c16-13', 'Po pilotażu nastąpi punkt decyzyjny, w którym rada wybierze wdrożenie pełne albo ograniczone.'),
  ('c16-14', 'Za mierzalny rezultat uznano skrócenie czasu obsługi zgłoszenia o co najmniej dwadzieścia procent.'),
  ('c16-15', 'Umowa wskazuje, że odpowiedzialność końcowa za zgodność rozwiązania z prawem pozostaje po stronie zamawiającego.')
) as editorial(id, example)
where flashcard.id = editorial.id;

update public.questions as question
set explanation = editorial.explanation
from (values
  ('c16-grammar', 0, 'Zakres odpowiedzialności precyzuje, za jakie decyzje, działania i rezultaty odpowiada dana osoba albo zespół; zapobiega to lukom kompetencyjnym.'),
  ('c16-grammar', 1, 'Warunek brzegowy wyznacza ograniczenie, którego projekt nie może naruszyć, na przykład nieprzekraczalny termin, budżet lub wymóg prawny.'),
  ('c16-grammar', 2, 'Ryzyko operacyjne dotyczy zakłócenia bieżącego działania organizacji, dlatego opisuje się jego przyczynę, prawdopodobieństwo oraz możliwy skutek.'),
  ('c16-grammar', 3, 'Wykonalność ocenia, czy plan da się rzeczywiście zrealizować przy dostępnych zasobach, czasie, technologii i obowiązujących ograniczeniach.'),
  ('c16-grammar', 4, 'Uzgodnić kryteria znaczy wspólnie ustalić mierzalne warunki, według których strony później rozpoznają poprawne wykonanie zadania.'),
  ('c16-grammar', 5, 'Przedstawić rekomendację to wskazać preferowane rozwiązanie i uzasadnić je dowodami, porównaniem wariantów oraz jawnymi zastrzeżeniami.'),
  ('c16-quiz', 0, 'Zakres odpowiedzialności rozdziela obowiązki i uprawnienia między uczestników projektu, dzięki czemu wiadomo, kto podejmuje decyzję i odpowiada za wynik.'),
  ('c16-quiz', 1, 'Warunek brzegowy jest granicą dopuszczalnego rozwiązania; wariant, który go nie spełnia, odpada niezależnie od innych korzyści.'),
  ('c16-quiz', 2, 'Ryzyko operacyjne nazywa możliwość zakłócenia procesów, systemów lub obsługi, a nie samą niepewność dotyczącą strategii organizacji.'),
  ('c16-quiz', 3, 'Wykonalność nie oznacza atrakcyjności pomysłu, lecz możliwość jego realizacji po uwzględnieniu zasobów, zależności i ograniczeń.'),
  ('c16-quiz', 4, 'Uzgodnić kryteria należy przed odbiorem pracy, aby obie strony stosowały te same, możliwe do sprawdzenia miary sukcesu.'),
  ('c16-quiz', 5, 'Rekomendacja łączy proponowane działanie z argumentami i ryzykiem; sama prezentacja danych nie wskazuje jeszcze, który wariant wybrać.'),
  ('c16-quiz', 6, 'Zastrzec poufność oznacza wyraźnie ograniczyć ujawnianie informacji oraz ustalić, kto i w jakim celu może z nich korzystać.'),
  ('c16-quiz', 7, 'Wariant awaryjny opisuje alternatywne działanie uruchamiane po wystąpieniu określonego problemu, a nie dowolną zmianę pierwotnego planu.'),
  ('c16-quiz', 8, 'Oszacować nakład to przewidzieć potrzebny czas, pracę i zasoby na podstawie dostępnych danych, z zaznaczeniem niepewności estymacji.'),
  ('c16-quiz', 9, 'Rozbieżność jest istotną różnicą między danymi, ocenami lub oczekiwaniami; w negocjacjach warto najpierw ustalić jej źródło.'),
  ('c16-reading-check', 0, 'Działy uzgodniły mierzalne kryteria i punkt decyzyjny, ponieważ te dwa elementy porządkowały ocenę wyniku oraz wybór dalszego działania.'),
  ('c16-reading-check', 1, 'Pierwszy akapit określa przedmiot rekomendacji, jej odbiorcę oraz dwa punkty wyjścia: warunki brzegowe i podział odpowiedzialności.'),
  ('c16-reading-check', 2, 'Drugi akapit pokazuje odpowiedzialne szacowanie: zamiast gwarancji bez problemów ekspertka podaje nakład, ryzyka i ich prawdopodobieństwo.'),
  ('c16-reading-check', 3, 'Trzeci akapit wyjaśnia, jak rozbieżne oczekiwania przełożono na wspólne kryteria oraz wyraźny moment podjęcia decyzji.'),
  ('c16-reading-check', 4, 'Czwarty akapit zawęża przedmiot negocjacji do kolejności, poufności i planu awaryjnego, podczas gdy sam cel pozostaje wspólny.'),
  ('c16-reading-check', 5, 'Ostatni akapit łączy stanowczą rekomendację z granicami ekspertyzy i wskazaniem odpowiedzialności, więc nie składa obietnicy bezwarunkowej.')
) as editorial(lesson_id, position, explanation)
where question.lesson_id = editorial.lesson_id
  and question.position = editorial.position;
