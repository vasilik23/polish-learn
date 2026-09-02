-- Keep the C1 literary-language editorial pass rerunnable and content-only.
update public.flashcards as flashcard
set example = editorial.example
from (values
  ('c17-1', 'Narrator niewiarygodny przemilcza własny udział w wypadku, choć ślady w jego relacji pozwalają czytelnikowi odtworzyć prawdę.'),
  ('c17-2', 'Perspektywa dorosłej bohaterki odsłania, jak pamięć po latach przekształciła znaczenie spotkania opisanego wcześniej oczami dziecka.'),
  ('c17-3', 'Metafora zamarzniętego zegara łączy poczucie winy bohatera z czasem, który pozornie stanął na dworcu.'),
  ('c17-4', 'Porównanie pustego peronu do sceny po spektaklu podkreśla samotność narratora i nieodwracalność wydarzeń.'),
  ('c17-5', 'Rytm zdania gwałtownie przyspiesza dzięki krótkim równoważnikom, gdy w oddali pojawia się światło pociągu.'),
  ('c17-6', 'Elipsa usuwa opis samego zderzenia, dlatego odbiorca musi uzupełnić najważniejsze zdarzenie na podstawie jego skutków.'),
  ('c17-7', 'Niedopowiedzenie w ostatnim akapicie nie rozstrzyga, czy bohater wyznał prawdę, czy ponownie wybrał milczenie.'),
  ('c17-8', 'Ironia dramatyczna powstaje, gdy czytelnik zna treść listu, a bohater nadal ufa osobie, która go zdradziła.'),
  ('c17-9', 'Stylizacja na dawny dziennik obejmuje archaiczne słownictwo, datowane wpisy i powściągliwy sposób wyrażania emocji.'),
  ('c17-10', 'Głos bohatera pozostaje rzeczowy, lecz powracające urwane zdania zdradzają napięcie, którego sam nie nazywa.'),
  ('c17-11', 'Obrazowanie oparte na zimnie, metalu i bladym świetle buduje atmosferę obcości jeszcze przed ujawnieniem konfliktu.'),
  ('c17-12', 'Kontrast między spokojnym opisem krajobrazu a chaotycznym monologiem pokazuje rozpad wewnętrznej równowagi postaci.'),
  ('c17-13', 'Wieloznaczność słowa «powrót» pozwala odczytać finał zarówno jako przyjazd do miasta, jak i odzyskanie pamięci.'),
  ('c17-14', 'Punkt kulminacyjny następuje nie podczas przyjazdu pociągu, lecz wtedy, gdy narrator rozpoznaje własne pismo na kopercie.'),
  ('c17-15', 'Interpretacja motywu zegara wymaga połączenia jego dosłownej obecności z winą, pamięcią i zaburzoną chronologią opowieści.')
) as editorial(id, example)
where flashcard.id = editorial.id;

update public.questions as question
set explanation = editorial.explanation
from (values
  ('c17-grammar', 0, 'Narrator niewiarygodny przedstawia wersję wydarzeń, której nie można przyjąć bez zastrzeżeń; sygnałem bywają sprzeczności, przemilczenia lub ograniczona wiedza.'),
  ('c17-grammar', 1, 'Perspektywa określa punkt widzenia, zakres wiedzy i sposób wartościowania zdarzeń; jej zmiana może całkowicie przekształcić sens tej samej sceny.'),
  ('c17-grammar', 2, 'Metafora przenosi znaczenie między odległymi obszarami bez dosłownego «jak», dzięki czemu konkretny obraz może wyrażać stan psychiczny lub abstrakcyjną ideę.'),
  ('c17-grammar', 3, 'Porównanie jawnie zestawia dwa zjawiska, zwykle przez «jak», «niczym» lub «niby», i uwydatnia wybraną wspólną cechę.'),
  ('c17-grammar', 4, 'Rytm zdania wynika między innymi z długości fraz, interpunkcji i powtórzeń; autor może nim przyspieszać akcję albo zatrzymywać uwagę czytelnika.'),
  ('c17-grammar', 5, 'Elipsa pomija składnik możliwy do odtworzenia z kontekstu; w narracji może też świadomie pozostawić lukę w przebiegu zdarzeń.'),
  ('c17-quiz', 0, 'Niewiarygodność nie oznacza po prostu kłamstwa: relację narratora podważają także ograniczona pamięć, interes własny i rozbieżności widoczne dla odbiorcy.'),
  ('c17-quiz', 1, 'Perspektywa porządkuje to, kto postrzega wydarzenia, co o nich wie i jak je ocenia; nie jest synonimem samego tematu utworu.'),
  ('c17-quiz', 2, 'Metafora tworzy nowe znaczenie przez niedosłowne utożsamienie, podczas gdy porównanie zachowuje wyraźne rozdzielenie zestawianych elementów.'),
  ('c17-quiz', 3, 'Porównanie wskazuje podobieństwo za pomocą jawnego łącznika; analiza powinna nazwać również cechę, którą takie zestawienie eksponuje.'),
  ('c17-quiz', 4, 'Rytm zdania jest słyszalnym układem akcentów, pauz i długości członów, który wpływa na tempo oraz emocjonalny odbiór fragmentu.'),
  ('c17-quiz', 5, 'Elipsę rozpoznajemy po braku elementu, który odbiorca potrafi dopowiedzieć; luka może działać zarówno gramatycznie, jak i kompozycyjnie.'),
  ('c17-quiz', 6, 'Niedopowiedzenie celowo nie zamyka sensu i zaprasza do interpretacji, zamiast jedynie usuwać zbędne słowo ze zdania.'),
  ('c17-quiz', 7, 'Ironia dramatyczna opiera się na przewadze wiedzy odbiorcy nad bohaterem, przez co jego słowa zyskują sens, którego postać sama nie dostrzega.'),
  ('c17-quiz', 8, 'Stylizacja konsekwentnie naśladuje cechy innej epoki, środowiska lub gatunku i obejmuje więcej niż pojedynczy archaizm czy potoczne słowo.'),
  ('c17-quiz', 9, 'Głos bohatera tworzą jego słownictwo, składnia, rytm i sposób oceniania; pozwala odróżnić postać od narratora oraz innych mówiących.'),
  ('c17-reading-check', 0, 'Wiarygodność osłabia rozbieżność między pewnymi deklaracjami narratora a szerszą wiedzą czytelnika, który potrafi dostrzec przemilczany udział bohatera.'),
  ('c17-reading-check', 1, 'Pierwszy akapit wprowadza pusty dworzec oraz stopniowe ujawnianie związku narratora z wydarzeniami, ustanawiając problem jego wiarygodności.'),
  ('c17-reading-check', 2, 'Drugi akapit przeciwstawia krótkie zdania przyspieszające oczekiwanie rozbudowanym metaforom, które zatrzymują narrację przy wspomnieniach.'),
  ('c17-reading-check', 3, 'Trzeci akapit przedstawia zegar jako możliwy znak winy, ale celowo nie zamyka tej wieloznacznej figury w jednej obowiązującej interpretacji.'),
  ('c17-reading-check', 4, 'Czwarty akapit buduje ironię dramatyczną: odbiorca wie więcej od bohatera i dlatego inaczej ocenia jego stanowcze zapewnienia.'),
  ('c17-reading-check', 5, 'Finał pomija jednoznaczny opis kulminacji, a niedopowiedzenie wymaga od czytelnika połączenia perspektyw i samodzielnej oceny narratora.')
) as editorial(lesson_id, position, explanation)
where question.lesson_id = editorial.lesson_id
  and question.position = editorial.position;
