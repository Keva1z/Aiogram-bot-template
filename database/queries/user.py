from typing import cast

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.enums import Role
from database.models.user import User


class UserUpdate(BaseModel):
    role: Role = Role.USER
    username: str | None = None


async def get_by_userid(session: AsyncSession, userid: int) -> User | None:
    """Get user by USERID"""
    query = select(User).where(User.userid == userid)
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def get_all(
    session: AsyncSession, limit: int = 10, offset: int = 0
) -> list[User]:
    """Get all users"""
    query = select(User).limit(limit).offset(offset)
    result = await session.execute(query)
    return list(result.scalars().all())


async def update_user(
    session: AsyncSession, userid: int, update: UserUpdate
) -> User | None:
    """Update user with schema"""
    user = await get_by_userid(session, userid)

    if user is None:
        return None

    updates = cast(dict[str, object], update.model_dump(exclude_unset=True))

    for key, value in updates.items():
        setattr(user, key, value)

    return user


async def create_user(session: AsyncSession, userid: int, **data) -> User:
    """Create new user"""
    user = User(userid=userid, **data)
    session.add(user)

    return user


async def delete(session: AsyncSession, userid: int) -> None:
    """Delete user"""
    user = await get_by_userid(session, userid)

    if user is None:
        return

    await session.delete(user)
