from typing import Optional
from pydantic import BaseModel, UUID4

from app.users.schemas import UserSchema


class MoneyAccountSchema(BaseModel):
    money_account_id: UUID4
    name: str
    user_id: str
    currency: str
    balance: float
    is_active: bool
    user: UserSchema

    class Config:
        orm_mode = True


class MoneyAccountSchemaIn(BaseModel):
    name: str
    user_id: str
    currency: Optional[str] = "DIN"
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
