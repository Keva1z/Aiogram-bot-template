from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User


async def create_user(
    session: AsyncSession, userid: int
) -> User:  # Создает нового пользователя
    result = await session.execute(select(User).where(User.userid == userid))
    user = result.scalar_one_or_none()

    if not user:
        user = User(userid=userid)
        session.add(user)
        await session.commit()
        await session.refresh(user)

    return user
