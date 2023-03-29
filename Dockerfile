FROM python:latest

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential libpq-dev gettext libmagic-dev libjpeg-dev zlib1g-dev

RUN pip install poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock /app/
RUN poetry install --no-root --no-dev

COPY ./app/ /app/
RUN python manage.py collectstatic --no-input
RUN python manage.py migrate

CMD ["gunicorn", "core.wsgi:application", "-b", "0.0.0.0:8000"]

EXPOSE 8000
