create table public.reading_texts (
  id text primary key,
  topic_id text references public.topics(id) on delete set null,
  title text not null,
  description text not null,
  level text not null default 'A1' check (level in ('A1', 'A2', 'B1', 'B2', 'C1', 'C2')),
  minutes smallint not null default 5 check (minutes > 0),
  emoji text not null default '',
  paragraphs jsonb not null default '[]'::jsonb check (jsonb_typeof(paragraphs) = 'array'),
  glossary jsonb not null default '{}'::jsonb check (jsonb_typeof(glossary) = 'object'),
  position smallint not null default 0 check (position >= 0),
  is_active boolean not null default true
);

create index reading_texts_topic_position_idx
  on public.reading_texts(topic_id, position);

create table public.personal_words (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  word text not null check (char_length(word) between 1 and 160),
  translation text not null check (char_length(translation) between 1 and 240),
  context text not null default '' check (char_length(context) <= 500),
  source_text_id text references public.reading_texts(id) on delete set null,
  created_at timestamptz not null default now(),
  constraint unique_personal_word unique (user_id, word)
);

create index personal_words_user_created_idx
  on public.personal_words(user_id, created_at desc);

alter table public.reading_texts enable row level security;
alter table public.personal_words enable row level security;

revoke all on table public.reading_texts from anon, authenticated;
revoke all on table public.personal_words from anon, authenticated;
grant select on table public.reading_texts to anon, authenticated;
grant select, insert, update, delete on table public.personal_words to authenticated;

create policy "Active reading texts are public"
  on public.reading_texts for select
  to anon, authenticated
  using (is_active = true);

create policy "Users read their personal words"
  on public.personal_words for select
  to authenticated
  using ((select auth.uid()) = user_id);

create policy "Users add their personal words"
  on public.personal_words for insert
  to authenticated
  with check ((select auth.uid()) = user_id);

create policy "Users update their personal words"
  on public.personal_words for update
  to authenticated
  using ((select auth.uid()) = user_id)
  with check ((select auth.uid()) = user_id);

create policy "Users delete their personal words"
  on public.personal_words for delete
  to authenticated
  using ((select auth.uid()) = user_id);

insert into public.reading_texts
  (id, topic_id, title, description, level, minutes, emoji, paragraphs, glossary, position)
values
  (
    'poranek-anny', 'first-steps', 'Poranek Anny', 'Обычное утро Анны в Варшаве',
    'A1', 4, '☀️',
    '["Anna mieszka w Warszawie. Codziennie rano wstaje o siódmej i otwiera okno. Dzisiaj jest ciepło i świeci słońce.", "Anna robi kawę i przygotowuje śniadanie. Je chleb z serem i słucha radia. Potem bierze plecak i idzie do pracy.", "Po drodze spotyka sąsiada. Mówi: Dzień dobry! Sąsiad uśmiecha się i życzy jej miłego dnia."]'::jsonb,
    '{"mieszka":"живёт","codziennie":"каждый день","rano":"утром","wstaje":"встаёт","otwiera":"открывает","okno":"окно","ciepło":"тепло","świeci":"светит","słońce":"солнце","robi":"делает","przygotowuje":"готовит","śniadanie":"завтрак","chleb":"хлеб","serem":"сыром","słucha":"слушает","potem":"потом","bierze":"берёт","plecak":"рюкзак","idzie":"идёт","pracy":"работа","drodze":"дорога","spotyka":"встречает","sąsiada":"соседа","uśmiecha":"улыбается","życzy":"желает","miłego":"приятного","dnia":"дня"}'::jsonb,
    0
  ),
  (
    'zakupy-na-targu', 'first-steps', 'Zakupy na targu', 'Покупаем овощи на городском рынке',
    'A1', 5, '🍎',
    '["W sobotę Marek idzie na targ. Chce kupić świeże warzywa i owoce. Na targu jest dużo ludzi i kolorowych stoisk.", "Najpierw Marek kupuje pomidory, ogórki i ziemniaki. Pyta sprzedawcę: Ile kosztuje kilogram pomidorów? Cztery złote — odpowiada sprzedawca.", "Na końcu wybiera czerwone jabłka. Płaci dwanaście złotych i wraca do domu z pełną torbą."]'::jsonb,
    '{"sobotę":"субботу","targ":"рынок","chce":"хочет","kupić":"купить","świeże":"свежие","warzywa":"овощи","owoce":"фрукты","dużo":"много","ludzi":"людей","kolorowych":"цветных","stoisk":"прилавков","najpierw":"сначала","kupuje":"покупает","pomidory":"помидоры","ogórki":"огурцы","ziemniaki":"картофель","pyta":"спрашивает","sprzedawcę":"продавца","kosztuje":"стоит","kilogram":"килограмм","cztery":"четыре","złote":"злотых","odpowiada":"отвечает","końcu":"конце","wybiera":"выбирает","czerwone":"красные","jabłka":"яблоки","płaci":"платит","dwanaście":"двенадцать","wraca":"возвращается","pełną":"полной","torbą":"сумкой"}'::jsonb,
    1
  );
