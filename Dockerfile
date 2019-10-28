FROM python:3.7-slim

# Ensure console output looks familiar
ENV PYTHONUNBUFFERED 1
# Don't write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

ENV DATABASE_URL postgres://errors_db@db:5432/errors_db

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install --no-cache --upgrade pip
RUN pip install --no-cache -r requirements/local.txt