-- Original A2 reading-comprehension activity. Existing public-content RLS and grants apply.
insert into public.lessons
  (id,topic_id,kind,title,plan_title,subtitle,description,minutes,emoji,theory_title,theory_sections,source_metadata,position,is_active)
values
  ('weekend-reading-check','past-weekend','quiz','Czy rozumiesz tekst?','Понимание текста','5 вопросов · A2','Проверь детали рассказа Каси и Павла',5,'📖','','[]','{"origin":"original","created_for":"PolskiFlow","verified_at":"2026-08-28"}',52,true)
on conflict(id) do update set
  topic_id=excluded.topic_id,
  kind=excluded.kind,
  title=excluded.title,
  plan_title=excluded.plan_title,
  subtitle=excluded.subtitle,
  description=excluded.description,
  minutes=excluded.minutes,
  emoji=excluded.emoji,
  theory_title=excluded.theory_title,
  theory_sections=excluded.theory_sections,
  source_metadata=excluded.source_metadata,
  position=excluded.position,
  is_active=excluded.is_active;

delete from public.questions where lesson_id='weekend-reading-check';
insert into public.questions
  (lesson_id,prompt,options,correct,explanation,position)
values
  ('weekend-reading-check','Dokąd Kasia pojechała po pracy?','["Do Krakowa","Do Wrocławia","Do parku"]',1,'В первом абзаце прямо сказано: Kasia pojechała pociągiem do Wrocławia.',0),
  ('weekend-reading-check','Co Kasia i jej koleżanka zrobiły w sobotę?','["Zwiedziły muzeum","Ugotowały obiad","Pojechały na rowerach"]',0,'В субботу подруги посетили музей и увидели рыночную площадь.',1),
  ('weekend-reading-check','Dlaczego Kasia i jej koleżanka dużo spacerowały?','["Bo zgubiły pociąg","Bo było słonecznie","Bo muzeum było zamknięte"]',1,'Союз więc связывает причину и результат: было солнечно, поэтому они много гуляли.',2),
  ('weekend-reading-check','Jak Paweł spędził część weekendu w domu?','["Pracował i sprzątał","Spał cały dzień","Ugotował obiad i obejrzał filmy"]',2,'Текст перечисляет два действия Павла дома: приготовил обед и посмотрел два фильма.',3),
  ('weekend-reading-check','Jak Paweł czuł się w poniedziałek?','["Miał dużo energii","Był bardzo zmęczony","Był chory"]',0,'После отдыха Павел в понедельник чувствовал прилив энергии.',4);

update public.reading_texts
set source_metadata = source_metadata || '{"comprehension_lesson_id":"weekend-reading-check"}'::jsonb
where id='weekend-kasi-i-pawla';
