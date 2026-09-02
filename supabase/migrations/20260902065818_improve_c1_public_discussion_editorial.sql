-- Keep the C1 public-discussion editorial pass rerunnable and content-only.
update public.flashcards as flashcard
set example = editorial.example
from (values
  ('c18-1', 'Mimo różnic mieszkańcy znaleźli obszar zgody: wszyscy chcieli bezpieczniejszego przejścia przez plac.'),
  ('c18-2', 'Moderatorka nazwała oś sporu, oddzielając dyskusję o liczbie miejsc parkingowych od rozmowy o bezpieczeństwie.'),
  ('c18-3', 'Każdy interesariusz otrzymał czas na przedstawienie potrzeb, od właścicieli sklepów po rodziców małych dzieci.'),
  ('c18-4', 'Aby legitymizować decyzję, urząd opublikował kryteria wyboru i odpowiedzi na uwagi zgłoszone podczas konsultacji.'),
  ('c18-5', 'Projekt miał zrównoważyć interesy kierowców, pieszych i lokalnych przedsiębiorców bez uprzywilejowania jednej grupy.'),
  ('c18-6', 'Prowadząca potrafiła oddać sprawiedliwość argumentowi przeciwników, zanim wskazała jego ograniczenia i zaproponowała korektę.'),
  ('c18-7', 'Warto nazwać napięcie między szybkim wdrożeniem zmian a potrzebą rzetelnego sprawdzenia ich skutków.'),
  ('c18-8', 'Na początku spotkania ustalono ramy debaty: zakres tematu, kolejność wypowiedzi oraz zasady reagowania na zarzuty.'),
  ('c18-9', 'Personalny atak mógł eskalować konflikt, dlatego moderatorka poprosiła rozmówcę o odniesienie się do konkretnego argumentu.'),
  ('c18-10', 'Stronom udało się wypracować kompromis, który zachował drzewa i dopuścił czasowe miejsca dostawcze.'),
  ('c18-11', 'Za warunek konieczny pilotażu uznano niezależny pomiar bezpieczeństwa przed zmianą organizacji ruchu i po niej.'),
  ('c18-12', 'Stanowisko mniejszości dołączono do protokołu, choć większość uczestników poparła inny wariant przebudowy.'),
  ('c18-13', 'Podsumowanie robocze wskazało ustalone fakty, nierozstrzygnięte pytania i dane potrzebne przed kolejnym spotkaniem.'),
  ('c18-14', 'Nowa procedura konsultacji gwarantuje mieszkańcom dostęp do projektu, termin na uwagi i odpowiedź urzędu.'),
  ('c18-15', 'Rada postanowiła odroczyć decyzję do czasu publikacji analizy wpływu inwestycji na lokalny handel.')
) as editorial(id, example)
where flashcard.id = editorial.id;

update public.questions as question
set explanation = editorial.explanation
from (values
  ('c18-grammar', 0, 'Obszar zgody obejmuje wartości lub cele akceptowane przez strony mimo sporu; może stać się punktem wyjścia do szukania rozwiązania.'),
  ('c18-grammar', 1, 'Oś sporu nazywa zasadniczą kwestię dzielącą rozmówców, dzięki czemu poboczne różnice nie przesłaniają głównego problemu debaty.'),
  ('c18-grammar', 2, 'Interesariuszem jest osoba albo grupa, na którą decyzja wpływa lub która może wpłynąć na jej przygotowanie i wykonanie.'),
  ('c18-grammar', 3, 'Legitymizować decyzję to budować jej społeczną akceptację przez przejrzystą procedurę, uzasadnienie i rzeczywisty udział zainteresowanych stron.'),
  ('c18-grammar', 4, 'Zrównoważyć interesy oznacza uwzględnić konkurujące potrzeby według jawnych kryteriów, a nie po prostu podzielić korzyści po równo.'),
  ('c18-grammar', 5, 'Oddać sprawiedliwość argumentowi to rzetelnie przedstawić jego najmocniejszą wersję przed krytyką, bez zniekształcania stanowiska rozmówcy.'),
  ('c18-quiz', 0, 'Obszar zgody nie usuwa różnic, lecz wskazuje wspólny cel, wokół którego strony mogą budować warunki dalszego porozumienia.'),
  ('c18-quiz', 1, 'Oś sporu porządkuje debatę przez wskazanie centralnej rozbieżności, na przykład konfliktu między dostępnością parkingu a przestrzenią dla pieszych.'),
  ('c18-quiz', 2, 'Interesariusz ma uzasadniony związek z decyzją jako jej uczestnik, odbiorca skutków lub podmiot dysponujący ważną wiedzą.'),
  ('c18-quiz', 3, 'Decyzję legitymizuje nie samo głosowanie, lecz również przejrzystość kryteriów, możliwość udziału i odpowiedź na zgłoszone argumenty.'),
  ('c18-quiz', 4, 'Równoważenie interesów wymaga nazwania potrzeb wszystkich stron i oceny skutków wariantów, zwłaszcza dla grup słabiej reprezentowanych.'),
  ('c18-quiz', 5, 'Oddanie sprawiedliwości argumentowi sygnalizuje intelektualną uczciwość: prowadzący uznaje jego trafną część, nawet jeśli odrzuca wniosek.'),
  ('c18-quiz', 6, 'Nazwać napięcie znaczy ujawnić konflikt między wartościami lub celami, aby rozmówcy mogli negocjować go wprost zamiast mówić obok siebie.'),
  ('c18-quiz', 7, 'Ramy debaty określają temat, role, czas i zasady wymiany argumentów; chronią rozmowę przed chaosem oraz zmianą przedmiotu sporu.'),
  ('c18-quiz', 8, 'Eskalować konflikt to zwiększać jego intensywność, na przykład przez personalizację zarzutów, groźby albo podważanie prawa strony do udziału.'),
  ('c18-quiz', 9, 'Wypracować kompromis oznacza wspólnie stworzyć rozwiązanie wymagające ustępstw, ale chroniące najważniejsze potrzeby każdej ze stron.'),
  ('c18-reading-check', 0, 'Bezpieczeństwo pieszych było obszarem zgody, ponieważ uznawały je obie strony mimo sporu dotyczącego liczby miejsc parkingowych.'),
  ('c18-reading-check', 1, 'Pierwszy akapit przedstawia uczestników oraz ramy rozmowy, dzięki czemu wiadomo, czyje interesy i według jakich zasad będą omawiane.'),
  ('c18-reading-check', 2, 'Drugi akapit oddziela oś sporu o parking od wspólnego celu, czyli bezpieczeństwa pieszych, który umożliwia dalsze negocjacje.'),
  ('c18-reading-check', 3, 'Trzeci akapit pokazuje interwencję moderatorki: uznaje argument mniejszości, lecz zatrzymuje wypowiedź nasilającą konflikt.'),
  ('c18-reading-check', 4, 'Czwarty akapit porządkuje stanowiska przez rozdzielenie faktów, wartości i brakujących danych, zamiast przedwcześnie ogłaszać zwycięzcę.'),
  ('c18-reading-check', 5, 'Ostatni akapit nie kończy procesu pozornym kompromisem: odracza decyzję, ale ustala warunki pilotażu oraz sposób jego oceny.')
) as editorial(lesson_id, position, explanation)
where question.lesson_id = editorial.lesson_id
  and question.position = editorial.position;
