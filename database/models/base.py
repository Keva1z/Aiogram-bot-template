from typing import Any

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


def _getrepr(object: Any) -> str:
    """Returns string representation of object's attributes"""
    return ", ".join(
        f"{k}={v}" for k, v in object.__dict__.items() if not k.startswith("_")
    )


class Base(AsyncAttrs, DeclarativeBase):
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({_getrepr(self)})"
