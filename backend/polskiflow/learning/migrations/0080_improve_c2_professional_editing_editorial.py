from django.db import migrations

EXAMPLES={
"c24-1":"Redakcja merytoryczna ujawniła, że wniosek raportu nie wynikał z przedstawionych danych porównawczych.",
"c24-2":"Redakcja stylistyczna skróciła ciężkie zdania, nie zmieniając stanowiska ani charakterystycznego tonu autorki.",
"c24-3":"Spójność globalna poprawiła się, gdy każdy rozdział zaczął prowadzić do głównego pytania analizy.",
"c24-4":"Tok wywodu załamywał się, ponieważ przykład pojawiał się przed tezą, którą miał dopiero ilustrować.",
"c24-5":"Hierarchia informacji wymagała przeniesienia kluczowego rezultatu przed szczegóły procedury technicznej.",
"c24-6":"Remat zdania zawiera nową informację, dlatego redaktor umieścił wynik na jego najmocniejszej końcowej pozycji.",
"c24-7":"Temat zdania nawiązywał do poprzedniego akapitu i ułatwiał czytelnikowi śledzenie zmiany perspektywy.",
"c24-8":"Nominalizacja „przeprowadzenie analizy” niepotrzebnie ukrywała wykonawcę i osłabiała dynamikę opisu.",
"c24-9":"Aby rozluźnić składnię, redaktorka podzieliła wielokrotnie złożone zdanie na dwie logiczne sekwencje.",
"c24-10":"Można usunąć redundancję, wykreślając powtórzoną definicję bez utraty argumentu ani potrzebnego kontekstu.",
"c24-11":"Redaktor musiał ujednolicić rejestr, bo formalną analizę przerywały przypadkowe potoczne komentarze.",
"c24-12":"W podsumowaniu warto wyeksponować wniosek, zamiast ponownie szczegółowo opisywać wszystkie etapy badania.",
"c24-13":"Trzeba było przestawić akapit o ograniczeniach przed rekomendację, aby czytelnik właściwie ocenił jej zakres.",
"c24-14":"Dobra korekta potrafi zachować głos autora, usuwając niejasność bez wygładzania celowej ironii.",
"c24-15":"Redaktorka umiała uzasadnić ingerencję konkretnym problemem logiki, rytmu lub oczekiwaniami docelowego odbiorcy.",
}
EXPLANATIONS={
0:"Redakcja merytoryczna sprawdza prawdziwość, logikę i kompletność treści; może wymagać nowych danych, korekty wniosku albo zmiany struktury argumentu.",
1:"Redakcja stylistyczna poprawia jasność, rejestr i rytm wypowiedzi, zachowując jej sens oraz rozpoznawalny głos autora.",
2:"Spójność globalna opisuje związki między częściami całego tekstu: każda sekcja powinna wspierać główny cel i wynikać z poprzedniej.",
3:"Tok wywodu to kolejność tez, przesłanek i przykładów; czytelnik powinien móc odtworzyć drogę od pytania do konkluzji.",
4:"Hierarchia informacji odróżnia treści kluczowe od wspierających i decyduje, co pojawia się wcześniej, zostaje rozwinięte lub tylko zasygnalizowane.",
5:"Remat wnosi nową lub najważniejszą informację o temacie zdania; jego pozycja pomaga sterować akcentem i płynnością tekstu.",
6:"Temat zdania wskazuje punkt wyjścia znany z kontekstu, dzięki czemu odbiorca rozumie, czego dotyczy następująca nowa informacja.",
7:"Nominalizacja zamienia czynność w rzeczownik; bywa użyteczna w stylu specjalistycznym, ale jej nadmiar ukrywa wykonawcę i obciąża składnię.",
8:"Rozluźnić składnię znaczy zmniejszyć przeciążenie zdania przez podział, zmianę szyku lub zastąpienie nominalizacji czasownikiem bez spłycania sensu.",
9:"Usunąć redundancję to wykreślić treść powtarzającą już przekazaną informację, o ile powtórzenie nie pełni świadomej funkcji retorycznej.",
}
def forwards(apps,schema_editor):
 F=apps.get_model("learning","Flashcard");Q=apps.get_model("learning","Question")
 for k,v in EXAMPLES.items():F.objects.filter(id=k).update(example=v)
 for p,v in EXPLANATIONS.items():Q.objects.filter(lesson_id="c24-quiz",position=p).update(explanation=v)
class Migration(migrations.Migration):
 dependencies=[("learning","0079_improve_c2_critical_polemics_editorial")]
 operations=[migrations.RunPython(forwards,migrations.RunPython.noop)]
