from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database.models import User


async def delete_user(session: AsyncSession, userid: int) -> None:
    result = await session.execute(select(User).where(User.userid == userid))
    user = result.scalar_one_or_none()

    if not user:
        return

    await session.delete(user)
    await session.commit()
