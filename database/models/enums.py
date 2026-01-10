from enum import Enum, auto
from sqlalchemy import Enum as SQLEnum

class Role(Enum):
    USER = "USER"
    ADMIN = "ADMIN"
    SUPERADMIN = "SUPERADMIN"