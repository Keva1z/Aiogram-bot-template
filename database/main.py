import logging, uuid

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from config import config
from database.models import Base

logging.basicConfig(level=logging.INFO)

engine = create_async_engine(
    url=config.database.url,
    echo=False,
    connect_args={
		"prepared_statement_name_func": lambda: f"__asyncpg_{uuid.uuid4()}__",
		"statement_cache_size": 0,
		"prepared_statement_cache_size": 0,
	},
)
async_session = async_sessionmaker(engine, expire_on_commit=False)

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logging.info("Database connected")