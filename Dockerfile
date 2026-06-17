FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS base

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/app/.venv \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

RUN useradd \
    --create-home \
    --uid 1000 \
    appuser

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync \
    --frozen \
    --no-install-project \
    --no-dev

RUN chown -R appuser:appuser /app


# --- Stage 1: bot ---
FROM base AS bot

USER appuser

COPY --chown=appuser:appuser bot ./bot
COPY --chown=appuser:appuser database ./database
COPY --chown=appuser:appuser assets ./assets
COPY --chown=appuser:appuser main.py config.py ./

CMD ["python", "main.py"]


# --- Stage 2: migrations ---
FROM base AS migrations

USER appuser

COPY --chown=appuser:appuser alembic ./alembic
COPY --chown=appuser:appuser database ./database
COPY --chown=appuser:appuser alembic.ini config.py ./

CMD ["alembic", "upgrade", "head"]
