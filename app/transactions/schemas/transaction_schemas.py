from datetime import datetime
from pydantic import BaseModel, UUID4


class TransactionSchema(BaseModel):
    transaction_id: UUID4
    amount: float
    user_id: str
    vendor_id: str
    outbound: bool
    currency: str
    transaction_time: datetime
    is_valid: bool

    class Config:
        orm_mode = True


class TransactionSchemaIn(BaseModel):
    amount: float
    user_id: str
    vendor_id: str
    outbound: bool
    currency: str

    class Config:
        orm_mode = True
