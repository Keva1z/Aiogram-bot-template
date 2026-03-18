from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.enums import Role
from database.repositories.user import get_by_userid


class RoleFilter(BaseFilter):
    def __init__(self, role: Union[Role, list[Role]]):
        self.role = role if isinstance(role, list) else [role]

    async def __call__(
        self, event: Union[Message, CallbackQuery], session: AsyncSession
    ) -> bool:
        """Check if user has required role"""
        if not event.from_user:
            return False

        user = await get_by_userid(session, event.from_user.id)

        if not user:
            return False

        return user.role in self.role
