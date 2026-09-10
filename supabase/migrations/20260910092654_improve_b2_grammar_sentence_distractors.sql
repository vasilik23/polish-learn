update public.questions as q
set options = case q.correct
  when 1 then jsonb_build_array(v.options -> 1, v.options -> 0, v.options -> 2)
  when 2 then jsonb_build_array(v.options -> 1, v.options -> 2, v.options -> 0)
  else v.options
end
from (
  values
    ('b2view-grammar', 5, '["Mimo że rozumiem to zastrzeżenie, nowe dane potwierdzają nasz wniosek.", "Mimo że rozumiem to zastrzeżenie, nowe dane podważają nasz wniosek.", "Chociaż odrzucam to zastrzeżenie, wcześniejsze dane potwierdzają nasz wniosek."]'::jsonb),
    ('b2news-grammar', 5, '["Świadek przekazał, że pociąg zatrzymał się przed stacją.", "Świadek przekazał, że pociąg zatrzyma się przed stacją.", "Świadek zaprzeczył, że pociąg zatrzymał się przed stacją."]'::jsonb),
    ('b2prof-grammar', 5, '["Ustalono, że wdrożenie zostanie przesunięte na przyszły miesiąc.", "Ustalono, że wdrożenie zostanie przyspieszone w przyszłym miesiącu.", "Ustalono, że wdrożenie zostanie przesunięte na bieżący miesiąc."]'::jsonb),
    ('b2tech-grammar', 5, '["Na podstawie wyników opracowano nowe rozwiązanie.", "Na podstawie wyników oceniono dotychczasowe rozwiązanie.", "Mimo uzyskanych wyników odrzucono nowe rozwiązanie."]'::jsonb),
    ('b2economy-grammar', 5, '["Prawdopodobnie ten wariant będzie bardziej opłacalny w porównaniu z poprzednim.", "Z pewnością ten wariant będzie mniej opłacalny w porównaniu z poprzednim.", "Prawdopodobnie ten wariant będzie równie opłacalny jak poprzedni."]'::jsonb),
    ('b2law-grammar', 5, '["W związku z brakiem odpowiedzi składam skargę na bezczynność organu.", "W związku z otrzymaniem odpowiedzi wycofuję skargę na bezczynność organu.", "Z powodu braku odpowiedzi składam wniosek o ponowne rozpatrzenie sprawy."]'::jsonb),
    ('b2psych-grammar', 5, '["Z jego perspektywy mogła okazać więcej zrozumienia.", "Z jego perspektywy nie powinna okazywać większego zrozumienia.", "Z jej perspektywy to on mógł okazać więcej zrozumienia."]'::jsonb),
    ('b2lit-grammar', 5, '["Bohaterka powiedziała, że wróci, ale narrator poddaje jej słowa w wątpliwość.", "Bohaterka powiedziała, że wróci, a narrator potwierdza prawdziwość jej słów.", "Bohaterka powiedziała, że nie wróci, ale narrator poddaje jej słowa w wątpliwość."]'::jsonb),
    ('b2discussion-grammar', 5, '["Podsumowując, zgadzamy się co do celu, ale sposób pozostaje sporny.", "Podsumowując, nie zgadzamy się co do celu, a sposób pozostaje sporny.", "Podsumowując, cel pozostaje sporny, ale akceptujemy proponowany sposób."]'::jsonb),
    ('b2intercultural-grammar', 5, '["Jeśli dobrze rozumiem, milczenie nie oznaczało sprzeciwu.", "Jeśli dobrze rozumiem, milczenie oznaczało wyraźny sprzeciw.", "Jeśli źle rozumiem, milczenie nie oznaczało zgody."]'::jsonb),
    ('b2academic-grammar', 5, '["Na podstawie tej próby nie można sformułować ostatecznego wniosku.", "Na podstawie tej próby można sformułować ostateczny wniosek.", "Na podstawie całej populacji nie można przedstawić wstępnej hipotezy."]'::jsonb),
    ('b2final-grammar', 5, '["Gdybyśmy powtórzyli projekt, wcześniej zebralibyśmy informację zwrotną.", "Gdybyśmy powtórzyli projekt, później zebralibyśmy informację zwrotną.", "Ponieważ powtórzyliśmy projekt, wcześniej zebraliśmy dane finansowe."]'::jsonb)
) as v(lesson_id, position, options)
where q.lesson_id = v.lesson_id
  and q.position = v.position;
