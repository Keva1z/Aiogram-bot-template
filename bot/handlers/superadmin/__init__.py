import logging

from aiogram import Router

from bot.filters.role import RoleFilter
from database.models import Role

# Superadmin routers
# from . import ...

logger = logging.getLogger(__name__)

router = Router(name="Superadmin")
router.message.filter(RoleFilter(role=[Role.SUPERADMIN]))
router.callback_query.filter(RoleFilter(role=[Role.SUPERADMIN]))

# router.include_routers()
