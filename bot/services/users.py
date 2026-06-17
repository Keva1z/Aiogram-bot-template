from sqlalchemy.ext.asyncio import AsyncSession

from database.models.user import User
from database.queries.user import create_user, get_by_userid


async def get_or_create_user(session: AsyncSession, userid: int, **data) -> User:
    """Get user by USERID or create new user"""
    user = await get_by_userid(session, userid)

    if user is None:
        user = await create_user(session, userid, **data)

    await session.commit()

    return user
