"""Users models module."""
from uuid import uuid4

from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from app.db import Base


class User(Base):
    """User class"""
    __tablename__ = "users"
    user_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    is_active = Column(Boolean, default=True)

    roles = relationship("UserHasRole", lazy="subquery", viewonly=True)

    def __init__(self, email: str, password: str, is_active: bool = True):
        self.email = email
        self.password = password
        self.is_active = is_active
