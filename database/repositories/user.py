from typing import cast

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from database.exceptions import UserCreateError
from database.schemas.user import UserUpdate

from ..models.user import User


async def get_by_userid(session: AsyncSession, userid: int) -> User | None:
    query = select(User).where(User.userid == userid)
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def get_all(session: AsyncSession) -> list[User]:
    query = select(User)
    result = await session.execute(query)
    return list(result.scalars().all())


async def update_user(
    session: AsyncSession, userid: int, update: UserUpdate
) -> User | None:
    user = await get_by_userid(session, userid)

    if user is None:
        return None

    updates = cast(dict[str, object], update.model_dump(exclude_unset=True))

    for key, value in updates.items():
        setattr(user, key, value)

    await session.commit()
    await session.refresh(user)
    return user


async def create(session: AsyncSession, userid: int, **data) -> User:
    user = User(userid=userid, **data)
    session.add(user)

    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()

        user = await get_by_userid(session, userid)
        if user is not None:
            return user

        raise UserCreateError()
    else:
        await session.refresh(user)
        return user


async def delete(session: AsyncSession, userid: int) -> bool:
    user = await get_by_userid(session, userid)

    if user is None:
        return False

    try:
        await session.delete(user)
        await session.commit()
        return True
    except SQLAlchemyError:
        await session.rollback()
        raise
