from enum import Enum
from typing import Any

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class PaginationActions(Enum):
    NEXT = "NEXT"
    PREVIOUS = "PREV"
    OPEN = "OPEN"
    BACK = "BACK"
    CLOSE = "CLOSE"


# Base class for pagination keyboards
# Inherit from it & use "prefix=..."
class Pagination(CallbackData, prefix="Pagination"):
    action: PaginationActions
    page: int = 0
    value: Any = None


# Function to add pagination controls to a keyboard builder
def add_pagination_controls(
    page: int,
    limit: int,
    length: int,
    builder: InlineKeyboardBuilder,
    *,
    x_action: PaginationActions = PaginationActions.CLOSE,
) -> InlineKeyboardBuilder:
    """Adds controls for pagination (previous, close, next) to the keyboard builder."""
    if page > 0:
        callback = Pagination(action=PaginationActions.PREVIOUS, page=page - 1)
        builder.button(text="◀️", callback_data=callback.pack())

    callback = Pagination(action=x_action)
    builder.button(text="❌", callback_data=callback.pack())

    if length >= limit:
        callback = Pagination(action=PaginationActions.NEXT)
        builder.button(text="▶️", callback_data=callback.pack())

    return builder


# Universal pagination keyboard creation function
# You can create your own function based on this, use it as example
def create_pagination_keyboard(
    data: dict[str, Any], page: int, limit: int
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    if len(data) > limit:
        raise ValueError(
            "Data must have the same length and be less than or equal to limit"
        )

    for name, value in data.items():
        callback = Pagination(action=PaginationActions.OPEN, page=page, value=value)
        builder.button(text=f"{name}", callback_data=callback.pack())

    builder = add_pagination_controls(page, limit, len(data), builder)

    builder.adjust(*[1 for i in range(len(data))], 3)

    return builder.as_markup()
