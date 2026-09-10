update public.questions
set prompt = 'Widzę świeży ___ na półce.',
    options = '["chleb", "chleba", "chlebem"]'::jsonb,
    correct = 0
where lesson_id = 'food-grammar'
  and position = 2;
