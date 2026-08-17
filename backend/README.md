# PolskiFlow Python backend

Здесь находятся независимое доменное ядро и постепенно вводимый Django-проект.
До переключения production текущий Next.js-интерфейс продолжает работать.

Запуск тестов из корня репозитория:

```bash
PYTHONPATH=backend python3 -m unittest discover -s backend/tests -v
```

Проверка Django после установки зависимостей:

```bash
cd backend
python manage.py check
python manage.py test
```

Проверенная версия зависимостей закреплена в `requirements.lock`.
