from pydantic import BaseModel

from database.models.enums import Role


class UserUpdate(BaseModel):
    role: Role = Role.USER
    username: str | None = None
