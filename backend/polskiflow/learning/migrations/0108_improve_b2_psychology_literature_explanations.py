from django.db import migrations


EXPLANATIONS = {
    "b2psych-grammar": {
        0: "Przysłówek „prawdopodobnie” przedstawia przyczynę jako hipotezę, ponieważ nie znamy wszystkich okoliczności.",
        1: "Konstrukcja „wydawało się” opisuje subiektywną ocenę sytuacji z perspektywy konkretnej osoby.",
        2: "Po czasowniku modalnym „mogła” występuje bezokolicznik „powiedzieć”, który nazywa niewykorzystaną możliwość.",
        3: "Wyrażenie „być może” oddziela ostrożne przypuszczenie od pewnego stwierdzenia o cudzych intencjach.",
        4: "„Prawdopodobnie” sygnalizuje hipotezę, a „ponieważ” wprowadza możliwą przyczynę jej wycofania.",
        5: "Zwrot „z jego perspektywy” ogranicza ocenę do punktu widzenia jednej osoby.",
    },
    "b2psych-quiz": {
        0: "Stawianie granic polega na jasnym komunikowaniu potrzeb i zachowań akceptowanych w relacji.",
        1: "„Być może” wyraża możliwość, dlatego nie przedstawia domysłu jako bezspornego faktu.",
        2: "Czasownik „przypisywać” łączy się z celownikiem osoby i biernikiem przypisywanej cechy.",
        3: "Nazwanie emocji i krótka przerwa pomagają obniżyć napięcie przed udzieleniem odpowiedzi.",
        4: "Forma „mogła powiedzieć” wskazuje na alternatywny sposób zachowania dostępny w przeszłości.",
        5: "„Prawdopodobnie” wyraźnie ogranicza pewność sądu i pozostawia miejsce na inne wyjaśnienia.",
        6: "Stałe połączenie „dojść do porozumienia” oznacza osiągnąć wspólne stanowisko po rozmowie.",
        7: "Żal wynika z niezauważonej potrzeby, więc zdanie podaje konkretną przyczynę emocji.",
        8: "Empatyczna reakcja nazywa możliwe uczucie rozmówcy bez oceniania go ani narzucania interpretacji.",
        9: "Zwrot „z jej perspektywy” przedstawia sytuację z punktu widzenia wskazanej osoby.",
    },
    "b2psych-reading-check": {
        0: "Lena czuła żal, ponieważ decyzje dotyczące wspólnego wyjazdu podjęto bez jej udziału.",
        1: "Tekst ostrożnie sugeruje, że Michał unikał konfrontacji z obawy przed impulsywną reakcją.",
        2: "Ustalona zasada oddziela obserwację od emocji i potrzeb, ograniczając wzajemne oskarżenia.",
        3: "Michał przyznał, że nie zapytał Leny o zdanie przed podjęciem wspólnej decyzji.",
        4: "Lena jasno zakomunikowała potrzebę uczestniczenia w decyzjach dotyczących ich wspólnych planów.",
        5: "Ostrożna modalność pomaga odróżnić opisane fakty od przypuszczeń o motywach bohaterów.",
    },
    "b2lit-grammar": {
        0: "Konstrukcja „odczytać jako” służy przedstawieniu uzasadnionej interpretacji obrazu lub motywu.",
        1: "W mowie zależnej zmieniamy „nie znam” na formę „nie zna” zgodną z narratorką.",
        2: "Spójnik „aby” wprowadza cel przywołania obrazu pustego peronu przez reżysera.",
        3: "Wyrażenie „dzięki temu” wskazuje skutek niejednoznacznego finału: możliwość własnej interpretacji.",
        4: "Zwrot „można odczytać jako” ostrożnie proponuje symboliczne znaczenie obrazu, nie ogłasza pewnika.",
        5: "Mowa zależna zachowuje zapowiedź powrotu, a „poddaje w wątpliwość” sygnalizuje dystans narratora.",
    },
    "b2lit-quiz": {
        0: "Fabuła to uporządkowany ciąg wydarzeń przedstawionych w dziele literackim albo filmowym.",
        1: "Zdanie o pustym peronie wyjaśnia możliwe znaczenie obrazu, dlatego jest interpretacją.",
        2: "Cytat wspiera argument tylko wtedy, gdy recenzent objaśnia jego znaczenie w kontekście.",
        3: "Tempo, montaż i ograniczanie informacji sterują oczekiwaniami widza, dzięki czemu budują napięcie.",
        4: "Niejednoznaczny finał pozostawia kilka interpretacji, o ile każdą można uzasadnić elementami dzieła.",
        5: "Czasownik „odwoływać się” wymaga przyimka „do” i wskazuje świadome nawiązanie do legendy.",
        6: "W mowie zależnej forma „nie wróci” zachowuje przyszłe znaczenie pierwotnej wypowiedzi bohatera.",
        7: "Przekonująca recenzja łączy tezę z przykładami oraz wyjaśnia podstawę sformułowanej oceny.",
        8: "Warstwa wizualna obejmuje kolor, kadr, światło i kompozycję widocznego obrazu filmowego.",
        9: "Formuła „można interpretować jako” zaznacza, że proponowane odczytanie nie jest jedynym możliwym.",
    },
    "b2lit-reading-check": {
        0: "Ida wraca do miasta, aby uporządkować mieszkanie pozostałe po zmarłym dziadku.",
        1: "Powracające światło na peronie można odczytać jako oczekiwanie i próbę nawiązania kontaktu.",
        2: "Film buduje napięcie krótkimi rozmowami oraz wiadomościami urwanymi przed pełnym wyjaśnieniem.",
        3: "Wiadomość ujawnia, że siostra również próbowała nawiązać kontakt, co zmienia ocenę milczenia.",
        4: "Finał pozostaje otwarty, ponieważ widz nie dowiaduje się, kto nadchodzi w ciemności.",
        5: "Recenzent uznaje zakończenie za spójne z powracającymi obrazami oraz głównym tematem pamięci.",
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
    dependencies = [("learning", "0107_improve_b2_professional_science_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
