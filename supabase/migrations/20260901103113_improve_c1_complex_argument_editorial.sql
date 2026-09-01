update public.flashcards as f
set example = v.example
from (values
  ('c12-1', 'Autor dodał zastrzeżenie, że wyniki pilotażu nie obejmują małych miejscowości.'),
  ('c12-2', 'Pierwsza przesłanka opiera się na danych, druga zaś pozostaje tylko założeniem.'),
  ('c12-3', 'Tok rozumowania jest spójny, dopóki autor nie utożsamia korelacji z przyczyną.'),
  ('c12-4', 'Najmocniejszy kontrargument dotyczył kosztów, których raport w ogóle nie oszacował.'),
  ('c12-5', 'Aby obalić zarzut, badaczka wskazała reprezentatywną próbę i pełne wyniki.'),
  ('c12-6', 'Warto przyznać rację oponentowi tam, gdzie jego uwaga ujawnia realne ryzyko.'),
  ('c12-7', 'Z dużym prawdopodobieństwem zmiana ograniczy ruch, choć skala efektu pozostaje niepewna.'),
  ('c12-8', 'Jedno udane wdrożenie nie przesądza, że rozwiązanie sprawdzi się wszędzie.'),
  ('c12-9', 'Poprzemy projekt o tyle, o ile przewidzi on niezależną ocenę skutków.'),
  ('c12-10', 'Dane są niepełne; tym niemniej pozwalają odrzucić najbardziej skrajny scenariusz.'),
  ('c12-11', 'Z porównania raportów może wynikać pośrednio, że autorzy przyjęli różne definicje sukcesu.'),
  ('c12-12', 'Uprawniony wniosek uwzględnia zarówno wyniki badania, jak i granice zastosowanej metody.'),
  ('c12-13', 'Powoływanie się na autorytet zamiast na dowody uznano za nadużycie argumentacyjne.'),
  ('c12-14', 'Komisja musi ważyć argumenty, zamiast liczyć wyłącznie głosy zwolenników i przeciwników.'),
  ('c12-15', 'Nowe dane skłoniły ekspertkę, by niuansować stanowisko bez wycofywania głównej tezy.')
) as v(id, example)
where f.id = v.id;

update public.questions as q
set explanation = v.explanation
from (values
  ('c12-grammar', 0, 'Zastrzeżenie ogranicza zakres tezy albo wskazuje warunek jej obowiązywania; dzięki niemu argument nie brzmi bezwzględnie.'),
  ('c12-grammar', 1, 'Przesłanka to zdanie, na którym opiera się wniosek; ocena argumentu wymaga sprawdzenia jej prawdziwości i związku z tezą.'),
  ('c12-grammar', 2, 'Tok rozumowania opisuje drogę od przesłanek do wniosku, dlatego można go oceniać pod kątem spójności i brakujących kroków.'),
  ('c12-grammar', 3, 'Kontrargument odpowiada na przedstawioną tezę, wskazując jej słabość, wyjątek albo konkurencyjne wyjaśnienie.'),
  ('c12-grammar', 4, 'Obalić zarzut znaczy wykazać, że dane zastrzeżenie jest nietrafne, na przykład przez podanie dowodu lub korektę założenia.'),
  ('c12-grammar', 5, 'Przyznać rację nie oznacza porzucić własnej tezy: można zaakceptować trafny punkt oponenta i następnie doprecyzować stanowisko.'),
  ('c12-quiz', 0, 'Zastrzeżenie wprowadza wyjątek, ograniczenie albo warunek, więc sygnalizuje, w jakim zakresie autor podtrzymuje swoją tezę.'),
  ('c12-quiz', 1, 'Przesłanka dostarcza podstawy dla wniosku; bez wiarygodnej przesłanki nawet logicznie brzmiąca konkluzja pozostaje słaba.'),
  ('c12-quiz', 2, 'Tok rozumowania łączy kolejne etapy argumentu i pozwala zobaczyć, czy wniosek rzeczywiście wynika z przyjętych przesłanek.'),
  ('c12-quiz', 3, 'Kontrargument nie jest samym sprzeciwem: powinien odnosić się do uzasadnienia tezy i pokazywać konkretną jego słabość.'),
  ('c12-quiz', 4, 'Obalenie zarzutu wymaga odpowiedzi na jego treść, a nie zmiany tematu ani podważania osoby, która go zgłosiła.'),
  ('c12-quiz', 5, 'Przyznanie racji wzmacnia uczciwą argumentację, gdy jasno wskazujemy trafny element cudzej wypowiedzi i jego wpływ na własny pogląd.'),
  ('c12-quiz', 6, 'Wyrażenie z dużym prawdopodobieństwem sygnalizuje mocną, lecz nie absolutną pewność i zostawia miejsce na wynik odmienny od przewidywanego.'),
  ('c12-quiz', 7, 'Konstrukcja nie przesądza oddziela dostępną przesłankę od ostatecznego wniosku: wskazany fakt sam jeszcze nie rozstrzyga sprawy.'),
  ('c12-quiz', 8, 'Konstrukcja o tyle, o ile uzależnia akceptację pierwszej części zdania od spełnienia warunku podanego w drugiej części.'),
  ('c12-quiz', 9, 'Tym niemniej wprowadza treść przeciwną do oczekiwania wynikającego z wcześniejszego zdania i pomaga zachować jego wagę.'),
  ('c12-reading-check', 0, 'Wniosek popiera pilotaż warunkowo: miasto ma jednocześnie zbadać dostępność oraz wpływ zmiany na lokalny handel.'),
  ('c12-reading-check', 1, 'Pierwszy akapit przedstawia przedmiot debaty i sygnalizuje sprzeczność danych; szczegółowe racje stron pojawiają się dopiero później.'),
  ('c12-reading-check', 2, 'Drugi akapit równoważy korzyść środowiskową z możliwym problemem dostaw, więc pokazuje stanowisko zwolenników z wyraźnym zastrzeżeniem.'),
  ('c12-reading-check', 3, 'Trzeci akapit przytacza kosztowy kontrargument przeciwników, lecz od razu ogranicza siłę pojedynczego przykładu jako dowodu.'),
  ('c12-reading-check', 4, 'Czwarty akapit opisuje pracę eksperta: oddziela on potwierdzone przesłanki od założeń, których raport nie uzasadnia.'),
  ('c12-reading-check', 5, 'Ostatni akapit formułuje warunkowe poparcie pilotażu i wskazuje dwa obszary, które miasto powinno równolegle monitorować.')
) as v(lesson_id, position, explanation)
where q.lesson_id = v.lesson_id and q.position = v.position;
