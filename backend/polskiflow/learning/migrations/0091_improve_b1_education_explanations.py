from django.db import migrations


EXPLANATIONS = {
    "b1edu-grammar": {
        0: "Spójnik ponieważ wprowadza rzeczywistą przyczynę regularnej nauki, czyli zamiar zdania egzaminu.",
        2: "W mowie zależnej twierdzenie po czasowniku powiedział wprowadzamy spójnikiem że, bez cudzysłowu.",
    },
    "b1edu-quiz": {
        2: "Stałe wyrażenie robić postępy oznacza stopniowo rozwijać umiejętności i osiągać lepsze wyniki.",
        3: "Spójnik chociaż wprowadza ustępstwo: brak zgody nie wyklucza zrozumienia komentarza nauczyciela.",
        4: "Po czasowniku powiedziała przekazujemy twierdzenie w mowie zależnej za pomocą spójnika że.",
        5: "Spójnik czy rozpoczyna w mowie zależnej pytanie, na które można odpowiedzieć tak albo nie.",
        6: "Konkretna informacja zwrotna wskazuje dokładny błąd i podpowiada, co należy poprawić.",
        8: "Spójnik ponieważ podaje przyczynę: zajęcia praktyczne pozwalają wykorzystać wiedzę teoretyczną w działaniu.",
    },
    "b1edu-reading-check": {
        0: "Lena zapisała się na kurs, aby pewniej prowadzić spotkania zawodowe po polsku.",
        5: "Lena uznała, że postęp wynika z regularnej, świadomej praktyki, a nie wyłącznie z talentu.",
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
    dependencies = [("learning", "0090_improve_b1_travel_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
