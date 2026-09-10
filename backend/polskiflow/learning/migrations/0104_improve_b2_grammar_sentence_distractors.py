from django.db import migrations


OPTION_FIXES = {
    "b2view-grammar": [
        "Mimo że rozumiem to zastrzeżenie, nowe dane potwierdzają nasz wniosek.",
        "Mimo że rozumiem to zastrzeżenie, nowe dane podważają nasz wniosek.",
        "Chociaż odrzucam to zastrzeżenie, wcześniejsze dane potwierdzają nasz wniosek.",
    ],
    "b2news-grammar": [
        "Świadek przekazał, że pociąg zatrzymał się przed stacją.",
        "Świadek przekazał, że pociąg zatrzyma się przed stacją.",
        "Świadek zaprzeczył, że pociąg zatrzymał się przed stacją.",
    ],
    "b2prof-grammar": [
        "Ustalono, że wdrożenie zostanie przesunięte na przyszły miesiąc.",
        "Ustalono, że wdrożenie zostanie przyspieszone w przyszłym miesiącu.",
        "Ustalono, że wdrożenie zostanie przesunięte na bieżący miesiąc.",
    ],
    "b2tech-grammar": [
        "Na podstawie wyników opracowano nowe rozwiązanie.",
        "Na podstawie wyników oceniono dotychczasowe rozwiązanie.",
        "Mimo uzyskanych wyników odrzucono nowe rozwiązanie.",
    ],
    "b2economy-grammar": [
        "Prawdopodobnie ten wariant będzie bardziej opłacalny w porównaniu z poprzednim.",
        "Z pewnością ten wariant będzie mniej opłacalny w porównaniu z poprzednim.",
        "Prawdopodobnie ten wariant będzie równie opłacalny jak poprzedni.",
    ],
    "b2law-grammar": [
        "W związku z brakiem odpowiedzi składam skargę na bezczynność organu.",
        "W związku z otrzymaniem odpowiedzi wycofuję skargę na bezczynność organu.",
        "Z powodu braku odpowiedzi składam wniosek o ponowne rozpatrzenie sprawy.",
    ],
    "b2psych-grammar": [
        "Z jego perspektywy mogła okazać więcej zrozumienia.",
        "Z jego perspektywy nie powinna okazywać większego zrozumienia.",
        "Z jej perspektywy to on mógł okazać więcej zrozumienia.",
    ],
    "b2lit-grammar": [
        "Bohaterka powiedziała, że wróci, ale narrator poddaje jej słowa w wątpliwość.",
        "Bohaterka powiedziała, że wróci, a narrator potwierdza prawdziwość jej słów.",
        "Bohaterka powiedziała, że nie wróci, ale narrator poddaje jej słowa w wątpliwość.",
    ],
    "b2discussion-grammar": [
        "Podsumowując, zgadzamy się co do celu, ale sposób pozostaje sporny.",
        "Podsumowując, nie zgadzamy się co do celu, a sposób pozostaje sporny.",
        "Podsumowując, cel pozostaje sporny, ale akceptujemy proponowany sposób.",
    ],
    "b2intercultural-grammar": [
        "Jeśli dobrze rozumiem, milczenie nie oznaczało sprzeciwu.",
        "Jeśli dobrze rozumiem, milczenie oznaczało wyraźny sprzeciw.",
        "Jeśli źle rozumiem, milczenie nie oznaczało zgody.",
    ],
    "b2academic-grammar": [
        "Na podstawie tej próby nie można sformułować ostatecznego wniosku.",
        "Na podstawie tej próby można sformułować ostateczny wniosek.",
        "Na podstawie całej populacji nie można przedstawić wstępnej hipotezy.",
    ],
    "b2final-grammar": [
        "Gdybyśmy powtórzyli projekt, wcześniej zebralibyśmy informację zwrotną.",
        "Gdybyśmy powtórzyli projekt, później zebralibyśmy informację zwrotną.",
        "Ponieważ powtórzyliśmy projekt, wcześniej zebraliśmy dane finansowe.",
    ],
}


def improve_options(apps, schema_editor):
    Question = apps.get_model("learning", "Question")
    for lesson_id, options in OPTION_FIXES.items():
        question = Question.objects.filter(lesson_id=lesson_id, position=5).first()
        if question is None:
            continue
        target = question.correct
        reordered = list(options[1:])
        reordered.insert(target, options[0])
        question.options = reordered
        question.save(update_fields=["options"])


class Migration(migrations.Migration):
    dependencies = [("learning", "0103_rebalance_a1_a2_question_options")]
    operations = [migrations.RunPython(improve_options, migrations.RunPython.noop)]
