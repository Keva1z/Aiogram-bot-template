import logging
import os

import dotenv

dotenv.load_dotenv(override=True)
logger = logging.getLogger(__name__)

class Database:
    DB_USER = os.getenv("DB_USER", "user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    DB_NAME = os.getenv("DB_NAME", "database")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", "5432"))

    @property
    def url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property
    def url_alembic(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

class Config:
    bot_token = os.getenv("BOT_TOKEN", "")
    database = Database()
    superadmin_ids: list[int] = list(
        map(int, os.getenv("SUPERADMIN_IDS", "").split(","))
    )

config = Config()
