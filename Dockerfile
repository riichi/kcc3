FROM python:3.12-slim-bookworm

RUN mkdir -p /app/web
WORKDIR /app/web

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y netcat-openbsd zlib1g-dev libjpeg-dev gcc

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV MEDIA_ROOT /app/media
ENV STATIC_ROOT /app/static

EXPOSE 8000
ENTRYPOINT ["/app/web/entrypoint.sh"]
CMD ["gunicorn", "kcc3.wsgi:application", "--bind", "0.0.0.0:8000"]
