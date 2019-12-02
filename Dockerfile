FROM python:3.7-slim

#
# Env Setup
#
ENV PYTHONUNBUFFERED 1 
# Sample values only
ENV DATABASE_URL postgres://errors_db@db:5432/errors_db
ENV DJANGO_HASHID_SALT 'sample hashid salt'
ENV DJANGO_SECRET_KEY 'sample secret key'
ENV DJANGO_SETTINGS_MODULE config.settings.production
# Don't write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install --no-cache --upgrade pip

COPY ./requirements /requirements
RUN if [ "${BUILD_ENV}" = "production" ]; then pip install --no-cache-dir -r requirements/production.txt; fi 
RUN if [ "${BUILD_ENV}" = "development" ]; then pip install --no-cache-dir -r requirements/local.txt; fi


COPY . /app/
WORKDIR /app


RUN python manage.py collectstatic --noinput

# CMD python ./manage.py runserver 0.0.0.0:8000
CMD gunicorn errors_db.wsgi:application
