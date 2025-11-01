FROM python:3.14-slim-bookworm

RUN mkdir -p /app/web
WORKDIR /app/web

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y netcat-openbsd zlib1g-dev libjpeg-dev gcc libimage-exiftool-perl

RUN pip install --upgrade pip
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
RUN pip install poetry==1.7.0 \
  && poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . .

ENV MEDIA_ROOT /app/media
ENV STATIC_ROOT /app/static

EXPOSE 8000
ENTRYPOINT ["/app/web/entrypoint.sh"]
CMD ["gunicorn", "kcc3.wsgi:application", "--bind", "0.0.0.0:8000"]
