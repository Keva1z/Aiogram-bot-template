from typing import Any

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


def _getrepr(object: Any) -> str:
    """Returns string representation of object's attributes"""
    return ", ".join(
        f"{k}={v}" for k, v in object.__dict__.items() if not k.startswith("_")
    )


class Base(AsyncAttrs, DeclarativeBase):
    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self) -> str:
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)!r}")
        return f"{self.__class__.__name__}({', '.join(cols)})"
