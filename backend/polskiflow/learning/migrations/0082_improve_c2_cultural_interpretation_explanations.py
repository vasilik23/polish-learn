from django.db import migrations
E={
0:"Kontekst kulturowy obejmuje wiedzę, normy i wydarzenia potrzebne do odczytania sensu, którego sam tekst nie wyjaśnia bezpośrednio.",
1:"Aluzja literacka pośrednio przywołuje rozpoznawalny utwór lub motyw; jej znaczenie powstaje przez porównanie nowego fragmentu z pamiętanym pierwowzorem.",
2:"Intertekstualność opisuje relacje tekstu z innymi wypowiedziami poprzez cytat, stylizację, polemikę lub przekształcenie wcześniejszego wzorca.",
3:"Symbolika nadaje elementowi znaczenie wykraczające poza jego funkcję dosłowną, ale interpretacja wymaga powtarzalnych sygnałów i kontekstu dzieła.",
4:"Konwencja epoki określa historyczne oczekiwania wobec gatunku, bohatera i stylu; jej znajomość pozwala rozpoznać świadome naruszenie normy.",
5:"Strategia narracyjna to sposób dozowania wiedzy, wyboru perspektywy i porządkowania zdarzeń, który kieruje zaufaniem oraz oceną czytelnika.",
6:"Perspektywa odbiorcy uwzględnia jego doświadczenie i kompetencje; różni czytelnicy mogą uruchamiać inne skojarzenia bez dowolności interpretacyjnej.",
7:"Konkurencyjne odczytanie proponuje inne, oparte na tekście wyjaśnienie tych samych sygnałów i powinno wskazywać własne mocne oraz słabe miejsca.",
8:"Osadzić w kontekście znaczy połączyć fragment z warunkami historycznymi, społecznymi lub gatunkowymi, unikając redukowania dzieła do tła.",
9:"Uruchomić skojarzenie to wywołać u odbiorcy pamięć motywu lub doświadczenia, które współtworzy sens bez jego dosłownego nazwania.",
}
def f(apps,schema_editor):
 Q=apps.get_model('learning','Question')
 for p,e in E.items():Q.objects.filter(lesson_id='c26-quiz',position=p).update(explanation=e)
class Migration(migrations.Migration):
 dependencies=[('learning','0081_improve_c2_cross_genre_explanations')]
 operations=[migrations.RunPython(f,migrations.RunPython.noop)]
