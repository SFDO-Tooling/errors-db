FROM python:3

# Ensure console output looks familiar
ENV PYTHONUNBUFFERED 1
# Don't write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

ENV DATABASE_URL postgres://errors_db@db:5432/errors_db
ENV POSTGRES_USER "postgres"
ENV POSTGRES_PASSWORD ""

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements/local.txt