"""Budgets schemas module."""
from typing import Optional
from datetime import date
from pydantic import BaseModel, UUID4

from app.categories.schemas import CategorySchema
from app.users.schemas import UserSchema


class BudgetSchema(BaseModel):
    """BudgetSchema class"""
    budget_id: UUID4
    name: str
    user_id: str
    category_id: str
    start_date: date
    end_date: date
    currency: str
    balance: float
    limit: float
    is_active: bool

    user: UserSchema
    category: CategorySchema

    class Config:
        """Config class"""
        orm_mode = True


class BudgetFundsSchema(BaseModel):
    """BudgetFundsSchema class"""
    name: str
    currency: str
    balance: float
    limit: float
    is_active: bool

    class Config:
        """Config class"""
        orm_mode = True


class BudgetSchemaIn(BaseModel):
    """BudgetSchemaIn class"""
    name: str
    user_id: str
    category_id: str
    start_date: str
    end_date: str
    currency: str
    limit: float

    class Config:
        """Config class"""
        orm_mode = True


class BudgetSchemaUpdate(BaseModel):
    """BudgetSchemaUpdate class"""
    name: Optional[str]
    user_id: Optional[str]
    category_id: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    currency: Optional[str]
    limit: Optional[float]
    balance: Optional[float]

    class Config:
        """Config class"""
        orm_mode = True


class BudgetSchemaUpdateIsActive(BaseModel):
    """BudgetSchemaUpdateIsActive class"""
    budget_id: str
    is_active: bool

    class Config:
        """Config class"""
        orm_mode = True
