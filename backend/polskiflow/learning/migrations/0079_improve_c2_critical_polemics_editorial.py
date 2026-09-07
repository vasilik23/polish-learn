from django.db import migrations


EXAMPLES = {
"c23-1":"Przed odpowiedzią recenzent wiernie odtworzył tezę oponenta, łącznie z warunkami ograniczającymi jej zakres.",
"c23-2":"Zasada życzliwości wymagała przyjąć najmocniejszą rozsądną interpretację wypowiedzi, zamiast wykorzystywać niezręczny skrót.",
"c23-3":"Argument stalowy uwzględniał najlepsze dane przeciwnika, dlatego jego późniejsza krytyka rzeczywiście dotyczyła sedna sporu.",
"c23-4":"Autor zbudował chochoł argumentacyjny, przypisując badaczom żądanie zakazu, którego nigdy nie sformułowali.",
"c23-5":"Punkt sporny dotyczył skali finansowania, choć obie strony zgadzały się co do celu programu.",
"c23-6":"Pierwsza przesłanka opierała się na nieaktualnym badaniu, więc nie mogła niezależnie podtrzymać całego rozumowania.",
"c23-7":"Konkluzja wykraczała poza przedstawione dane, ponieważ wyniki lokalne uogólniono na wszystkich mieszkańców kraju.",
"c23-8":"Ciężar dowodu spoczywał na autorze twierdzącym, że pojedyncza korelacja dowodzi skuteczności nowej polityki.",
"c23-9":"Można przyznać rację częściowo w sprawie kosztów, a nadal odrzucać proponowany sposób ich ograniczenia.",
"c23-10":"Recenzent postanowił zakwestionować przesłankę o reprezentatywności próby, nie podważając poprawności samych obliczeń.",
"c23-11":"Komentator powinien odróżnić fakt od oceny, zanim nazwie wzrost wydatków społeczną porażką.",
"c23-12":"Aby uniknąć nadinterpretacji, raport oddzielił wynik statystyczny od hipotezy dotyczącej jego możliwej przyczyny.",
"c23-13":"Badacz musiał sformułować zastrzeżenie, że obserwowany efekt może nie utrzymać się poza badaną grupą.",
"c23-14":"Aby dochować rzetelności, publicystka przytoczyła dane sprzeczne z jej stanowiskiem i wyjaśniła ich ograniczenia.",
"c23-15":"Po uznaniu mocnego kontrargumentu ekspert mógł pozostać przy swoim stanowisku, ale zawęził jego zakres.",
}

EXPLANATIONS = {
0:"Teza oponenta to rzeczywiste stanowisko drugiej strony; należy je odtworzyć wraz z zakresem i zastrzeżeniami przed rozpoczęciem krytyki.",
1:"Zasada życzliwości nakazuje wybierać najmocniejszą rozsądną interpretację cudzej wypowiedzi, dzięki czemu spór dotyczy idei, nie potknięć językowych.",
2:"Argument stalowy wzmacnia stanowisko przeciwnika do jego najlepszej wersji; obalenie takiej wersji jest poznawczo cenniejsze niż łatwego uproszczenia.",
3:"Chochoł argumentacyjny jest zniekształconą, łatwiejszą do zaatakowania wersją poglądu, którego rozmówca w rzeczywistości nie przedstawił.",
4:"Punkt sporny precyzyjnie wskazuje kwestię dzielącą strony i chroni dyskusję przed pozornym konfliktem wokół celów już wspólnie zaakceptowanych.",
5:"Przesłanka jest zdaniem wspierającym dalszy wniosek; zakwestionowanie jej prawdziwości lub adekwatności może osłabić całą strukturę argumentu.",
6:"Konkluzja wynika z przesłanek tylko w granicach, które one uzasadniają; szersze twierdzenie wymaga dodatkowych danych albo jawnego zastrzeżenia.",
7:"Ciężar dowodu określa, kto powinien uzasadnić twierdzenie; zwykle spoczywa na osobie wprowadzającej mocną lub nietypową tezę.",
8:"Przyznać rację częściowo znaczy zaakceptować trafny fragment argumentu bez automatycznej zgody na wszystkie przesłanki, wnioski i rekomendacje.",
9:"Zakwestionować przesłankę to podważyć podstawę rozumowania, na przykład reprezentatywność próby, zamiast zaprzeczać samej konkluzji bez uzasadnienia.",
}

def forwards(apps, schema_editor):
    Flashcard=apps.get_model("learning","Flashcard"); Question=apps.get_model("learning","Question")
    for key,value in EXAMPLES.items(): Flashcard.objects.filter(id=key).update(example=value)
    for position,value in EXPLANATIONS.items(): Question.objects.filter(lesson_id="c23-quiz",position=position).update(explanation=value)

class Migration(migrations.Migration):
    dependencies=[("learning","0078_improve_c2_research_synthesis_editorial")]
    operations=[migrations.RunPython(forwards,migrations.RunPython.noop)]
