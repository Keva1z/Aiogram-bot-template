from typing import Optional

from pydantic import BaseModel

from database.models.enums import Role


class UserUpdate(BaseModel):
    role: Optional[Role] = None
    username: Optional[str] = None
