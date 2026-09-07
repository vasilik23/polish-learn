update public.questions as q
set explanation = values_to_apply.explanation
from (
  values
    ('b1region-grammar', 0, 'Przyimek „według” łączy się z dopełniaczem, dlatego poprawną formą jest „według przewodnika”.'),
    ('b1region-grammar', 2, '„Natomiast” podkreśla kontrast między płaską północą regionu a górskim krajobrazem południa.'),
    ('b1region-quiz', 0, 'Województwo jest największą jednostką podziału administracyjnego Polski i obejmuje wiele powiatów oraz gmin.'),
    ('b1region-quiz', 2, 'Przyimek „według” wymaga dopełniacza, więc rzeczownik „kronika” przyjmuje formę „kroniki”.'),
    ('b1region-quiz', 3, 'Konstrukcja „zarówno…, jak i…” łączy równorzędne elementy: w tym zdaniu góry oraz jeziora.'),
    ('b1region-quiz', 5, '„Natomiast” zestawia dwa odmienne obrazy: ruchliwe centrum oraz spokojne wsie.'),
    ('b1region-quiz', 8, 'Wyrażenie „w przeciwieństwie do” ma stałe połączenie z przyimkiem „do” i dopełniaczem.'),
    ('b1region-reading-check', 0, 'Kasia zaplanowała wyjazd w Beskid Niski, ponieważ chciała poznać mniej oczywisty region Polski.'),
    ('b1region-reading-check', 2, 'Muzeum prezentowało lokalne dziedzictwo, czyli historię, tradycje i codzienne życie mieszkańców regionu.'),
    ('b1region-reading-check', 3, 'Kasia odwiedziła rodzinną pracownię, gdzie spotkała rzemieślników pielęgnujących lokalną tradycję.')
) as values_to_apply(lesson_id, position, explanation)
where q.lesson_id = values_to_apply.lesson_id
  and q.position = values_to_apply.position;
