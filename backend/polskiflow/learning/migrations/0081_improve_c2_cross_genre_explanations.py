from django.db import migrations
E={
0:"Konwencja gatunkowa określa oczekiwaną kompozycję, ton i relację z odbiorcą; transformacja może je zmienić, lecz powinna zachować fakty.",
1:"Dominanta tekstu jest jego nadrzędną funkcją, na przykład informowaniem lub perswazją; jej rozpoznanie kieruje decyzjami podczas zmiany gatunku.",
2:"Kompresja treści skraca przekaz przez hierarchizację informacji, a nie mechaniczne usuwanie zdań; kluczowe warunki i źródła muszą pozostać.",
3:"Eksplicytacja ujawnia informację wcześniej pozostawioną w domyśle, gdy nowy odbiorca nie dysponuje potrzebnym kontekstem kulturowym lub specjalistycznym.",
4:"Zmiana rejestru dostosowuje słownictwo i składnię do sytuacji, ale nie powinna zwiększać ani zmniejszać pewności pierwotnego twierdzenia.",
5:"Rama interpretacyjna podpowiada, które związki między faktami uznać za centralne; jej zmiana może przekształcić wydźwięk mimo zachowania danych.",
6:"Adresat docelowy wyznacza zakres objaśnień, terminologię i ton; redaktor nie może zakładać wiedzy właściwej zupełnie innej grupie.",
7:"Hierarchia faktów oddziela informacje konieczne od szczegółów wspierających, dzięki czemu skrót zachowuje sens i proporcje oryginału.",
8:"Przeformułować przekaz znaczy zbudować go ponownie dla innego gatunku lub odbiorcy, nie zaś tylko zastąpić pojedyncze słowa synonimami.",
9:"Zachować zastrzeżenie to przenieść do nowej wersji ograniczenie zakresu lub pewności; jego pominięcie zniekształca siłę wniosku.",
}
def f(apps,schema_editor):
 Q=apps.get_model('learning','Question')
 for p,e in E.items():Q.objects.filter(lesson_id='c25-quiz',position=p).update(explanation=e)
class Migration(migrations.Migration):
 dependencies=[('learning','0080_improve_c2_professional_editing_editorial')]
 operations=[migrations.RunPython(f,migrations.RunPython.noop)]
