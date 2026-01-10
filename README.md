# Python template for bots

## Tech stack

- **Python 3.13 & higher**
- Aiogram 3.x
- SQLAlchemy & Alembic
- PostgreSQL

Install & Run using [UV](https://docs.astral.sh/uv/getting-started/installation/)

```bash
uv venv
source .venv/Scripts/activate
uv sync
```

## Build

1. Create .env file & fill it with your data shown in .env.sample
2. Run database `docker-compose up -d`
    - You can add volume to make data persistent
    - Use `http://localhost:8080` for adminer. **Note:** use `db` as server
3. Run alembic migrations `alembic upgrade head`
    - After changes in models use `alembic revision --autogenerate -m "text"` and then `alembic upgrade head`
4. Run `uv run main.py`

* *Build Dockerfile for your needs.

## Structure

```bash
assets /            # Folder for assets
bot /
    filters /
        role.py     # Role filter
    handlers /      # All bot routes
    keyboards /     # All bot keyboards
    states /        # States for FSM
database /
    methods /   # CRUD operations 
    models /    # SQLAlchemy models (don't forget to import them in __init__.py)
    main.py     # Initialization script
alembic/        # Migration history and env.py config
config.py   # Configuration file, takes data from .env
main.py     # Main startup file
```