from django.db import migrations


EXPLANATIONS = {
    "b1soc-grammar": {
        0: "„Ponieważ” wprowadza przyczynę: autor popiera projekt dlatego, że ułatwi on życie starszym mieszkańcom.",
        1: "„Chociaż” sygnalizuje ustępstwo: koszt projektu nie przekreśla jego możliwych długoterminowych korzyści.",
        2: "„Więc” wprowadza skutek braku bezpiecznych przejść: mieszkańcy zwracają się z prośbą o zmiany.",
        3: "Po wyrażeniu opinii podajemy uzasadnienie: nawet niewielkie działanie może przynieść zauważalny efekt.",
        4: "Zdanie z „chociaż” zestawia różne opinie z możliwością osiągnięcia wspólnego rozwiązania.",
    },
    "b1soc-quiz": {
        2: "„Jednak” łączy zalety projektu z przeciwnym argumentem dotyczącym jego wysokiego kosztu.",
        3: "„Dlatego” wprowadza propozycję parku jako logiczny skutek rozpoznanego braku zieleni.",
    },
    "b1soc-reading-check": {
        2: "Maja protokołowała argumenty obu stron, dzięki czemu żaden ważny głos nie został pominięty.",
        3: "Kompromis polegał na podziale przestrzeni między plac zabaw a spokojną strefę zieleni.",
        4: "Wspólny projekt zbliżył sąsiadów, ponieważ razem szukali rozwiązania odpowiadającego różnym potrzebom.",
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
    dependencies = [("learning", "0086_improve_b1_final_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
