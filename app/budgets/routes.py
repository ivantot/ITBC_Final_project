from fastapi import APIRouter, Depends

from app.budgets.controllers import BudgetController
from app.budgets.schemas import BudgetSchema, BudgetSchemaIn, BudgetSchemaUpdate
from app.users.controllers.user_auth_controller import JWTBearer

budget_router = APIRouter(tags=["Budgets"], prefix="/api/budgets")


@budget_router.post("/add-new-budget", response_model=BudgetSchema)
def create_category(budget: BudgetSchemaIn):
    budget = BudgetController.create_budget(budget.name,
                                            budget.user_id,
                                            budget.category_id,
                                            budget.start_date,
                                            budget.end_date,
                                            budget.currency,
                                            budget.balance)
    return budget


@budget_router.get("/id", response_model=BudgetSchema)
def get_budget_by_id(budget_id: str):
    return BudgetController.read_budget_by_id(budget_id)


@budget_router.get("/get-budgets-by-user-id", response_model=list[BudgetSchema])
def get_budgets_by_user_id(user_id: str):
    return BudgetController.read_budgets_by_user_id(user_id)


@budget_router.get("/get-budgets-by-category-id", response_model=list[BudgetSchema])
def get_budgets_by_category_id(category_id: str):
    return BudgetController.read_budgets_by_category_id(category_id)


@budget_router.get("/get-budgets-by-currency", response_model=list[BudgetSchema])
def get_budgets_by_currency(currency: str):
    return BudgetController.read_budgets_by_currency(currency)


@budget_router.get("/get-all-budgets", response_model=list[BudgetSchema])
def get_all_budgets():
    return BudgetController.read_all_budgets()


@budget_router.put("/update/is_active", response_model=BudgetSchema)
def update_budget_is_active(budget_id: str, is_active: bool):
    return BudgetController.update_budget_is_active(budget_id, is_active)


@budget_router.put("/update", response_model=BudgetSchema)
def update_budget_by_id(budget_id: str, budget: BudgetSchemaUpdate = None):
    return BudgetController.update_budget_by_id(budget_id,
                                                budget.name,
                                                budget.user_id,
                                                budget.category_id,
                                                budget.start_date,
                                                budget.end_date,
                                                budget.currency,
                                                budget.balance)


@budget_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_budget_by_id(budget_id: str):
    return BudgetController.delete_budget_by_id(budget_id)
