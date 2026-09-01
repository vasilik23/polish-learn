from django.db import migrations


EXAMPLES = {
    "c14-1": "Sedno raportu jest proste: dodatkowa zieleń ograniczy ryzyko podtopień po gwałtownych ulewach.",
    "c14-2": "Odbiorca niespecjalistyczny potrzebuje objaśnienia terminu, a nie pełnej listy technicznych parametrów.",
    "c14-3": "Ekspertka przełożyła na prosty język zależność między szczelną nawierzchnią a szybkim odpływem wody.",
    "c14-4": "Aby uniknąć uproszczenia, prowadzący zaznaczył, że proponowane rozwiązanie zmniejsza ryzyko, lecz go nie usuwa.",
    "c14-5": "Zanim przedstawiła wyniki, badaczka objaśniła pojęcie retencji na przykładzie osiedlowego ogrodu deszczowego.",
    "c14-6": "W podsumowaniu trzeba zachować zastrzeżenie, że prognoza opiera się na danych z jednego sezonu.",
    "c14-7": "Moderator uporządkował informacje: najpierw nazwał problem, potem przyczyny, a na końcu możliwe działania.",
    "c14-8": "Żeby wyjaśnić działanie mokradeł, edukatorka podała analogię do gąbki zatrzymującej część wody.",
    "c14-9": "Wykres pomaga wyjaśnić zależność między powierzchnią terenów zielonych a tempem odpływu deszczówki.",
    "c14-10": "Można pominąć detal konstrukcyjny, jeśli nie zmienia on decyzji, którą mają podjąć mieszkańcy.",
    "c14-11": "Po każdym etapie ekspert prosił uczestników o przykład, aby sprawdzić zrozumienie omawianej zależności.",
    "c14-12": "Na końcu rzeczniczka podsumowała trzy warianty, ich koszty oraz najważniejsze ograniczenia.",
    "c14-13": "Tłumacz środowiskowy pomagał pośredniczyć między inżynierami a mieszkańcami podczas konsultacji projektu.",
    "c14-14": "Krótka wersja powinna wiernie oddać sens raportu, nawet jeśli pomija część danych technicznych.",
    "c14-15": "Prowadząca stopniowała trudność: zaczęła od przykładu, a dopiero później wprowadziła fachowe pojęcia.",
}


EXPLANATIONS = {
    ("c14-grammar", 0): "Sedno to najważniejsza myśl komunikatu; mediator wybiera ją przed skracaniem tekstu, aby odbiorca nie zgubił głównego wniosku.",
    ("c14-grammar", 1): "Odbiorca niespecjalistyczny nie zna zawodowego kodu danej dziedziny, dlatego potrzebuje jasnych definicji i kontekstu zamiast żargonu.",
    ("c14-grammar", 2): "Przełożyć na prosty język znaczy wyrazić tę samą treść przystępniej, bez zmiany zależności, warunków ani stopnia pewności.",
    ("c14-grammar", 3): "Uniknąć uproszczenia to zachować informacje konieczne do poprawnego rozumienia, nawet gdy pomijamy mniej istotne szczegóły.",
    ("c14-grammar", 4): "Objaśnić pojęcie można przez krótką definicję, przykład lub kontrast; samo zastąpienie terminu łatwiejszym słowem nie zawsze wystarcza.",
    ("c14-grammar", 5): "Zachować zastrzeżenie oznacza przenieść do streszczenia warunek lub ograniczenie, które wpływa na zakres prawdziwości wniosku.",
    ("c14-quiz", 0): "Sedno odpowiada na pytanie, co odbiorca powinien zapamiętać przede wszystkim; nie jest listą wszystkich informacji z materiału.",
    ("c14-quiz", 1): "Odbiorca niespecjalistyczny może rozumieć problem, choć nie zna terminologii; komunikat należy więc dostosować, a nie infantylizować.",
    ("c14-quiz", 2): "Przekład na prosty język zachowuje sens oryginału, ale zmienia słownictwo, składnię i kolejność informacji na bardziej przystępne.",
    ("c14-quiz", 3): "Uproszczenie staje się zniekształceniem, gdy usuwa ważny warunek, skalę ryzyka albo relację przyczynową obecną w źródle.",
    ("c14-quiz", 4): "Objaśnienie pojęcia łączy termin z jego znaczeniem w danym kontekście, dzięki czemu odbiorca potrafi dalej śledzić wywód.",
    ("c14-quiz", 5): "Zastrzeżenie ogranicza zasięg twierdzenia, na przykład wskazuje warunek lub niepewność; wierna mediacja nie może go usuwać.",
    ("c14-quiz", 6): "Uporządkowanie informacji buduje czytelną kolejność, na przykład problem–przyczyna–skutek–rozwiązanie, i zmniejsza obciążenie odbiorcy.",
    ("c14-quiz", 7): "Analogia przybliża nieznane zjawisko przez podobieństwo do znanego doświadczenia, ale warto również wskazać granice porównania.",
    ("c14-quiz", 8): "Wyjaśnić zależność to pokazać, jak zmiana jednego elementu wpływa na drugi, zamiast jedynie wymienić oba fakty.",
    ("c14-quiz", 9): "Pominąć detal można wtedy, gdy nie zmienia on głównego wniosku, warunków jego obowiązywania ani decyzji odbiorcy.",
    ("c14-reading-check", 0): "Analityczka porównała zieleń do gąbki: obraz pokazuje zdolność zatrzymywania wody, a późniejsze zastrzeżenie wyznacza granicę analogii.",
    ("c14-reading-check", 1): "Pierwszy akapit określa zadanie mediacyjne: specjalistyczny raport o retencji trzeba wyjaśnić mieszkańcom bez wiedzy technicznej.",
    ("c14-reading-check", 2): "Drugi akapit wydobywa sedno raportu i przedstawia prosty związek między zielenią, wolniejszym odpływem a ryzykiem podtopień.",
    ("c14-reading-check", 3): "Trzeci akapit łączy przystępną analogię z ważnym zastrzeżeniem, dzięki czemu porównanie nie obiecuje pełnej ochrony przed ulewą.",
    ("c14-reading-check", 4): "Czwarty akapit pokazuje świadomą selekcję: wzory można pominąć, lecz liczby potrzebne do porównania wariantów trzeba zachować i objaśnić.",
    ("c14-reading-check", 5): "Ostatni akapit opisuje sprawdzanie zrozumienia przez własne podsumowanie odbiorców, bez infantylizowania ich ani odpytywania z terminów.",
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
    dependencies = [("learning", "0066_improve_c1_analytical_reading_editorial")]
    operations = [
        migrations.RunPython(improve_editorial_content, migrations.RunPython.noop)
    ]
