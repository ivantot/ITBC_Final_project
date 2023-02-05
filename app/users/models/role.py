from uuid import uuid4

from sqlalchemy import Column, String

from app.db import Base
from app.users.enums import RoleEnum


class Role(Base):
    __tablename__ = "roles"
    role_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    role_type = Column(String(100), unique=True)

    def __init__(self, role_type: RoleEnum):
        self.role_type = role_type
