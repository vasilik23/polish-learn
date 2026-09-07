from django.db import migrations


EXAMPLES = {
    "c28-1": "Synteza źródeł połączyła wynik eksperymentu, obserwację pracowników i mechanizmy opisane w wywiadach.",
    "c28-2": "Triangulacja danych ujawniła, że podobny efekt pojawia się w pomiarach ilościowych i relacjach uczestników.",
    "c28-3": "Jakość dowodu oceniono wyżej w eksperymencie, choć jego krótki czas ograniczał trwałość wniosku.",
    "c28-4": "Duża próba badawcza zwiększyła precyzję oszacowania, ale nie usunęła problemu samooboru uczestników.",
    "c28-5": "Zmienna zakłócająca, taka jak sen, mogła wpływać zarówno na wybór spaceru, jak i koncentrację.",
    "c28-6": "Najważniejsze ograniczenie metodologiczne polegało na braku losowego przydziału w badaniu obserwacyjnym.",
    "c28-7": "Stopień pewności określono jako umiarkowany, bo wyniki były zbieżne, lecz metody miały istotne słabości.",
    "c28-8": "Zbieżność wyników wzmacnia hipotezę tylko wtedy, gdy badania nie powtarzają tych samych błędów.",
    "c28-9": "Badacze musieli ważyć dowody według kontroli zmiennych, czasu obserwacji i trafności zastosowanych miar.",
    "c28-10": "Aby porównać metodologie, zespół zestawił dobór próby, miary wyniku oraz możliwe źródła błędu.",
    "c28-11": "Wywiady pomogły wyjaśnić rozbieżność między testem uwagi a subiektywną oceną produktywności.",
    "c28-12": "Eksperyment próbował kontrolować zmienną pory dnia, wyznaczając wszystkim podobne godziny spaceru.",
    "c28-13": "Autorzy postanowili zastrzec zakres wniosku do krótkich przerw podczas pracy zdalnej.",
    "c28-14": "Raport pozwolił wskazać lukę badawczą: brakowało długoterminowego porównania różnych rodzajów odpoczynku.",
    "c28-15": "Trzeba nie mylić korelacji z przyczynowością, gdy uczestnicy samodzielnie wybierają badaną aktywność.",
}


EXPLANATIONS = {
    ("c28-grammar", 0): "Spójnik „jednak” ogranicza siłę pozornej zgodności: podobny wynik nie wystarcza, jeśli oba badania korzystają z małych i podobnych prób.",
    ("c28-grammar", 1): "Konstrukcja „im…, tym…” wiąże jakość kontroli z ostrożnością wniosku: słabsza kontrola zmiennych pozwala mówić o związku, nie o przyczynie.",
    ("c28-grammar", 2): "Poprawny wniosek oddziela obserwowaną współzmienność od mechanizmu przyczynowego i jawnie wskazuje, że alternatywne wyjaśnienia nadal są możliwe.",
    ("c28-grammar", 3): "Sprzecznych źródeł nie liczy się jak głosów; waży się dobór próby, kontrolę zmiennych, trafność miar i zgodność metody z pytaniem.",
    ("c28-grammar", 4): "Umiarkowany stopień pewności oznacza, że kilka przesłanek wspiera wniosek, ale znane ograniczenia nie pozwalają traktować go jako rozstrzygającego.",
    ("c28-grammar", 5): "Luka badawcza nazywa dokładnie brakujący dowód: długoterminowe porównanie rodzajów przerw w różnych grupach zawodowych.",
    ("c28-quiz", 0): "Synteza źródeł łączy ustalenia z różnych materiałów w jeden ważony wniosek, zachowując ich zgodności, rozbieżności i ograniczenia.",
    ("c28-quiz", 1): "Triangulacja danych sprawdza zjawisko różnymi metodami lub źródłami; zgodność niezależnych perspektyw może zwiększyć wiarygodność interpretacji.",
    ("c28-quiz", 2): "Jakość dowodu zależy od tego, jak dobrze metoda odpowiada pytaniu i ogranicza błędy, a nie tylko od liczby uczestników.",
    ("c28-quiz", 3): "Próba badawcza to wybrana część populacji; sposób jej doboru decyduje, na kogo można ostrożnie uogólnić rezultat.",
    ("c28-quiz", 4): "Zmienna zakłócająca wpływa jednocześnie na badany czynnik i wynik, tworząc związek, który może błędnie wyglądać na przyczynowy.",
    ("c28-quiz", 5): "Ograniczenie metodologiczne wskazuje cechę projektu osłabiającą interpretację, na przykład krótki czas, samoobór albo nietrafną miarę.",
    ("c28-quiz", 6): "Stopień pewności komunikuje, jak silnie dostępne dowody wspierają wniosek; powinien maleć wraz z liczbą istotnych niewiadomych.",
    ("c28-quiz", 7): "Zbieżność wyników oznacza podobny kierunek ustaleń, lecz nie gwarantuje prawdy, zwłaszcza gdy źródła dzielą ten sam błąd.",
    ("c28-quiz", 8): "Ważyć dowody znaczy oceniać ich znaczenie według jakości i adekwatności metody, zamiast przyznawać każdemu źródłu równą siłę.",
    ("c28-quiz", 9): "Porównać metodologie to zestawić sposób doboru danych, pomiaru i kontroli błędów, aby wyjaśnić różną siłę wyników.",
    ("c28-reading-check", 0): "Pierwsze badanie objęło czterdzieści osób i wykazało niewielką poprawę wyniku w teście uwagi po krótkich spacerach.",
    ("c28-reading-check", 1): "Duża próba była obserwacyjna, a uczestnicy sami wybierali spacery, więc sen, motywacja i obciążenie pracą mogły zakłócać związek.",
    ("c28-reading-check", 2): "Wywiady zasugerowały alternatywny mechanizm: poprawa mogła wynikać z odcięcia od komunikatorów i przerwy poznawczej, nie wyłącznie z ruchu.",
    ("c28-reading-check", 3): "Za umiarkowanie pewny uznano wniosek, że regularne krótkie przerwy sprzyjają subiektywnej koncentracji, bez przesądzania przewagi spaceru.",
    ("c28-reading-check", 4): "Rekomendacja proponowała dobrowolny test niskiego ryzyka, ponieważ dowody nie uzasadniały przedstawiania spaceru jako obowiązkowej terapii wydajności.",
    ("c28-reading-check", 5): "Ostatni akapit wskazuje brak porównania rodzajów przerw oraz danych o długoterminowych skutkach w różnych zawodach.",
}


def improve_editorial_content(apps, schema_editor):
    Flashcard = apps.get_model("learning", "Flashcard")
    Question = apps.get_model("learning", "Question")
    for card_id, example in EXAMPLES.items():
        Flashcard.objects.filter(id=card_id).update(example=example)
    for (lesson_id, position), explanation in EXPLANATIONS.items():
        Question.objects.filter(lesson_id=lesson_id, position=position).update(explanation=explanation)


class Migration(migrations.Migration):
    dependencies = [("learning", "0077_improve_c2_expert_mediation_editorial")]
    operations = [migrations.RunPython(improve_editorial_content, migrations.RunPython.noop)]
