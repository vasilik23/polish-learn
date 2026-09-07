-- Keep the C2 rhetorical-strategy editorial pass rerunnable and content-only.
update public.flashcards as flashcard
set example = editorial.example
from (values
  ('c22-1', 'Figura retoryczna wzmacniała wezwanie do działania, lecz mówczyni wyjaśniła też przesłanki swojej propozycji.'),
  ('c22-2', 'Redaktor przesunął punkt ciężkości z alarmującego hasła na porównanie kosztów trzech możliwych rozwiązań.'),
  ('c22-3', 'Gradacja prowadziła od drobnych niedogodności przez straty finansowe aż do ryzyka zamknięcia zakładu.'),
  ('c22-4', 'Antyteza „nie mniej kontroli, lecz lepsza kontrola” precyzyjnie oddzieliła cel reformy od użytych środków.'),
  ('c22-5', 'Paralelizm składniowy uporządkował trzy postulaty: sprawdźmy dane, porównajmy warianty, oceńmy skutki.'),
  ('c22-6', 'Pytanie retoryczne otworzyło debatę, ale nie zostało przedstawione jako dowód słuszności projektu.'),
  ('c22-7', 'Puenta połączyła wcześniejsze argumenty z konkretnym wnioskiem o półrocznym, niezależnie ocenianym pilotażu.'),
  ('c22-8', 'Aby wyprzedzić kontrargument, autorka sama omówiła koszt reformy i wskazała granice proponowanej rekompensaty.'),
  ('c22-9', 'Mówca zaczął stopniować napięcie od jednostkowego przypadku do konsekwencji odczuwanych przez całą dzielnicę.'),
  ('c22-10', 'Debata miała przesunąć akcent z politycznych deklaracji na mierzalne rezultaty wcześniejszego programu.'),
  ('c22-11', 'Ekspert postanowił zawęzić tezę do transportu publicznego, ponieważ dane nie obejmowały ruchu prywatnego.'),
  ('c22-12', 'Reportaż potrafił odwrócić perspektywę, pokazując reformę oczami osób dotąd nieobecnych w konsultacjach.'),
  ('c22-13', 'Pozorny dylemat kazał wybierać między natychmiastową zgodą a katastrofą, choć istniały warianty pośrednie.'),
  ('c22-14', 'Komentator zastosował chwyt erystyczny: zaatakował kompetencje rozmówcy, aby odwrócić uwagę od niewygodnych danych.'),
  ('c22-15', 'Uczciwość argumentacyjna wymagała ujawnienia ograniczeń badania, mimo że osłabiały efektowność końcowej tezy.')
) as editorial(id, example)
where flashcard.id = editorial.id;

update public.questions as question
set explanation = editorial.explanation
from (values
  ('c22-grammar', 0, 'Konstrukcja „nie..., lecz...” tworzy antytezę: zachowuje wspólny cel, a kontrastuje wyłącznie sposoby jego osiągnięcia.'),
  ('c22-grammar', 1, 'Spójnik „nawet jeśli” wprowadza ustępstwo; uznanie trafności zarzutu nie oznacza jeszcze obalenia głównego wniosku.'),
  ('c22-grammar', 2, 'Powtórzenie „potrzebujemy” buduje paralelizm składniowy, natomiast trzy konkretne dopełnienia chronią wypowiedź przed pustym patosem.'),
  ('c22-grammar', 3, 'Uczciwe wyprzedzenie kontrargumentu najpierw uznaje realny koszt, a następnie proponuje porównywalny koszt zaniechania jako kryterium oceny.'),
  ('c22-grammar', 4, 'Dobra puenta wynika z przytoczonego rezultatu pilotażu i prowadzi do sprawdzalnego następnego kroku, czyli niezależnej ewaluacji.'),
  ('c22-grammar', 5, 'Pierwsze zdanie tworzy pozorny dylemat, ponieważ pomija zmianę projektu, pilotaż i inne możliwości między dwiema skrajnościami.'),
  ('c22-quiz', 0, 'Figura retoryczna to celowa organizacja języka, która kieruje uwagą lub wzmacnia efekt wypowiedzi, ale sama nie zastępuje dowodu.'),
  ('c22-quiz', 1, 'Punkt ciężkości wskazuje element przedstawiony jako najważniejszy; jego przesunięcie zmienia hierarchię argumentów bez koniecznej zmiany faktów.'),
  ('c22-quiz', 2, 'Gradacja szereguje argumenty albo obrazy według rosnącej lub malejącej siły, dzięki czemu świadomie steruje napięciem wypowiedzi.'),
  ('c22-quiz', 3, 'Antyteza zestawia kontrastujące idee w równoległej konstrukcji, aby precyzyjnie uwidocznić różnicę między stanowiskami lub pojęciami.'),
  ('c22-quiz', 4, 'Paralelizm składniowy powtarza podobny schemat zdań lub członów, porządkując tok argumentu i nadając mu wyraźny rytm.'),
  ('c22-quiz', 5, 'Pytanie retoryczne nie oczekuje bezpośredniej odpowiedzi; podkreśla sugerowany wniosek, dlatego nie wolno traktować go jak dowodu.'),
  ('c22-quiz', 6, 'Puenta zamyka wypowiedź znaczącym wnioskiem, który powinien wynikać z wcześniejszych przesłanek, a nie jedynie efektownie brzmieć.'),
  ('c22-quiz', 7, 'Wyprzedzić kontrargument znaczy samodzielnie przedstawić silne zastrzeżenie i uczciwie na nie odpowiedzieć, zanim zrobi to odbiorca.'),
  ('c22-quiz', 8, 'Stopniować napięcie to układać kolejne elementy tak, aby ich emocjonalna lub argumentacyjna siła rosła w kontrolowany sposób.'),
  ('c22-quiz', 9, 'Przesunąć akcent oznacza zmienić to, czemu wypowiedź nadaje największą wagę, na przykład zastąpić moralną presję kryteriami oceny.'),
  ('c22-reading-check', 0, 'Pierwszy akapit pokazuje pozorny dylemat: przeciwników natychmiastowego działania przedstawiono jako rzekomych obrońców chaosu.'),
  ('c22-reading-check', 1, 'W drugim akapicie redaktorka zastępuje binarny wybór porównaniem trzech wariantów oraz ich kosztów i skutków społecznych.'),
  ('c22-reading-check', 2, 'Trzeci akapit powtarza konstrukcję „sprawdźmy”, by zachować rytm i zarazem wyodrębnić trzy przejrzyste kryteria kontroli.'),
  ('c22-reading-check', 3, 'Trzeci akapit uznaje koszt reorganizacji dostaw i wskazuje fundusz przejściowy jako częściową, a nie całkowitą odpowiedź.'),
  ('c22-reading-check', 4, 'Czwarty akapit zastępuje efektowne hasło propozycją półrocznego pilotażu, którego wynik mają rozstrzygnąć publiczne kryteria.'),
  ('c22-reading-check', 5, 'Ostatni akapit definiuje uczciwość argumentacyjną jako podporządkowanie kompozycji, gradacji i antytezy jakości przedstawionych racji.')
) as editorial(lesson_id, position, explanation)
where question.lesson_id = editorial.lesson_id
  and question.position = editorial.position;
