from django.db import migrations


EXPLANATIONS = {
    "b2prof-grammar": {
        0: "Zwrot „zwracam się z prośbą o” łagodzi żądanie i zachowuje formalny rejestr korespondencji.",
        1: "„Omówienie” jest rzeczownikiem odczasownikowym, który nazywa proces omawiania planu bez wskazywania wykonawcy.",
        2: "Forma „ustalono” bezosobowo przedstawia podjętą decyzję, skupiając uwagę odbiorcy na jej treści.",
        3: "Czasownik „prosić” łączy się z przyimkiem „o”, dlatego mówimy „proszę o potwierdzenie”.",
        4: "Konstrukcja „w nawiązaniu do” wymaga dopełniacza i formalnie odsyła do wcześniejszego spotkania.",
        5: "Bezosobowe „ustalono” oraz strona bierna „zostanie przesunięte” podkreślają decyzję, nie jej autora.",
    },
    "b2prof-quiz": {
        0: "„Porządek obrad” oznacza rosyjską „повестку встречи”, czyli listę kwestii zaplanowanych do omówienia.",
        1: "Pytanie „Czy mogę zabrać głos?” uprzejmie prosi o możliwość wypowiedzi i respektuje kolejność rozmówców.",
        2: "Po spotkaniu wysyła się podsumowanie, aby utrwalić decyzje, terminy oraz dalsze zadania uczestników.",
        3: "Formuła „uprzejmie przypominam” przekazuje informację o terminie bez rozkazującego lub agresywnego tonu.",
        4: "„Wdrożenie” jest nominalizacją czasownika „wdrożyć”, ponieważ rzeczownik nazywa proces wprowadzania rozwiązania.",
        5: "Osoby odpowiedzialne i terminy wskazują, kto oraz kiedy ma wykonać uzgodnione zadania.",
        6: "Rzeczownik „przesłanie” wymaga dopełniacza, dlatego poprawną formą jest „przesłanie załącznika”.",
        7: "„Zgłosić zastrzeżenie” znaczy przedstawić uzasadnioną wątpliwość lub sprzeciw wobec proponowanego rozwiązania.",
        8: "Zwrot „pozostaję do dyspozycji” jest neutralnym, profesjonalnym zakończeniem oferującym dalszą pomoc odbiorcy.",
        9: "Bezosobowe „uzgodniono” wysuwa osiągnięte porozumienie na pierwszy plan zamiast wskazywać konkretnych autorów.",
    },
    "b2prof-reading-check": {
        0: "Przed spotkaniem uczestnicy otrzymali porządek obrad, projekt harmonogramu oraz pytania wymagające decyzji.",
        1: "Dział sprzedaży obawiał się, że pracownicy nie zdążą przejść szkolenia przed planowanym terminem.",
        2: "Zespół rozwiązał problem przez podział wdrożenia na dwa etapy, osiągając praktyczny kompromis.",
        3: "Każdemu zadaniu przypisano termin realizacji i osobę odpowiedzialną, aby plan był wykonalny.",
        4: "Formy bezosobowe zastosowano, by protokół podkreślał uzgodnione rezultaty zamiast przebiegu indywidualnych wypowiedzi.",
        5: "Maja poprosiła uczestników o przesłanie uwag do podsumowania najpóźniej do środy.",
    },
    "b2tech-grammar": {
        0: "Zaimek „które” ma rodzaj nijaki i zgadza się z rzeczownikiem „urządzenie” w mianowniku.",
        1: "Strona bierna wymaga imiesłowu „przetwarzane”, który zgadza się z liczbą mnogą rzeczownika „dane”.",
        2: "Konstrukcja „bada się” bezosobowo opisuje proces badawczy, gdy wykonawca nie jest istotny.",
        3: "Forma „zaobserwowano” na „-no” informuje o wyniku obserwacji bez nazywania konkretnego badacza.",
        4: "Definicję tworzy konstrukcja „to zbiór”, a imiesłów „wykorzystywany” zgadza się z rzeczownikiem „zbiór”.",
        5: "Wyrażenie „na podstawie” rządzi dopełniaczem „wyników”, a „opracowano” bezosobowo opisuje rezultat.",
    },
    "b2tech-quiz": {
        0: "W badaniu „próbka” oznacza wybrany materiał albo grupę obserwacji poddawaną analizie.",
        1: "Hipotezę należy sprawdzić za pomocą danych, ponieważ samo założenie nie stanowi jeszcze wyniku.",
        2: "Zdanie definiuje czujnik przez wskazanie jego klasy, czyli urządzenia, oraz wyróżniającej funkcji.",
        3: "Strona bierna „zostały zweryfikowane” wymaga imiesłowu zgodnego z rzeczownikiem „dane” w liczbie mnogiej.",
        4: "Powtórzenie badania na większej próbce zwiększa wiarygodność, ponieważ ogranicza wpływ przypadkowych wyników.",
        5: "Bezosobowe „testuje się” opisuje regularną czynność laboratoryjną bez wskazywania konkretnego wykonawcy.",
        6: "Czasownik „wykrywać” naturalnie łączy się z rzeczownikiem „wzorce” i opisuje działanie algorytmu.",
        7: "Opis ograniczeń wyznacza granice wniosku i zapobiega nadmiernemu uogólnianiu rezultatów badania.",
        8: "Przyimek złożony „na podstawie” wymaga dopełniacza, dlatego poprawna forma brzmi „wyników”.",
        9: "Strona bierna wysuwa rozwiązanie i rezultat opracowania przed osobę wykonującą tę czynność.",
    },
    "b2tech-reading-check": {
        0: "Czujnik mierzy wilgotność gleby, a zebrane dane przekazuje programowi sterującemu podlewaniem.",
        1: "System uruchamia podlewanie dopiero po wykryciu dłuższego niedoboru wody w wybranej części ogrodu.",
        2: "Badanie przeprowadzono w sześciu miejskich ogrodach, porównując zużycie wody przez dwa miesiące.",
        3: "Średni wynik wskazywał osiemnaście procent oszczędności wody w badanych lokalizacjach.",
        4: "Autorzy wskazali niewielką próbkę oraz prowadzenie badania wyłącznie latem jako jego ograniczenia.",
        5: "Jasne objaśnienie technologii kolejno przedstawia definicję, proces, wyniki oraz granice wyciąganego wniosku.",
    },
}


def improve_explanations(apps, schema_editor):
    Question = apps.get_model("learning", "Question")
    for lesson_id, explanations in EXPLANATIONS.items():
        for position, explanation in explanations.items():
            Question.objects.filter(lesson_id=lesson_id, position=position).update(
                explanation=explanation
            )


class Migration(migrations.Migration):
    dependencies = [("learning", "0106_improve_b2_academic_final_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
