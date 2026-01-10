import asyncio
import logging
import os

from aiogram import Bot, Dispatcher

from config import config
from bot.handlers import setup_handlers
from database.main import async_main, async_session

from bot.middlewares.sessions import DbSessionMiddleware

bot = Bot(token=config.bot_token)
dp = Dispatcher(bot=bot)

logging.basicConfig(level=logging.INFO)


async def on_startup():
    await async_main()  # Initialize database

    setup_handlers(dp)

    logging.info("Bot started")


async def main() -> None:

    dp.update.middleware(DbSessionMiddleware(session_pool=async_session))
    dp.startup.register(on_startup)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
