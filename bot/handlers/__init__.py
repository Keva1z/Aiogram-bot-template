from aiogram import Dispatcher

from bot.handlers import admin, start, superadmin, user

__all__ = ["superadmin", "admin", "start", "user"]


def setup_handlers(dp: Dispatcher):
    dp.include_routers(user.router, admin.router, superadmin.router, start.router)
