from typing import Optional
from pydantic import BaseModel, UUID4


class MoneyAccountSchema(BaseModel):
    money_account_id: UUID4
    name: str
    user_id: str
    currency: str
    balance: float
    is_active: bool

    class Config:
        orm_mode = True


class MoneyAccountSchemaIn(BaseModel):
    name: str
    user_id: str
    currency: str
    balance: float

    class Config:
        orm_mode = True


class MoneyAccountSchemaUpdate(BaseModel):
    name: Optional[str]
    user_id: Optional[str]
    currency: Optional[str]
    balance: Optional[float]

    class Config:
        orm_mode = True
