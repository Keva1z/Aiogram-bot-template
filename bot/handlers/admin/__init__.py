import logging

from aiogram import Router

from bot.filters.role import RoleFilter
from database.models import Role

# Admin routers
# from . import ...

logger = logging.getLogger(__name__)

router = Router(name="Admin")
router.message.filter(RoleFilter(role=[Role.SUPERADMIN, Role.ADMIN]))
router.callback_query.filter(RoleFilter(role=[Role.SUPERADMIN, Role.ADMIN]))

# router.include_routers()
