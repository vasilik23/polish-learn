from django.db import migrations


EXPLANATIONS = {
    "b1rel-quiz": {
        1: "Wyrażenie liczyć na kogoś oznacza ufać, że dana osoba udzieli potrzebnego wsparcia.",
        3: "Po stopniu wyższym bardziej otwarty używamy przyimka od oraz rzeczownika w dopełniaczu.",
        4: "Czasownik opowiedzieć łączy się z celownikiem, dlatego poprawną formą zaimka jest której.",
        5: "Konstrukcja tak samo jak porównuje równy stopień cechy u nas i naszych rodziców.",
        6: "Spokojna i szczera rozmowa pozwala obu stronom wyjaśnić potrzeby oraz zakończyć nieporozumienie.",
        8: "Czasownik dogadać się oznacza osiągnąć wzajemne porozumienie mimo wcześniejszej różnicy zdań.",
    },
    "b1rel-reading-check": {
        0: "Ola i Michał pokłócili się, ponieważ mieli różne oczekiwania dotyczące wspólnego wyjazdu.",
        2: "Michał zaproponował, aby każda osoba spokojnie opisała własne potrzeby dotyczące wyjazdu.",
        3: "Ola potrzebowała spokojnego odpoczynku bez pośpiechu, zamiast codziennych długich wędrówek.",
        4: "Kompromis połączył potrzeby obojga: wspólną aktywność oraz czas na spokojny odpoczynek.",
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
    dependencies = [("learning", "0095_improve_b1_health_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
