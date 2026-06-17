# Python template for bots

Template for Telegram bots with modern Python tooling.

## Tech stack

- **Python 3.13+**
- **Aiogram 3.x**
- **SQLAlchemy**
- **Alembic**
- **PostgreSQL**
- **Pydantic**
- **uv** — dependency management
- **Ruff** — linting & formatting
- **pre-commit** — git hooks
- **Docker / Docker Compose**

---

## Development setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

Create virtual environment and install dependencies:

```bash
uv sync
```

Activate environment:
Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```
---

## Environment

Create `.env` file:

```bash
cp .env.sample .env
```
Fill required variables.

---

## Code quality

This project uses:

- ruff check for linting
- ruff format for formatting
- pre-commit hooks before commits

Install git hooks:

```bash
uv run pre-commit install
```

Run hooks manually:
```bash
uv run pre-commit run --all-files
```

Run Ruff manually:
```
uv run ruff check .
uv run ruff format .
```

---

## Run with Docker

Build and start services:

```bash
# Production
docker compose up -d --build

# Development
docker compose --profile dev up -d --build
```

Services:

- Bot
- PostgreSQL
- Alembic migrations
- Adminer **(Development)**

Adminer: `http://localhost:8080`

Database server inside Docker network: `db`

To stop and remove containers:

```bash
# Production
docker compose down

# Development
docker compose --profile dev down
```

---

## Database migrations
Migrations are executed automatically before bot startup.

Manual migration:
```bash
docker compose run --rm migrations
```

Create new migration:
```bash
uv run alembic revision --autogenerate -m "migration name"
```

---

## Project structure

```
assets /                  # Static assets

bot /
    filters /             # Aiogram filters
    middlewares /         # Bot middlewares
        sessions.py       # Database session middleware
    handlers /            # Bot routes
    keyboards /           # Reply/inline keyboards
    states /              # FSM states
    services /            # Services for logic

database /
    queries /             # CRUD operations
    models /              # SQLAlchemy models
    main.py               # Database initialization

alembic /
    versions /            # Migration history
    env.py                # Alembic configuration

config.py                 # Application configuration from .env
main.py                   # Application entry point

pyproject.toml            # Dependencies and tooling config
uv.lock                   # Locked dependencies
docker-compose.yml        # Local infrastructure
Dockerfile                # Container build
```
