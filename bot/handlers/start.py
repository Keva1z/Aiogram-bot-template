import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    BotCommand,
    BotCommandScopeChat,
    Message,
)
from sqlalchemy.ext.asyncio import AsyncSession

from config import config
from database.models import Role
from database.repositories.user import UserUpdate, create_user, update_user

logger = logging.getLogger(__name__)

router = Router(name="start")

user_commands = [
    BotCommand(command="start", description="Запустить бота"),
]


admin_commands = [
    *user_commands,
    BotCommand(command="admin", description="Открыть админ панель"),
]


@router.message(CommandStart())
async def cmd_start(message: Message, session: AsyncSession, state: FSMContext):
    """Handle /start command"""
    if not message.from_user or not message.bot:
        return

    logger.info(f"User {message.from_user.id} started bot")

    # Create user if not exists
    user = await create_user(session, message.from_user.id)

    await state.clear()

    # Update owner role
    if user.userid in config.SUPERADMIN_IDS and user.role != Role.SUPERADMIN:
        user = await update_user(session, user.userid, UserUpdate(role=Role.SUPERADMIN))
        if user is None:
            return

    commands = admin_commands if user.role in [Role.SUPERADMIN] else user_commands
    await message.bot.set_my_commands(
        commands, scope=BotCommandScopeChat(chat_id=message.chat.id)
    )

    await message.answer("Заглушка!")
