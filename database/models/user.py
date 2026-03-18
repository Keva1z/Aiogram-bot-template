from sqlalchemy import (
    BigInteger,
    Enum,
)
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .enums import Role


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    userid: Mapped[int] = mapped_column(BigInteger, unique=True)
    role: Mapped[Role] = mapped_column(Enum(Role), default=Role.USER)
