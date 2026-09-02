from django.db import migrations


EXAMPLES = {
    "c15-1": "Spójność wywodu osłabła, gdy autorka wprowadziła nowy wątek bez powiązania go z wcześniejszą tezą.",
    "c15-2": "Każdy akapit problemowy analizuje jeden aspekt zjawiska i prowadzi do cząstkowego wniosku.",
    "c15-3": "Zdanie tematyczne zapowiada, że akapit porówna wpływ pracy zdalnej na produktywność dwóch grup.",
    "c15-4": "Łącznik „natomiast” sygnalizuje wyraźny kontrast między wynikami obu przywołanych badań.",
    "c15-5": "Synteza źródeł ujawniła, że pozornie sprzeczne wyniki dotyczą różnych grup wiekowych.",
    "c15-6": "Aby przywołać badanie, autorka podała nazwisko badaczki, rok publikacji i zakres analizowanej próby.",
    "c15-7": "Badacz powinien zastrzec, że niewielka próba nie pozwala uogólnić wyniku na całą populację.",
    "c15-8": "Po analizie danych trzeba doprecyzować tezę: korzyść dotyczy zadań indywidualnych, nie każdej formy pracy.",
    "c15-9": "Wywód prowadzi od definicji problemu przez analizę dowodów do ostrożnej konkluzji.",
    "c15-10": "Konkluzja odpowiada na pytanie badawcze i wskazuje granice sformułowanego wniosku.",
    "c15-11": "Argument poboczny o kosztach biura trafił do przypisu, ponieważ nie rozstrzygał głównego pytania.",
    "c15-12": "Hierarchia informacji jest czytelna: najpierw pojawia się teza, potem kluczowe dowody, a następnie wyjątki.",
    "c15-13": "Aby unikać powtórzeń, nie wystarczy zastępować słów synonimami; trzeba również łączyć pokrewne sądy.",
    "c15-14": "Przed oddaniem artykułu autorka musiała redagować przejścia między akapitami i usunąć dwa zbędne przykłady.",
    "c15-15": "Odsyłacz prowadzi do pełnego opisu źródła, dzięki czemu czytelnik może sprawdzić przywołane dane.",
}


EXPLANATIONS = {
    ("c15-grammar", 0): "Spójność wywodu oznacza logiczne powiązanie tezy, argumentów i wniosków; odbiorca powinien rozumieć, dlaczego kolejny element wynika z poprzedniego.",
    ("c15-grammar", 1): "Akapit problemowy rozwija jeden wyraźnie określony aspekt zagadnienia: stawia pytanie lub tezę cząstkową, analizuje dowody i domyka rozumowanie.",
    ("c15-grammar", 2): "Zdanie tematyczne sygnalizuje główną funkcję akapitu, dlatego pomaga czytelnikowi przewidzieć, czy nastąpi definicja, porównanie, argument czy zastrzeżenie.",
    ("c15-grammar", 3): "Łącznik ujawnia relację między fragmentami tekstu, na przykład kontrast, skutek albo dopowiedzenie; jego wybór musi odpowiadać rzeczywistej relacji logicznej.",
    ("c15-grammar", 4): "Synteza źródeł zestawia ustalenia według problemów i zależności, zamiast kolejno streszczać każdą publikację bez wspólnego wniosku.",
    ("c15-grammar", 5): "Przywołać badanie to wskazać jego autora lub instytucję oraz istotny wynik w sposób pozwalający odróżnić cudze ustalenie od własnego komentarza.",
    ("c15-quiz", 0): "Spójność wywodu dotyczy logicznego przebiegu rozumowania w całym tekście, a nie wyłącznie poprawności pojedynczych zdań.",
    ("c15-quiz", 1): "Akapit problemowy skupia się na jednym podproblemie i rozwija go za pomocą analizy, dowodów oraz cząstkowego wniosku.",
    ("c15-quiz", 2): "Zdanie tematyczne nazywa zasadniczą myśl albo zadanie akapitu i wyznacza ramę dla zdań, które po nim następują.",
    ("c15-quiz", 3): "Łącznik to środek językowy pokazujący relację między częściami wypowiedzi, na przykład jednak sygnalizuje przeciwstawienie lub zastrzeżenie.",
    ("c15-quiz", 4): "Synteza źródeł łączy wyniki kilku publikacji wokół wspólnego pytania, wskazując zgodności, różnice i możliwe przyczyny rozbieżności.",
    ("c15-quiz", 5): "Przywołać badanie oznacza odwołać się do konkretnej pracy i jasno zaznaczyć, które twierdzenie pochodzi z tego źródła.",
    ("c15-quiz", 6): "Zastrzec znaczy ograniczyć zakres twierdzenia przez podanie warunku, wyjątku albo źródła niepewności; nie jest to wycofanie całej tezy.",
    ("c15-quiz", 7): "Doprecyzować tezę to zawęzić lub uzupełnić ją tak, aby odpowiadała przedstawionym dowodom i nie obiecywała więcej, niż one uzasadniają.",
    ("c15-quiz", 8): "Wywód jest uporządkowanym tokiem argumentacji: obejmuje przesłanki, ich analizę oraz wynikające z nich wnioski.",
    ("c15-quiz", 9): "Konkluzja domyka analizę, odpowiadając na pytanie tekstu; może też nazwać ograniczenia i konsekwencje, zamiast mechanicznie powtarzać wstęp.",
    ("c15-reading-check", 0): "Argument o kosztach biura był poboczny wobec analizy badań nad pracą zdalną, więc przypis zachował informację bez zakłócania głównego toku.",
    ("c15-reading-check", 1): "Pierwszy akapit przedstawia temat eseju oraz materiał badawczy: trzy badania nad pracą zdalną, oparte na różnych metodach.",
    ("c15-reading-check", 2): "Drugi akapit opisuje organizację części analitycznych: zdanie tematyczne nazywa problem, a dalsze zdania porównują zgodne i sprzeczne wyniki.",
    ("c15-reading-check", 3): "Trzeci akapit pokazuje syntezę: Marta nie relacjonuje źródeł osobno, lecz zestawia wyniki, ograniczenia prób i własną tezę.",
    ("c15-reading-check", 4): "Czwarty akapit uzasadnia przeniesienie argumentu do przypisu tym, że zaburzał on spójność wywodu oraz hierarchię informacji.",
    ("c15-reading-check", 5): "Ostatni akapit odróżnia konkluzję od streszczenia: zakończenie odpowiada na pytanie i formułuje ostrożny dalszy wniosek.",
}


def improve_editorial_content(apps, schema_editor):
    Flashcard = apps.get_model("learning", "Flashcard")
    Question = apps.get_model("learning", "Question")

    for card_id, example in EXAMPLES.items():
        Flashcard.objects.filter(id=card_id).update(example=example)

    for (lesson_id, position), explanation in EXPLANATIONS.items():
        Question.objects.filter(lesson_id=lesson_id, position=position).update(
            explanation=explanation
        )


class Migration(migrations.Migration):
    dependencies = [("learning", "0067_improve_c1_mediation_editorial")]
    operations = [
        migrations.RunPython(improve_editorial_content, migrations.RunPython.noop)
    ]
