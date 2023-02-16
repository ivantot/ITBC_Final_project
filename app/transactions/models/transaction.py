from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.db import Base


class Transaction(Base):
    __tablename__ = "transactions"
    transaction_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    outbound = Column(Boolean, default=True)
    amount = Column(Float)
    currency = Column(String(10), default="DIN")
    transaction_time = Column(DateTime, default=datetime.utcnow())
    user_id = Column(String(50), ForeignKey("users.user_id"), nullable=False, unique=False)
    vendor_id = Column(String(50), ForeignKey("vendors.vendor_id"), nullable=False, unique=False)
    is_valid = Column(Boolean, default=True)

    user = relationship("User", lazy="subquery")
    vendor = relationship("Vendor", lazy="subquery")

    def __init__(self,
                 amount: float,
                 user_id: str,
                 vendor_id: str,
                 outbound: bool = True,
                 currency: str = "DIN",
                 transaction_time: datetime = datetime.utcnow(),
                 is_valid: bool = True):
        self.amount = amount
        self.user_id = user_id
        self.vendor_id = vendor_id
        self.outbound = outbound
        self.currency = currency
        self.transaction_time = transaction_time
        self.is_valid = is_valid
