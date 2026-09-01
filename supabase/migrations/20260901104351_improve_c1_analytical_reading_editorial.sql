update public.flashcards as f
set example = v.example
from (values
  ('c13-1', 'Ukrytym założeniem felietonu jest przekonanie, że każdy mieszkaniec porusza się po mieście samochodem.'),
  ('c13-2', 'Nagłówek narzuca ramę interpretacyjną, w której protest przedstawiono jako konflikt pokoleń.'),
  ('c13-3', 'Dobór przykładów eksponuje koszt reformy, ale nie pokazuje korzyści odczuwanych przez mieszkańców.'),
  ('c13-4', 'Pominięcie danych z mniejszych miejscowości wyraźnie osłabia wniosek sformułowany w raporcie.'),
  ('c13-5', 'Mimo neutralnego słownictwa wypowiedź ma krytyczny wydźwięk dzięki zestawieniu dwóch sprzecznych liczb.'),
  ('c13-6', 'Ironiczne pytanie autora pozornie zaprasza do refleksji, a faktycznie ośmiesza stanowisko przeciwników.'),
  ('c13-7', 'Określenie „lekkomyślna decyzja” jest wartościujące, ponieważ podsuwa ocenę przed przedstawieniem faktów.'),
  ('c13-8', 'Pozornie neutralny opis kolejki pomija jej przyczynę i przez to obciąża odpowiedzialnością klientów.'),
  ('c13-9', 'Kolejność argumentów sugeruje, że autor uznaje względy ekonomiczne za ważniejsze od społecznych.'),
  ('c13-10', 'Brak informacji o liczebności próby pozwala podważać wiarygodność przytoczonego sondażu.'),
  ('c13-11', 'Strategia autora polega na przywołaniu głosu eksperta dopiero po serii emocjonalnych przykładów.'),
  ('c13-12', 'Wiarygodność komentarza rośnie, gdy autor ujawnia źródła danych i ograniczenia własnej analizy.'),
  ('c13-13', 'Punkt widzenia narratora ujawnia się nie w deklaracjach, lecz w tym, komu oddaje on głos.'),
  ('c13-14', 'Aby odczytać intencję felietonisty, trzeba zestawić dosłowną treść pytań z ich ironicznym tonem.'),
  ('c13-15', 'Wniosek implicytny wynika z układu argumentów, choć autor nigdzie nie formułuje go wprost.')
) as v(id, example)
where f.id = v.id;

update public.questions as q
set explanation = v.explanation
from (values
  ('c13-grammar', 0, 'Założenie ukryte to niewypowiedziana przesłanka, którą autor traktuje jak oczywistą; jej ujawnienie pozwala sprawdzić podstawę wniosku.'),
  ('c13-grammar', 1, 'Rama interpretacyjna porządkuje fakty według wybranej perspektywy, przez co wpływa na to, jak odbiorca rozumie całe zdarzenie.'),
  ('c13-grammar', 2, 'Dobór przykładów oznacza decyzję, które przypadki pokazać; jednostronny wybór może wzmacniać tezę bez pełnego obrazu sytuacji.'),
  ('c13-grammar', 3, 'Pominięcie jest znaczącym brakiem informacji: w analizie pytamy, czy nieobecny fakt mógłby zmienić ocenę argumentu.'),
  ('c13-grammar', 4, 'Wydźwięk to ogólne wrażenie i ocena sugerowane przez tekst; tworzą go między innymi słownictwo, kontrast oraz kolejność informacji.'),
  ('c13-grammar', 5, 'Ironiczny komunikat przekazuje ocenę pośrednio: jego zamierzony sens różni się od znaczenia dosłownego i zależy od kontekstu.'),
  ('c13-quiz', 0, 'Ukryta przesłanka nie pada wprost, ale jest konieczna, aby rozumowanie autora wydawało się spójne; warto więc ocenić jej zasadność.'),
  ('c13-quiz', 1, 'Rama interpretacyjna nadaje faktom wspólny sens, na przykład przedstawiając zmianę jako postęp, kryzys albo konflikt interesów.'),
  ('c13-quiz', 2, 'Dobór przykładów może wspierać określoną perspektywę: analizujemy zarówno przywołane przypadki, jak i te konsekwentnie nieobecne.'),
  ('c13-quiz', 3, 'Pominięcie nie jest jedynie skrótem, gdy usuwa informację istotną dla wniosku; wtedy staje się elementem strategii argumentacyjnej.'),
  ('c13-quiz', 4, 'Wydźwięk opisuje ton i ocenę płynącą z całości wypowiedzi, nawet jeśli autor unika bezpośrednich sądów wartościujących.'),
  ('c13-quiz', 5, 'Ironia wymaga odczytania rozbieżności między sensem dosłownym a intencją, którą sygnalizują kontekst, przesada lub ton wypowiedzi.'),
  ('c13-quiz', 6, 'Słowo wartościujący wskazuje, że element języka nie tylko opisuje fakt, lecz także podpowiada odbiorcy jego pozytywną lub negatywną ocenę.'),
  ('c13-quiz', 7, 'Pozornie neutralna wypowiedź zachowuje bezstronną formę, ale doborem informacji, porządkiem lub przemilczeniem wspiera określony punkt widzenia.'),
  ('c13-quiz', 8, 'Sugerować to komunikować sens pośrednio, bez jednoznacznego stwierdzenia; odbiorca rekonstruuje go z kontekstu i organizacji tekstu.'),
  ('c13-quiz', 9, 'Podważać znaczy przedstawiać powody, dla których teza, źródło albo dowód mogą być niewiarygodne, niepełne lub błędnie zinterpretowane.'),
  ('c13-reading-check', 0, 'Pierwszy komentarz wymienia koszty, lecz przemilcza korzyści oraz głosy mieszkańców; właśnie ta asymetria kształtuje jego pozorną neutralność.'),
  ('c13-reading-check', 1, 'Pierwszy akapit ustanawia sytuację porównania: studentka analizuje dwa komentarze dotyczące tej samej miejskiej zmiany.'),
  ('c13-reading-check', 2, 'Drugi akapit pokazuje selektywność pierwszego komentarza: eksponuje on koszty, a usuwa korzyści i perspektywę mieszkańców.'),
  ('c13-reading-check', 3, 'Trzeci akapit łączy ironiczne pytania z wartościującym wydźwiękiem, więc opisuje pośredni sposób ujawniania oceny autora.'),
  ('c13-reading-check', 4, 'Czwarty akapit podaje metodę analizy: zamiast przypisywać autorowi poglądy, studentka bada przykłady, źródła i ramę tekstu.'),
  ('c13-reading-check', 5, 'Ostatni akapit formułuje zasadę analitycznego czytania: trzeba oddzielić treść jawną od wniosku sugerowanego konstrukcją wypowiedzi.')
) as v(lesson_id, position, explanation)
where q.lesson_id = v.lesson_id and q.position = v.position;
