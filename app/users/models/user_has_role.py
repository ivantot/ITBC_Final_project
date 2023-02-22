"""Users models module."""
from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class UserHasRole(Base):
    """UserHasRole class"""
    __tablename__ = "user_has_roles"
    user_has_role_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    user_id = Column(String(50), ForeignKey("users.user_id"), nullable=False)
    role_id = Column(String(50), ForeignKey("roles.role_id"), nullable=False)

    user = relationship("User", lazy="subquery")
    role = relationship("Role", lazy="subquery")

    def __init__(self, user_id: str, role_id: str):
        self.user_id = user_id
        self.role_id = role_id
