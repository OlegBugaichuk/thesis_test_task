# Тестовое задание, компания Тезис

## Запуск проекта с докером

- Создаем образ контейнера

```bash
docker build -t thesis .
```

- Запускаем контейнер

```bash
docker run -p 8000:8000 thesis
```

- Переходим на [localhost:8000/api/docs/](localhost:8000/api/docs/) или [127.0.0.1:8000/api/docs/](127.0.0.1:8000/api/docs/)

---
## Запуск проекта без докера

- ставим [poetry](https://python-poetry.org/docs/#installation) если отсутсвует

- устанавливаем зависимости 
```bash
poetry install --no-root
```

- активируем виртуальное окружение
```bash
poetry shell
```

- накатываем миграции (используется SQLite, для простоты) 
```bash
cd app
python manage.py migrate
```

- запускаем сервер 

```bash
# либо через manage.py
python manage.py runserver
```

```bash
# либо gunicorn
gunicorn core.wsgi:application
```

---
## Запуск тестов

в каталоге app

```bash
pytest
```

---
## Дополнительно

Swagger доступен по /api/docs/

Перед запуском сервера желательно создать юзера, для доступа к employees

```bash
python manage.py createsuperuser
```