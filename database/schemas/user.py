from typing import Optional

from pydantic import BaseModel

from database.models.enums import Role


class UserUpdate(BaseModel):
    role: Role = Role.USER
    username: Optional[str] = None
