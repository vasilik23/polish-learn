from django.db import migrations


EXPLANATIONS = {
    "b2discussion-grammar": {
        0: "Formuła „jeśli dobrze rozumiem” neutralnie sprawdza trafność parafrazy i pozwala rozmówcy ją skorygować.",
        1: "Konstrukcja „z jednej strony…, z drugiej strony…” porządkuje i równoważy dwa odmienne aspekty argumentu.",
        2: "Czasownik „wrócić” łączy się z przyimkiem „do” i dopełniaczem, dlatego mówimy „do kwestii”.",
        3: "Imiesłów „podsumowując” wprowadza zwięzły wniosek, a spójnik „lecz” zachowuje wskazane rozbieżności.",
        4: "Po czasowniku „proponować” naturalnie występuje bezokolicznik, a formuła wstępna łagodzi sprawdzanie intencji.",
        5: "Zwrot „zgadzać się co do” wymaga dopełniacza, natomiast „ale” wyraźnie zachowuje kontrast.",
    },
    "b2discussion-quiz": {
        0: "Zwrot „oddać głos” oznacza przekazać kolej wypowiedzi konkretnej osobie uczestniczącej w dyskusji.",
        1: "Formuła „jeśli dobrze rozumiem” sprawdza cudzą intencję bez narzucania rozmówcy własnej interpretacji.",
        2: "„Punkt sporny” nazywa kwestię, w której uczestnicy nadal prezentują odmienne stanowiska.",
        3: "Zwrot „wróćmy do pytania” uprzejmie kieruje rozmowę na wcześniejszy temat bez oceniania uczestnika.",
        4: "Moderator parafrazuje wypowiedź, aby sprawdzić jej sens i uczynić stanowisko zrozumiałym dla wszystkich.",
        5: "Para „z jednej strony…, z drugiej strony…” służy uporządkowanemu zestawieniu dwóch aspektów sprawy.",
        6: "Rzetelne podsumowanie osobno wskazuje osiągnięte porozumienie oraz kwestie, które nadal pozostają sporne.",
        7: "Zwrot „dojść do głosu” oznacza otrzymać realną możliwość przedstawienia swojej wypowiedzi podczas rozmowy.",
        8: "Moderator przerywa wypowiedź ze względów proceduralnych, gdy narusza ona temat albo ustalony czas.",
        9: "„Osiągnąć porozumienie” znaczy wspólnie wypracować rozwiązanie możliwe do zaakceptowania przez uczestników.",
    },
    "b2discussion-reading-check": {
        0: "Celem spotkania było rozpoznanie potrzeb mieszkańców przed podjęciem decyzji, a nie natychmiastowe głosowanie.",
        1: "Moderatorka ujęła stanowiska jako potrzebę dostępności oraz pytanie o warunki bezpiecznej realizacji.",
        2: "Moderatorka przerwała wątek, ponieważ odszedł od ustalonego tematu godzin pracy biblioteki.",
        3: "Seniorka połączyła dostępność biblioteki z bezpiecznym powrotem, rozszerzając perspektywę całej dyskusji.",
        4: "Uczestnicy uzgodnili trzymiesięczny pilotaż obejmujący dwa wieczory w każdym tygodniu.",
        5: "W podsumowaniu jako nierozstrzygnięte wskazano źródło finansowania oraz dokładne godziny otwarcia.",
    },
    "b2intercultural-grammar": {
        0: "Formuła „mam wrażenie, że” przedstawia obserwację jako osobistą i ogranicza siłę uogólnienia.",
        1: "Stały zwrot „mieć na myśli” oznacza zamierzony sens wypowiedzi i wymaga formy „masz”.",
        2: "Ta formuła uznaje niezamierzony skutek słów, a następnie precyzyjnie wyjaśnia pierwotną intencję.",
        3: "Spójnik „zanim” wprowadza czynność wcześniejszą, więc najpierw pytamy, a dopiero potem interpretujemy.",
        4: "Konstrukcja „lepiej…, niż…” porównuje rozwiązania i wskazuje doprecyzowanie jako rozsądniejszy wybór.",
        5: "Pytanie „czy dobrze rozumiem, że…” neutralnie sprawdza interpretację przed sformułowaniem oceny.",
    },
    "b2intercultural-quiz": {
        0: "„Norma komunikacyjna” to przyjęty w danym kontekście sposób prowadzenia rozmowy i wyrażania intencji.",
        1: "„Nieporozumienie” oznacza sytuację, w której rozmówcy odmiennie rozumieją przekazaną wiadomość lub zachowanie.",
        2: "„Intencja” nazywa zamiar mówiącego, który może różnić się od rzeczywistego efektu wypowiedzi.",
        3: "„Interpretować” znaczy nadawać znaczenie wypowiedzi, zachowaniu albo sytuacji na podstawie dostępnych wskazówek.",
        4: "„Uogólnienie” przypisuje cechę szerszej grupie, choć pojedyncza obserwacja nie musi jej potwierdzać.",
        5: "„Stereotyp” jest uproszczonym przekonaniem o grupie, które pomija różnice między konkretnymi osobami.",
        6: "„Bezpośredni” opisuje styl, w którym zamiar lub oczekiwanie zostaje wyrażone jasno i wprost.",
        7: "„Pośredni” określa styl przekazywania sensu przez sugestię, kontekst albo łagodniejszą formułę.",
        8: "„Doprecyzować” znaczy uzupełnić wypowiedź tak, aby jej znaczenie stało się dokładniejsze i jednoznaczne.",
        9: "Zwrot „odczytać ton” oznacza rozpoznać emocjonalny sposób, w jaki została sformułowana wiadomość.",
    },
    "b2intercultural-reading-check": {
        0: "Lenę uraziła interpretacja krótkiej wiadomości jako chłodnej oceny jej przygotowanej pracy.",
        1: "Marek świadomie mówił o własnym doświadczeniu, unikając nieuprawnionego uogólnienia na całą grupę.",
        2: "Szkolenie pokazało, że zachowanie zależy również od wieku, roli, branży oraz konkretnej sytuacji.",
        3: "Zespół postanowił dodawać do pilnych krótkich wiadomości kontekst, termin oraz krótkie podziękowanie.",
        4: "Zasada „najpierw pytamy, potem interpretujemy” nakazuje sprawdzić intencję przed ocenieniem zachowania.",
        5: "Zespół dostosował wspólne normy komunikacji, lecz nie próbował usuwać indywidualnych różnic uczestników.",
    },
}


def improve_explanations(apps, schema_editor):
    Question = apps.get_model("learning", "Question")
    for lesson_id, explanations in EXPLANATIONS.items():
        for position, explanation in explanations.items():
            Question.objects.filter(lesson_id=lesson_id, position=position).update(
                explanation=explanation
            )


class Migration(migrations.Migration):
    dependencies = [("learning", "0108_improve_b2_psychology_literature_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
