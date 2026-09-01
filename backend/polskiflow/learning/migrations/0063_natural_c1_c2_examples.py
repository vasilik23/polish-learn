from django.db import migrations


EXAMPLES = {
    "c11-1": "Ten sam żart sprawdzi się w rozmowie, lecz nie w oficjalnym rejestrze.",
    "c11-2": "Precyzyjny dobór słów złagodził krytykę bez osłabiania argumentu.",
    "c11-3": "Zwrot grzecznościowy otwiera prośbę, ale nie zastępuje jasnego celu.",
    "c11-4": "Potoczny ton skrócił dystans między prowadzącą a publicznością.",
    "c11-5": "Neutralny opis oddziela wynik badania od opinii autora.",
    "c11-6": "Oficjalny komunikat podaje podstawę decyzji i termin odwołania.",
    "c11-7": "Redaktorka musiała dostosować wypowiedź do odbiorców spoza branży.",
    "c11-8": "W pierwszym liście warto zachować dystans, nie popadając w chłód.",
    "c11-9": "Prowadzący skrócił dystans, zwracając się do uczestników po imieniu.",
    "c11-10": "Nawet dobra rada może brzmieć protekcjonalnie, gdy ignoruje doświadczenie rozmówcy.",
    "c11-11": "Żart okazał się niestosowny w oficjalnym wystąpieniu.",
    "c11-12": "Adresat zna temat, lecz nie musi znać specjalistycznej terminologii.",
    "c11-13": "Kontekst sytuacyjny decyduje, czy bezpośrednia prośba zabrzmi uprzejmie.",
    "c11-14": "Trzeba przeredagować akapit, aby usunąć niezamierzoną ironię.",
    "c11-15": "Autorka wyważyła ton między stanowczością a otwartością na dialog.",
    "c21-1": "Pytanie «kiedy przestałeś?» zawiera presupozycję, że dana czynność wcześniej trwała.",
    "c21-2": "Odpowiedź «część wyników jest obiecująca» może nieść implikaturę, że reszta rozczarowuje.",
    "c21-3": "Celowe niedopowiedzenie pozwoliło autorce zachować napięcie do ostatniego akapitu.",
    "c21-4": "Wieloznaczność zaimka sprawiła, że nie było jasne, kto podjął decyzję.",
    "c21-5": "Dosłowność cytatu nie przesądza jeszcze o intencji mówiącego.",
    "c21-6": "Odczytanie intencji wymaga uwzględnienia tonu, relacji i sytuacji.",
    "c21-7": "Ironia nadała pozornie neutralnemu zdaniu krytyczny sens naddany.",
    "c21-8": "Z kontekstu wynika, że propozycja była próbą kompromisu, nie ultimatum.",
    "c21-9": "Rzecznik uchylił się od odpowiedzi, powtarzając jedynie treść komunikatu.",
    "c21-10": "Mówczyni zasugerowała mimochodem, że termin może ulec zmianie.",
    "c21-11": "Przed debatą należy doprecyzować zakres pojęcia odpowiedzialności.",
    "c21-12": "Dodanie nazwiska pozwoliło rozbroić dwuznaczność ostatniego zdania.",
    "c21-13": "Autor pozostawił pole do interpretacji, nie wskazując motywów bohaterki.",
    "c21-14": "Czytając między wierszami, nie wolno przedstawiać hipotezy jako faktu.",
    "c21-15": "Nie bez znaczenia pozostaje moment, w którym opublikowano sprostowanie.",
}


def replace_template_examples(apps, schema_editor):
    Flashcard = apps.get_model("learning", "Flashcard")
    for card_id, example in EXAMPLES.items():
        Flashcard.objects.filter(id=card_id).update(example=example)


class Migration(migrations.Migration):
    dependencies = [("learning", "0062_editorial_sample_a1_c2")]
    operations = [
        migrations.RunPython(replace_template_examples, migrations.RunPython.noop)
    ]
