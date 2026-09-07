from django.db import migrations


EXAMPLES = {
    "c19-1": "Konwencja gatunkowa reportażu pozwala autorce budować napięcie scenami, których nie pomieściłaby krótka depesza.",
    "c19-2": "Lead podaje najważniejszy fakt i jego znaczenie, zanim czytelnik przejdzie do szczegółów decyzji rady miasta.",
    "c19-3": "Nagłówek wartościujący nazwał reformę porażką, choć przytoczone dane nie uzasadniały tak jednoznacznej oceny.",
    "c19-4": "Rama przekazu przesunęła uwagę z kosztu inwestycji na pytanie, kto rzeczywiście skorzysta z nowych połączeń.",
    "c19-5": "Depesza ograniczała się do czasu, miejsca i potwierdzonych liczb, pozostawiając interpretację późniejszym komentarzom.",
    "c19-6": "Felieton świadomie wyostrzył konflikt wartości, ale autor wyraźnie zaznaczył, gdzie kończą się fakty, a zaczyna opinia.",
    "c19-7": "Redakcja opublikowała sprostowanie, gdy okazało się, że podpis pod wykresem przypisywał dane niewłaściwej instytucji.",
    "c19-8": "Autoryzacja wypowiedzi objęła brzmienie cytatów ekspertki, lecz nie dała jej prawa do zmiany pytań dziennikarki.",
    "c19-9": "Skrót myślowy o rzekomej zgodzie mieszkańców zacierał różnice między wynikami dwóch niezależnych badań.",
    "c19-10": "Selekcja informacji uwypukliła protesty, a niemal pominęła konsultacje, przez co wydarzenie wyglądało na bardziej jednostronne.",
    "c19-11": "Aby przekształcić gatunek, studentka skróciła analizę do depeszy, zachowując źródła, datę i najważniejsze zastrzeżenie.",
    "c19-12": "Redaktor chciał zachować sens wypowiedzi, dlatego nie usunął z cytatu warunku ograniczającego pewność prognozy.",
    "c19-13": "Publicysta postanowił wyostrzyć tezę, zestawiając obietnice urzędu z rezultatami poprzedniego, nieskutecznego programu.",
    "c19-14": "W serwisie informacyjnym trzeba oddzielić komentarz prowadzącego od relacji o tym, co faktycznie ustalili kontrolerzy.",
    "c19-15": "Odpowiedzialność redakcyjna wymaga poprawienia błędu w widocznym miejscu, a nie tylko cichej podmiany artykułu.",
}


EXPLANATIONS = {
    ("c19-grammar", 0): "Konwencja gatunkowa to utrwalony zestaw cech danego typu przekazu, na przykład tempo depeszy, osobisty ton felietonu albo sceniczność reportażu.",
    ("c19-grammar", 1): "Lead otwiera materiał i kondensuje jego najważniejszą informację; powinien pozwolić odbiorcy szybko rozpoznać temat oraz znaczenie zdarzenia.",
    ("c19-grammar", 2): "Nagłówek wartościujący nie tylko zapowiada temat, lecz także narzuca ocenę słowami takimi jak „porażka” czy „przełom”, zanim pojawią się dowody.",
    ("c19-grammar", 3): "Rama przekazu decyduje, z jakiej perspektywy odbiorca interpretuje fakty: ten sam program można przedstawić jako koszt, inwestycję albo kwestię równości.",
    ("c19-grammar", 4): "Depesza przekazuje szybko zweryfikowane podstawowe fakty i źródła; ogranicza komentarz oraz szczegółową interpretację właściwą innym gatunkom.",
    ("c19-grammar", 5): "Felieton dopuszcza wyrazisty autorski głos, ironię i ocenę, ale jego konwencja nie zwalnia autora z uczciwego przedstawiania faktów.",
    ("c19-quiz", 0): "Konwencja gatunkowa określa oczekiwaną formę, ton i sposób organizacji treści, dlatego wpływa na to, jak materiał zostanie napisany i odczytany.",
    ("c19-quiz", 1): "Lead jest krótkim otwarciem materiału informacyjnego: wybiera sedno wydarzenia i zachęca do poznania dalszych, bardziej szczegółowych informacji.",
    ("c19-quiz", 2): "Nagłówek wartościujący zawiera interpretację lub ocenę; może ukierunkować reakcję odbiorcy jeszcze przed przeczytaniem argumentów i danych.",
    ("c19-quiz", 3): "Rama przekazu porządkuje fakty wokół wybranego problemu i przez tę selekcję podpowiada odbiorcy, co uznać za najważniejsze.",
    ("c19-quiz", 4): "Depesza jest zwięzłą informacją agencyjną opartą na szybko sprawdzalnych faktach, którą redakcje mogą dalej rozwijać w innych formach.",
    ("c19-quiz", 5): "Felieton to gatunek publicystyczny z rozpoznawalnym głosem autora; subiektywność jest w nim jawna, a nie ukryta pod pozorem neutralnej wiadomości.",
    ("c19-quiz", 6): "Sprostowanie koryguje opublikowaną informację nieprawdziwą lub nieścisłą i powinno jasno wskazywać, co w pierwotnym materiale wymaga poprawy.",
    ("c19-quiz", 7): "Autoryzacja wypowiedzi pozwala rozmówcy sprawdzić brzmienie własnych cytatów, nie oznacza jednak przejęcia przez niego redakcyjnej kontroli nad materiałem.",
    ("c19-quiz", 8): "Skrót myślowy pomija część rozumowania lub warunków; bywa ekonomiczny, ale może zniekształcić wniosek, gdy odbiorca nie zna brakującego kontekstu.",
    ("c19-quiz", 9): "Selekcja informacji jest nieuniknionym wyborem faktów do publikacji; jej skutki trzeba oceniać, pytając również o dane i perspektywy pominięte.",
    ("c19-reading-check", 0): "W trzecim akapicie redaktorka usuwa nagłówek sugerujący skutek, którego nie potwierdzały dane; nie rezygnuje ani z liczb, ani z całego posta.",
    ("c19-reading-check", 1): "Pierwszy akapit ustanawia wspólne źródło eksperymentu: jedna depesza ma zostać przekształcona w trzy różne materiały medialne.",
    ("c19-reading-check", 2): "Drugi akapit kontrastuje neutralny lead wiadomości z oceniającym felietonem, pokazując, jak gatunek zmienia ton oraz siłę tezy.",
    ("c19-reading-check", 3): "Trzeci akapit pokazuje granicę skracania: format posta wymaga kondensacji, ale nie usprawiedliwia niepotwierdzonej sugestii w nagłówku.",
    ("c19-reading-check", 4): "Czwarty akapit wymienia elementy niepodlegające swobodnej transformacji — liczby, źródło i zastrzeżenia — oraz nakazuje oznaczyć komentarz.",
    ("c19-reading-check", 5): "Ostatni akapit formułuje wniosek ćwiczenia: można zmieniać selekcję i ton zgodnie z gatunkiem, lecz sens faktów musi pozostać nienaruszony.",
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
    dependencies = [("learning", "0073_index_lesson_result_events_lesson")]
    operations = [
        migrations.RunPython(improve_editorial_content, migrations.RunPython.noop)
    ]
