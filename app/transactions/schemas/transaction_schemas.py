from datetime import datetime
from pydantic import BaseModel, UUID4

from app.users.schemas import UserSchema
from app.vendors.schemas import VendorSchema


class TransactionSchema(BaseModel):
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
        orm_mode = True


class TransactionVendorSchema(BaseModel):
    transaction_id: UUID4
    amount: float
    outbound: bool
    currency: str
    transaction_time: datetime
    is_valid: bool
    cash_payment: bool

    class Config:
        orm_mode = True


class TransactionSchemaIn(BaseModel):
    amount: float
    user_id: str
    vendor_id: str
    outbound: bool
    currency: str
    cash_payment: bool

    class Config:
        orm_mode = True
