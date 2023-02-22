"""Transactions schemas module."""
from datetime import datetime
from pydantic import BaseModel, UUID4

from app.users.schemas import UserSchema
from app.vendors.schemas import VendorSchema


class TransactionSchema(BaseModel):
    """TransactionSchema class"""
    transaction_id: UUID4
    amount: float
    user_id: str
    vendor_id: str
    outbound: bool
    currency: str
    transaction_time: datetime
    is_valid: bool
    cash_payment: bool

    user: UserSchema
    vendor: VendorSchema

    class Config:
        """Config class"""
        orm_mode = True


class TransactionVendorSchema(BaseModel):
    """TransactionVendorSchema class"""
    transaction_id: UUID4
    amount: float
    outbound: bool
    currency: str
    transaction_time: datetime
    is_valid: bool
    cash_payment: bool

    class Config:
        """Config class"""
        orm_mode = True


class TransactionInOutboundSchema(BaseModel):
    """TransactionInOutboundSchema class"""
    transaction_id: UUID4
    amount: float
    user_id: str
    vendor_id: str
    outbound: bool
    currency: str
    transaction_time: datetime
    is_valid: bool
    cash_payment: bool

    class Config:
        """Config class"""
        orm_mode = True


class TransactionSchemaIn(BaseModel):
    """TransactionSchemaIn class"""
    amount: float
    user_id: str
    vendor_id: str
    outbound: bool
    currency: str
    cash_payment: bool

    class Config:
        """Config class"""
        orm_mode = True


class TransactionSchemaUpdateIsValid(BaseModel):
    """TransactionSchemaUpdateIsValid class"""
    transaction_id: str
    is_valid: bool

    class Config:
        """Config class"""
        orm_mode = True
