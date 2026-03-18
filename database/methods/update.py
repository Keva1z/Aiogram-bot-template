from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Role, User

# Example:


class update_user:
    @staticmethod
    async def role(session: AsyncSession, userid: int, role: Role) -> User | None:
        result = await session.execute(select(User).where(User.userid == userid))
        user = result.scalar_one_or_none()

        if not user:
            return None

        user.role = role
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
