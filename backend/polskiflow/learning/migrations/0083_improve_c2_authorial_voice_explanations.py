from django.db import migrations
E={
0:"Głos autorski to rozpoznawalny sposób wyboru słów, perspektywy i kompozycji; nie sprowadza się do pojedynczego ozdobnego chwytu.",
1:"Ton wypowiedzi wyraża stosunek autora do tematu i odbiorcy poprzez rejestr, modalność, rytm oraz stopień emocjonalnego dystansu.",
2:"Rytm prozy powstaje z długości zdań, akcentów, powtórzeń i pauz; kieruje tempem lektury oraz siłą kolejnych argumentów.",
3:"Kadencja zdania opisuje jego końcowy przebieg intonacyjny i składniowy, który może domknąć myśl albo świadomie pozostawić napięcie.",
4:"Fraza rozpoznawalna ujawnia indywidualny styl przez charakterystyczny szyk, obrazowanie lub rytm, lecz powtarzana mechanicznie staje się manierą.",
5:"Dystans narracyjny określa bliskość narratora wobec postaci i zdarzeń; jego zmiana wpływa na empatię, wiedzę oraz wiarygodność opowieści.",
6:"Ironia dyskretna tworzy różnicę między sensem dosłownym a sugerowaną oceną, pozostawiając odbiorcy wystarczające, lecz nie nachalne sygnały.",
7:"Zagęszczenie składni skupia wiele relacji w jednym zdaniu; może wzmacniać intensywność, ale bez kontroli utrudnia rozpoznanie hierarchii myśli.",
8:"Modulować tempo znaczy świadomie przyspieszać lub spowalniać narrację długością zdań, szczegółem, dialogiem i rozmieszczeniem pauz.",
9:"Przełamać regularność warto w punkcie znaczeniowego zwrotu: nagła zmiana rytmu wtedy akcentuje sens, zamiast wyglądać na przypadkową niezręczność.",
}
def f(apps,schema_editor):
 Q=apps.get_model('learning','Question')
 for p,e in E.items():Q.objects.filter(lesson_id='c29-quiz',position=p).update(explanation=e)
class Migration(migrations.Migration):
 dependencies=[('learning','0082_improve_c2_cultural_interpretation_explanations')]
 operations=[migrations.RunPython(f,migrations.RunPython.noop)]
