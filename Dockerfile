# --- Stage 0: base ---
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS base

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Create Non-Priveleged user
RUN useradd -m -u 1000 appuser

# Install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev --no-cache

RUN chown -R appuser:appuser /app

USER appuser
ENV PATH="/app/.venv/bin:$PATH"

# --- Stage 1: bot ---
FROM base AS bot
WORKDIR /app
COPY bot ./bot
COPY database ./database
COPY assets ./assets
COPY main.py .
COPY config.py .

CMD ["uv", "run", "main.py"]

# --- Stage 2: migrations ---
FROM base AS migrations
WORKDIR /app
COPY alembic ./alembic
COPY database ./database
COPY alembic.ini .
COPY config.py .
CMD ["uv", "run", "alembic", "upgrade", "head"]
