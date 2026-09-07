from django.db import migrations
E={0:'Wprowadzenie jasno nazywa temat i cel, dzięki czemu odbiorca rozumie kierunek całej wypowiedzi.',3:'Stałe połączenie „odnieść się do” wymaga dopełniacza: odnosimy się do opinii rozmówcy.',5:'„Następnie” porządkuje drugi etap wypowiedzi między początkiem argumentacji a końcowym wnioskiem.',6:'Konkretny przykład wzmacnia opinię, ponieważ pokazuje, jak ogólne twierdzenie działa w rzeczywistej sytuacji.',7:'Samoocena obejmuje poprawienie błędów, ocenę struktury i upewnienie się, że odpowiedź realizuje cel.',8:'Po przyimku „do” używamy dopełniacza: styl dostosowujemy do potrzeb konkretnego odbiorcy.'}
def f(apps,schema_editor):
 Q=apps.get_model('learning','Question')
 for p,e in E.items():Q.objects.filter(lesson_id='b1final-quiz',position=p).update(explanation=e)
class Migration(migrations.Migration):
 dependencies=[('learning','0085_improve_b1_ecology_explanations')]
 operations=[migrations.RunPython(f,migrations.RunPython.noop)]
