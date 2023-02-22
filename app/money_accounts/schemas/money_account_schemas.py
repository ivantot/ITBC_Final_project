"""Money account schemas module."""
from typing import Optional
from pydantic import BaseModel, UUID4

from app.users.schemas import UserSchema


class MoneyAccountSchema(BaseModel):
    """MoneyAccountSchema class"""
    money_account_id: UUID4
    name: str
    user_id: str
    currency: str
    balance: float
    is_active: bool
    user: UserSchema

    class Config:
        """Config class"""
        orm_mode = True


class MoneyAccountSchemaIn(BaseModel):
    """MoneyAccountSchemaIn class"""
    name: str
    user_id: str
    currency: Optional[str] = "DIN"
    balance: float

    class Config:
        """Config class"""
        orm_mode = True


class MoneyAccountSchemaUpdate(BaseModel):
    """MoneyAccountSchemaUpdate class"""
    name: Optional[str]
    user_id: Optional[str]
    currency: Optional[str]
    balance: Optional[float]

    class Config:
        """Config class"""
        orm_mode = True


class MoneyAccountSchemaUpdateIsActive(BaseModel):
    """MoneyAccountSchemaUpdateIsActive class"""
    money_account_id: str
    is_active: bool

    class Config:
        """Config class"""
        orm_mode = True
