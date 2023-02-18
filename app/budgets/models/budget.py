from uuid import uuid4
from datetime import datetime

from sqlalchemy import Column, String, Boolean, Float, ForeignKey, Date, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import relationship

from app.db import Base


class Budget(Base):
    __tablename__ = "budgets"
    budget_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(100))
    balance = Column(Float, default=0.0)
    currency = Column(String(10), default="DIN")
    start_date = Column(Date)
    end_date = Column(Date)
    is_active = Column(Boolean, default=True)
    user_id = Column(String(50), ForeignKey("users.user_id"), nullable=False, unique=False)
    category_id = Column(String(50), ForeignKey("categories.category_id"), nullable=False, unique=False)
    __table_args__ = (UniqueConstraint("user_id", "category_id", name="user_category_uc"),
                      CheckConstraint(start_date < end_date, name='start_end_cc'))

    user = relationship("User", lazy="subquery")
    category = relationship("Category", lazy="subquery")

    def __init__(self, name: str,
                 user_id: str,
                 category_id: str,
                 start_date: str,
                 end_date: str,
                 currency: str = "DIN",
                 balance: float = 0.0,
                 is_active: bool = True):
        self.name = name
        self.user_id = user_id
        self.category_id = category_id
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.currency = currency
        self.balance = balance
        self.is_active = is_active
