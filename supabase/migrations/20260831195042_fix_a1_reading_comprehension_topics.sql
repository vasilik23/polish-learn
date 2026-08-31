-- Move two legacy readings into the canonical A1 topic that already owns
-- their unique comprehension quizzes.
update public.reading_texts
set topic_id = 'introductions'
where id in ('poranek-anny', 'zakupy-na-targu')
  and topic_id is distinct from 'introductions';
