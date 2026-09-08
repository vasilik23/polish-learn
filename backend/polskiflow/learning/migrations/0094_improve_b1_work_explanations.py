from django.db import migrations


EXPLANATIONS = {
    "b1work-quiz": {
        0: "Stanowisko oznacza określoną funkcję lub miejsce pracownika w strukturze firmy albo instytucji.",
        1: "Wyrażenie należeć do łączy się z dopełniaczem, dlatego poprawna forma brzmi do obowiązków.",
        2: "Proces rekrutacji zwykle rozpoczyna kandydat, wysyłając CV z opisem doświadczenia i umiejętności.",
        7: "Szkolenie wspiera rozwój zawodowy, ponieważ pozwala zdobywać nowe kompetencje potrzebne w pracy.",
        8: "Forma mógłby Pan tworzy uprzejmą oficjalną prośbę odpowiednią w kontakcie zawodowym.",
        9: "Otrzymać awans oznacza przejść na wyższe stanowisko dzięki dobrym wynikom zawodowym.",
    },
    "b1work-reading-check": {
        0: "Lena szukała pracy dającej większą odpowiedzialność oraz możliwość dalszego rozwoju zawodowego.",
        1: "Przed wysłaniem CV Lena opisała konkretne osiągnięcia i ukończyła dodatkowy kurs.",
        2: "Kierownik poprosił Lenę o przykład reakcji na opóźnienie projektu, aby ocenić jej kompetencje.",
        3: "Lena spokojnie przedstawiła plan działania i rozmowę z klientem, pokazując własną inicjatywę.",
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
    dependencies = [("learning", "0093_improve_b1_culture_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
