FROM python:3.7-slim

# Ensure console output looks familiar
ENV PYTHONUNBUFFERED 1
# Don't write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install --no-cache --upgrade pip

COPY ./requirements /requirements
RUN pip install --no-cache -r requirements/local.txt

COPY . /app/
WORKDIR /app

ENV DATABASE_URL postgres://errors_db@db:5432/errors_db
ENV DJANGO_HASHID_SALT 'sample hashid salt'
ENV DJANGO_SECRET_KEY 'sample secret key'
ENV DJANGO_SETTINGS_MODULE config.settings.production

RUN python manage.py collectstatic --noinput

