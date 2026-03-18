import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.handlers import setup_handlers
from bot.middlewares.sessions import DbSessionMiddleware
from config import config
from database.main import async_main, async_session

bot = Bot(token=config.BOT_TOKEN)
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
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.warning("Bot stopped!")
