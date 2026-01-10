from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, String, Boolean, Integer, ForeignKey, DateTime, JSON, Enum as SQLEnum, Float

from .base import Base
from .enums import Role

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    userid: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    role: Mapped[Role] = mapped_column(SQLEnum(Role), nullable=False, default=Role.USER)
