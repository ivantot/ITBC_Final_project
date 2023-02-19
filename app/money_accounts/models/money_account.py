from uuid import uuid4

from sqlalchemy import Column, String, Boolean, Float, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

from app.db import Base

from app.config import settings

CURRENCIES = settings.CURRENCIES.split(",")


class MoneyAccount(Base):
    __tablename__ = "money_accounts"
    money_account_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(100))
    user_id = Column(String(50), ForeignKey("users.user_id"), nullable=False, unique=True)
    currency = Column(String(10), default="DIN")
    balance = Column(Float, default=0.0)
    is_active = Column(Boolean, default=True)
    __table_args__ = (CheckConstraint(currency.in_(CURRENCIES), name='money_account_currencies_cc'),)

    user = relationship("User", lazy="subquery")

    def __init__(self, name: str, user_id: str, currency: str = "DIN", balance: float = 0.0, is_active: bool = True):
        self.name = name
        self.user_id = user_id
        self.currency = currency
        self.balance = balance
        self.is_active = is_active
