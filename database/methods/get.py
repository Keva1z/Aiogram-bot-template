from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database.models import User, Role


class get_user:
    @staticmethod
    async def by_userid(session: AsyncSession, userid: int) -> User | None:
            return (
                await session.execute(select(User).where(User.userid == userid))
            ).scalar_one_or_none()

    @staticmethod
    async def all(session: AsyncSession):
        return (await session.execute(select(User))).scalars().all()
