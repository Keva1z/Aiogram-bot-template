import logging

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import config
from database.models import Base

logging.basicConfig(level=logging.INFO)

engine = create_async_engine(
    url=config.database.url,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=300,
)
async_session = async_sessionmaker(
    engine, autoflush=True, autocommit=False, expire_on_commit=False
)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logging.info("Database connected")
