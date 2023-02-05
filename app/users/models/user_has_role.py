from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base
from app.users.enums import RoleEnum


class UserHasRole(Base):
    __tablename__ = "user_has_roles"
    user_has_role_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    user_id = Column(String(50), ForeignKey("users.user_id"))
    role_id = Column(String(50), ForeignKey("roles.role_id"))

    user = relationship("Users", lazy="subquery")
    role = relationship("Roles", lazy="subquery")

    def __init__(self, role_type: RoleEnum):
        self.role_type = role_type
