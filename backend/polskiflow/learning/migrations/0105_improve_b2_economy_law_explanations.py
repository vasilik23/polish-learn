from django.db import migrations


EXPLANATIONS = {
    "b2economy-grammar": {
        0: "Przyimek „o” wskazuje wielkość zmiany, dlatego sprzedaż wzrosła właśnie o dwanaście procent.",
        1: "Konstrukcja „z… do…” podaje wartość początkową i końcową badanego udziału.",
        2: "Po stopniu wyższym używamy „niż”, gdy bezpośrednio porównujemy dwa konkretne okresy.",
        3: "Przysłówek „prawdopodobnie” przedstawia stabilizację jako prognozę, a nie pewny fakt.",
    },
    "b2economy-quiz": {
        0: "Siła nabywcza określa ilość dóbr, które można kupić za posiadany dochód.",
        1: "Spadek o 12 zł wobec początkowych 120 zł stanowi dokładnie dziesięć procent.",
        2: "Popyt opisuje zapotrzebowanie kupujących, natomiast podaż dotyczy towarów oferowanych przez sprzedawców.",
        3: "Przyimek „o” odpowiada na pytanie, o jaką wartość zwiększył się dochód.",
        4: "Zwrot „możliwe, że” ogranicza pewność wniosku i sygnalizuje jedynie prawdopodobny rozwój sytuacji.",
        5: "Opłacalność uwzględnia łączny koszt oraz odpowiednią jakość, a nie tylko cenę początkową.",
        6: "Wzrost z 20% do 30% oznacza różnicę dziesięciu punktów procentowych.",
        7: "Czasownik „wahać się” opisuje naprzemienne wzrosty i spadki wartości w badanym okresie.",
        8: "Rozsądna decyzja wymaga porównania całkowitych kosztów, warunków umowy oraz własnych potrzeb.",
        9: "Czas przyszły i słowo „prawdopodobnie” wskazują, że zdanie przedstawia prognozę.",
    },
    "b2economy-reading-check": {
        1: "W pierwszym akapicie abonament obejmuje nie tylko urządzenie, lecz także jego naprawy.",
        2: "Przy najwyższej miesięcznej opłacie suma po czterech latach może osiągnąć 3900 złotych.",
        3: "Firmy rozwijają subskrypcje, ponieważ stałe przychody ułatwiają im przewidywanie przyszłych wpływów.",
        4: "Tekst ostrzega zarówno przed podwyżką opłat, jak i karą za wcześniejsze rozwiązanie umowy.",
        5: "Końcowy wniosek zaleca porównać pełne koszty, warunki umowy oraz rzeczywiste potrzeby.",
    },
    "b2law-grammar": {
        0: "Rzeczownik „prośba” łączy się z przyimkiem „o”, który wprowadza jej przedmiot.",
        1: "Czasownik zwrotny „odwołać się” wymaga przyimka „od” oraz rzeczownika w dopełniaczu.",
        2: "Stałe połączenie „ubiegać się o” nazywa świadczenie, które ktoś chce uzyskać.",
        3: "Wyrażenie „zgodnie z” wprowadza regulamin jako podstawę określającą wymagany termin odpowiedzi.",
        4: "Po „proszę o” używamy rzeczownika odczasownikowego, a „na podstawie” wymaga dopełniacza.",
        5: "Wyrażenie „w związku z” wymaga narzędnika, natomiast skargę składamy „na” bezczynność.",
    },
    "b2law-quiz": {
        0: "Załącznik jest dokumentem dołączanym do pisma, gdy wymaga go dana procedura.",
        1: "Od decyzji można się odwołać, ponieważ czasownik ten tworzy połączenie „odwołać się od”.",
        2: "Formuła „zwracam się z prośbą” jest neutralna, precyzyjna i odpowiednia dla oficjalnego pisma.",
        3: "Wyrażenie „na podstawie ustawy” wskazuje akt prawny będący podstawą działania urzędu.",
        4: "Uzasadnienie przedstawia faktyczne i prawne powody, które doprowadziły do danego rozstrzygnięcia.",
        5: "Stałe połączenie „ubiegać się o” wymaga przyimka „o” przed nazwą oczekiwanego dokumentu.",
        6: "Gdy termin upływa, kończy się czas przewidziany na wykonanie wymaganej czynności.",
        7: "Konkretne żądanie, jego podstawa i załączniki pozwalają organowi sprawnie ocenić wniosek.",
        8: "Przed grupą spółgłosek używamy wariantu „ze”, dlatego mówimy „w związku ze zmianą”.",
        9: "Sprawę rozpatruje organ właściwy według rodzaju sprawy i obowiązujących przepisów.",
    },
    "b2law-reading-check": {
        0: "W pouczeniu do decyzji wyraźnie wskazano czternastodniowy termin na wniesienie odwołania.",
        1: "Urząd odmówił świadczenia, ponieważ uznał, że do wniosku nie dołączono dokumentu o dochodzie.",
        2: "Marta dysponowała elektronicznym potwierdzeniem, że wymagany plik został wysłany przez platformę.",
        3: "W odwołaniu Marta zażądała ponownego rozpatrzenia sprawy oraz zmiany wcześniejszej decyzji.",
        4: "Rezygnacja z ocen pracownika pozwoliła Marcie skupić oficjalne pismo na sprawdzalnych faktach.",
        5: "Przed wysłaniem pisma tekst zaleca sprawdzić właściwy organ, termin oraz sposób doręczenia.",
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
    dependencies = [("learning", "0104_improve_b2_grammar_sentence_distractors")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
