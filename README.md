# Python template for bots

## Tech stack

- **Python 3.13 & higher**
- Aiogram 3.x
- SQLAlchemy & Alembic
- PostgreSQL
- Pydantic

Install & Run using [UV](https://docs.astral.sh/uv/getting-started/installation/)

```bash
uv venv
source .venv/Scripts/activate
uv sync
```

## Build

1. Create .env file & fill it with your data shown in .env.sample
2. Run database & bot `docker compose up -d --build`
    - Use `http://localhost:8080` for adminer. **Note:** use `db` as server
    - To remove all data use `docker compose down -v`, it will delete volumes


## Structure

```bash
assets /            # Folder for assets
bot /
    filters /
        role.py     # Role filter
    middlewares /   # Bot middlewares
        sessions.py # Middleware for database sessions
    handlers /      # All bot routes
    keyboards /     # All bot keyboards
    states /        # States for FSM
database /
    repositories /   # CRUD operations
    models /    # SQLAlchemy models (don't forget to import them in __init__.py)
    schemas /   # Schemas for CRUD operations
    exceptions.py   # Custom database exceptions
    main.py     # Initialization script
alembic/        # Migration history and env.py config
config.py   # Configuration file, takes data from .env
main.py     # Main startup file
```
