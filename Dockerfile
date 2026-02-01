FROM python:3.14-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN mkdir -p /app/web
WORKDIR /app/web

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y netcat-openbsd zlib1g-dev libjpeg-dev gcc libimage-exiftool-perl

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev

COPY . .

ENV MEDIA_ROOT=/app/media
ENV STATIC_ROOT=/app/static
ENV PATH="/app/web/.venv/bin:$PATH"

EXPOSE 8000
ENTRYPOINT ["/app/web/entrypoint.sh"]
CMD ["uv", "run", "granian", "--interface", "wsgi", "kcc3.wsgi:application", "--host", "0.0.0.0", "--port", "8000"]
