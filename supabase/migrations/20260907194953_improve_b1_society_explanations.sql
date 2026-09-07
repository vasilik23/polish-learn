update public.questions as q
set explanation = values_to_apply.explanation
from (
  values
    ('b1soc-grammar', 0, '„Ponieważ” wprowadza przyczynę: autor popiera projekt dlatego, że ułatwi on życie starszym mieszkańcom.'),
    ('b1soc-grammar', 1, '„Chociaż” sygnalizuje ustępstwo: koszt projektu nie przekreśla jego możliwych długoterminowych korzyści.'),
    ('b1soc-grammar', 2, '„Więc” wprowadza skutek braku bezpiecznych przejść: mieszkańcy zwracają się z prośbą o zmiany.'),
    ('b1soc-grammar', 3, 'Po wyrażeniu opinii podajemy uzasadnienie: nawet niewielkie działanie może przynieść zauważalny efekt.'),
    ('b1soc-grammar', 4, 'Zdanie z „chociaż” zestawia różne opinie z możliwością osiągnięcia wspólnego rozwiązania.'),
    ('b1soc-quiz', 2, '„Jednak” łączy zalety projektu z przeciwnym argumentem dotyczącym jego wysokiego kosztu.'),
    ('b1soc-quiz', 3, '„Dlatego” wprowadza propozycję parku jako logiczny skutek rozpoznanego braku zieleni.'),
    ('b1soc-reading-check', 2, 'Maja protokołowała argumenty obu stron, dzięki czemu żaden ważny głos nie został pominięty.'),
    ('b1soc-reading-check', 3, 'Kompromis polegał na podziale przestrzeni między plac zabaw a spokojną strefę zieleni.'),
    ('b1soc-reading-check', 4, 'Wspólny projekt zbliżył sąsiadów, ponieważ razem szukali rozwiązania odpowiadającego różnym potrzebom.')
) as values_to_apply(lesson_id, position, explanation)
where q.lesson_id = values_to_apply.lesson_id
  and q.position = values_to_apply.position;
