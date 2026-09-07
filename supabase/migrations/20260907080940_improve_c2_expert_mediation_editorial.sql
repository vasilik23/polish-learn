-- Keep the C2 expert-mediation editorial pass rerunnable and content-only.
update public.flashcards as flashcard set example = editorial.example
from (values
('c27-1','Mediatorka poprosiła każdą grupę o potwierdzenie parafrazy, zanim zapisała wspólne kryteria decyzji.'),
('c27-2','Wspólny mianownik znaleziono nie w gotowym rozwiązaniu, lecz w zgodzie na ograniczenie ryzyka dla pacjentów.'),
('c27-3','Rozbieżność stanowisk dotyczyła akceptowalnej liczby fałszywych alarmów, a nie samej potrzeby prowadzenia badań.'),
('c27-4','Interes strony został opisany jako potrzeba możliwie wczesnej diagnozy bez nadmiernego obciążania zdrowych osób.'),
('c27-5','Pole porozumienia poszerzyło się, gdy rozmówcy oddzielili wspólny cel od sporu o próg klasyfikacji.'),
('c27-6','Termin specjalistyczny „czułość” wyjaśniono liczbą chorych, których system może poprawnie wskazać lub przeoczyć.'),
('c27-7','Asymetria wiedzy utrudniała rozmowę, ponieważ pacjenci znali skutki alarmów, a informatycy ograniczenia modelu.'),
('c27-8','Warunek brzegowy zabraniał przenosić wyniki pilotażu z jednej poradni bezpośrednio na cały region.'),
('c27-9','Przed oceną wariantów strony musiały uzgodnić definicję bezpieczeństwa oraz sposób mierzenia każdego ryzyka.'),
('c27-10','Mediatorka pomogła przełożyć na język praktyki abstrakcyjny próg, pokazując jego wpływ na liczbę powiadomień.'),
('c27-11','Aby zneutralizować napięcie, prowadząca uznała obawy pacjentów i poprosiła ekspertów o podanie konkretnych konsekwencji.'),
('c27-12','Upraszczając opis modelu, trzeba zachować precyzję dotyczącą zakresu danych i niepewności prognozy.'),
('c27-13','Dobre pytanie pozwoliło wydobyć potrzebę kontroli nad powiadomieniami, ukrytą wcześniej pod ogólnym sprzeciwem.'),
('c27-14','Zespół próbował sformułować wariant pośredni: ograniczony pilotaż z częstą oceną i prawem rezygnacji z komunikatów.'),
('c27-15','Rolą prowadzącej było uporządkować konsekwencje, a nie rozstrzygać za strony, jaki poziom ryzyka zaakceptować.')
) editorial(id,example) where flashcard.id=editorial.id;

update public.questions as question set explanation=editorial.explanation
from (values
('c27-grammar',0,'Zdanie z „jeżeli” wyznacza warunek rozpoczęcia negocjacji: najpierw strony muszą tak samo rozumieć ryzyko, dopiero potem ustalają jego dopuszczalny poziom.'),
('c27-grammar',1,'„Innymi słowy” sygnalizuje kontrolowaną parafrazę, natomiast „zaś” zestawia odmienne potrzeby bez sugerowania, że jedna z nich jest mniej ważna.'),
('c27-grammar',2,'Trafna parafraza zachowuje ograniczenie zakresu: wynik z jednej poradni nie staje się automatycznie dowodem dotyczącym wszystkich placówek w regionie.'),
('c27-grammar',3,'Mediację sprawdza się przez zwrotne potwierdzenie stron: każda z nich ocenia, czy parafraza zachowała jej intencję, warunki oraz stopień pewności.'),
('c27-grammar',4,'Napięcie zmniejsza nazwanie wspólnego celu przy jednoczesnym zachowaniu realnej rozbieżności; pozorna zgoda tylko ukryłaby konflikt kryteriów.'),
('c27-grammar',5,'Propozycja dwóch opisanych wariantów pozostawia mandat decyzyjny uczestnikom, ponieważ mediatorka porządkuje skutki, ale nie wybiera za nich.'),
('c27-quiz',0,'Mediatorka prowadzi proces rozumienia stanowisk i poszukiwania warunków porozumienia, nie pełni jednak funkcji arbitra wydającego wiążące rozstrzygnięcie.'),
('c27-quiz',1,'Wspólny mianownik to minimalny cel lub kryterium podzielane mimo różnic; w tekście jest nim wykrywanie przypadków bez przeciążania pacjentów.'),
('c27-quiz',2,'Rozbieżność stanowisk nazywa konkretny punkt niezgody między stronami, dzięki czemu można negocjować kryterium zamiast powtarzać ogólne deklaracje.'),
('c27-quiz',3,'Interes strony oznacza potrzebę albo wartość stojącą za jej postulatem; odróżnienie interesu od żądania otwiera drogę do innych rozwiązań.'),
('c27-quiz',4,'Pole porozumienia obejmuje te cele i warunki, które strony mogą zaakceptować wspólnie, nawet jeśli nadal różnią się co do sposobu realizacji.'),
('c27-quiz',5,'Termin specjalistyczny ma precyzyjne znaczenie w danej dziedzinie; mediator powinien je objaśnić bez usuwania ograniczeń istotnych dla decyzji.'),
('c27-quiz',6,'Asymetria wiedzy występuje, gdy uczestnicy dysponują różnymi rodzajami informacji; mediacja ma je udostępnić, a nie udawać pełną symetrię kompetencji.'),
('c27-quiz',7,'Warunek brzegowy określa zakres, w którym wniosek pozostaje ważny, dlatego jego pominięcie mogłoby niesłusznie rozszerzyć rezultat pilotażu.'),
('c27-quiz',8,'Uzgodnić definicję znaczy sprawdzić, czy strony przypisują kluczowemu pojęciu ten sam zakres i kryteria, zanim zaczną oceniać rozwiązania.'),
('c27-quiz',9,'Przełożyć na język praktyki to pokazać obserwowalne skutki abstrakcyjnego pojęcia, na przykład liczbę przeoczonych przypadków lub fałszywych alarmów.'),
('c27-reading-check',0,'W pierwszym akapicie każda grupa łączyła „bezpieczeństwo” z innym kryterium: czułością, alarmami albo progiem, więc samo słowo nie usuwało różnic.'),
('c27-reading-check',1,'Drugi akapit objaśnia czułość przez praktyczne pytanie o liczbę chorych, których system może przeoczyć, oraz koszt obniżenia progu.'),
('c27-reading-check',2,'Informatycy zastrzegli w trzecim akapicie, że wynik jednej poradni nie uzasadnia automatycznego wdrożenia rozwiązania w całym regionie.'),
('c27-reading-check',3,'Czwarty akapit wskazuje wspólny mianownik: wykryć możliwie wiele przypadków, nie przeciążając przy tym pacjentów nadmiarem alarmów.'),
('c27-reading-check',4,'Przy obu wariantach zapisano korzyści, ryzyka i dane potrzebne do oceny, aby wybór nie opierał się na samych deklaracjach stron.'),
('c27-reading-check',5,'Mediacja nie przyniosła jeszcze decyzji, lecz stworzyła wspólny język, kryteria, warianty oraz termin dostarczenia brakujących danych.')
) editorial(lesson_id,position,explanation)
where question.lesson_id=editorial.lesson_id and question.position=editorial.position;
