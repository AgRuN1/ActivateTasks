FROM python:3.13-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install --no-compile --upgrade pip \
 && pip install --no-compile poetry
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction