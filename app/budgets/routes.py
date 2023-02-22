"""Budgets module."""
from fastapi import APIRouter, Depends

from app.budgets.controllers import BudgetController
from app.budgets.schemas import BudgetSchema, BudgetSchemaIn, BudgetSchemaUpdate, BudgetFundsSchema, \
    BudgetSchemaUpdateIsActive
from app.users.controllers.user_auth_controller import JWTBearer

budget_router = APIRouter(tags=["Budgets"], prefix="/api/budgets")


@budget_router.post("/add-new-budget", response_model=BudgetSchema,
                    dependencies=[Depends(JWTBearer("USER"))])
def create_category(budget: BudgetSchemaIn):
    """create_category route"""
    budget = BudgetController.create_budget(name=budget.name,
                                            user_id=budget.user_id,
                                            category_id=budget.category_id,
                                            start_date=budget.start_date,
                                            end_date=budget.end_date,
                                            currency=budget.currency,
                                            limit=budget.limit)
    return budget


@budget_router.get("/id", response_model=BudgetSchema,
                   dependencies=[Depends(JWTBearer("USER"))])
def get_budget_by_id(budget_id: str):
    """get_budget_by_id route"""
    return BudgetController.read_budget_by_id(budget_id)


@budget_router.get("/get-budgets-by-user-id", response_model=list[BudgetSchema],
                   dependencies=[Depends(JWTBearer("USER"))])
def get_budgets_by_user_id(user_id: str):
    """get_budgets_by_user_id route"""
    return BudgetController.read_budgets_by_user_id(user_id)


@budget_router.get("/get-budgets-by-category-id", response_model=list[BudgetSchema],
                   dependencies=[Depends(JWTBearer("USER"))])
def get_budgets_by_category_id(category_id: str):
    """get_budgets_by_category_id route"""
    return BudgetController.read_budgets_by_category_id(category_id)


@budget_router.get("/get-budgets-by-currency", response_model=list[BudgetSchema],
                   dependencies=[Depends(JWTBearer("ADMIN"))])
def get_budgets_by_currency(currency: str):
    """get_budgets_by_currency route"""
    return BudgetController.read_budgets_by_currency(currency)


@budget_router.get("/get-all-budgets", response_model=list[BudgetSchema],
                   dependencies=[Depends(JWTBearer("ADMIN"))])
def get_all_budgets():
    """get_all_budgets route"""
    return BudgetController.read_all_budgets()


@budget_router.put("/update/is_active", response_model=BudgetSchema,
                   dependencies=[Depends(JWTBearer("ADMIN"))])
def update_budget_is_active(budget: BudgetSchemaUpdateIsActive):
    """update_budget_is_active route"""
    return BudgetController.update_budget_is_active(budget.budget_id, budget.is_active)


@budget_router.put("/update", response_model=BudgetSchema,
                   dependencies=[Depends(JWTBearer("USER"))])
def update_budget_by_id(budget_id: str, budget: BudgetSchemaUpdate = None):
    """update_budget_by_id route"""
    return BudgetController.update_budget_by_id(budget_id=budget_id,
                                                name=budget.name,
                                                user_id=budget.user_id,
                                                category_id=budget.category_id,
                                                start_date=budget.start_date,
                                                end_date=budget.end_date,
                                                currency=budget.currency,
                                                limit=budget.limit,
                                                balance=budget.balance)


@budget_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_budget_by_id(budget_id: str):
    """delete_budget_by_id route"""
    return BudgetController.delete_budget_by_id(budget_id)


@budget_router.get("/get-budgets-funds-by-user-id", response_model=dict[str, list[BudgetFundsSchema]],
                   dependencies=[Depends(JWTBearer("USER"))])
def get_budgets_funds_per_category_by_user_id(user_id: str):
    """get_budgets_funds_per_category_by_user_id route"""
    return BudgetController.read_budgets_funds_per_category_by_user_id(user_id)
