"""Vendors models module."""
from uuid import uuid4

from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class Vendor(Base):
    """Vendor class"""
    __tablename__ = "vendors"
    vendor_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(100), unique=True)
    address = Column(String(200))
    cash_only = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    category_id = Column(String(50), ForeignKey("categories.category_id"), nullable=False, unique=False)

    category = relationship("Category", lazy="subquery")

    def __init__(self,
                 name: str,
                 address: str,
                 category_id: str,
                 cash_only: bool = False,
                 is_active: bool = True):
        self.name = name
        self.address = address
        self.category_id = category_id
        self.cash_only = cash_only
        self.is_active = is_active
