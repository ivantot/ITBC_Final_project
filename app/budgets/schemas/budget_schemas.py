from typing import Optional
from pydantic import BaseModel, UUID4
from datetime import date

from app.categories.schemas import CategorySchema
from app.users.schemas import UserSchema


class BudgetSchema(BaseModel):
    budget_id: UUID4
    name: str
    user_id: str
    category_id: str
    start_date: date
    end_date: date
    currency: str
    balance: float
    is_active: bool

    user: UserSchema
    category: CategorySchema

    class Config:
        orm_mode = True


class BudgetSchemaIn(BaseModel):
    name: str
    user_id: str
    category_id: str
    start_date: str
    end_date: str
    currency: str
    balance: float

    class Config:
        orm_mode = True


class BudgetSchemaUpdate(BaseModel):
    name: Optional[str]
    user_id: Optional[str]
    category_id: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    currency: Optional[str]
    balance: Optional[float]

    class Config:
        orm_mode = True
