"""Budget controllers module."""
from typing import Dict

from fastapi import HTTPException

from app.budgets.exceptions import BudgetNotFoundException, StartAfterEndDateException, \
    ActiveBudgetForCategoryExistsException
from app.budgets.models import Budget
from app.budgets.services import BudgetService
from app.categories.exceprtions import CategoryNotActiveException, CategoryNotFoundException
from app.money_accounts.exceptions import CurrencyNotAllowedException
from app.users.exceptions import UserNotActiveException, UserNotFoundException


class BudgetController:
    """BudgetController class"""

    @staticmethod
    def create_budget(name: str,
                      user_id: str,
                      category_id: str,
                      start_date: str,
                      end_date: str,
                      limit,
                      currency: str = "DIN",
                      balance: float = 0.0):
        """create_budget function"""
        try:
            budget = BudgetService.create_budget(name,
                                                 user_id,
                                                 category_id,
                                                 start_date,
                                                 end_date,
                                                 limit,
                                                 currency,
                                                 balance)
            return budget
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except UserNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except CategoryNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except CategoryNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except ActiveBudgetForCategoryExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except StartAfterEndDateException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except CurrencyNotAllowedException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def read_budget_by_id(budget_id: str):
        """read_budget_by_id function"""
        budget = BudgetService.read_budget_by_id(budget_id)
        if budget:
            return budget
        raise HTTPException(status_code=400, detail=f"Budget with provided id {budget_id} does not exist.")

    @staticmethod
    def read_budgets_by_user_id(user_id: str):
        """read_budgets_by_user_id function"""
        budgets = BudgetService.read_budgets_by_user_id(user_id)
        if budgets:
            return budgets
        raise HTTPException(status_code=400, detail=f"Budgets with provided user id {user_id} do not exist.")

    @staticmethod
    def read_budgets_by_category_id(category_id: str):
        """read_budgets_by_category_id function"""
        budgets = BudgetService.read_budgets_by_category_id(category_id)
        if budgets:
            return budgets
        raise HTTPException(status_code=400,
                            detail=f"Budgets with provided category id {category_id} do not exist.")

    @staticmethod
    def read_budgets_by_currency(currency: str):
        """read_budgets_by_currency function"""
        budgets = BudgetService.read_budgets_by_currency(currency)
        if budgets:
            return budgets
        raise HTTPException(status_code=400,
                            detail=f"Budgets with provided currency {currency} do not exist.")

    @staticmethod
    def read_all_budgets():
        """read_all_budgets function"""
        budgets = BudgetService.read_all_budgets()
        return budgets

    @staticmethod
    def update_budget_is_active(budget_id: str, is_active: bool):
        """update_budget_is_active function"""
        try:
            return BudgetService.update_budget_is_active(budget_id, is_active)
        except BudgetNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_budget_by_id(budget_id: str,
                            name: str = None,
                            user_id: str = None,
                            category_id: str = None,
                            start_date: str = None,
                            end_date: str = None,
                            currency: str = None,
                            limit: float = None,
                            balance: float = None):
        """update_budget_by_id function"""
        try:
            return BudgetService.update_budget_by_id(budget_id=budget_id,
                                                     name=name,
                                                     user_id=user_id,
                                                     category_id=category_id,
                                                     start_date=start_date,
                                                     end_date=end_date,
                                                     currency=currency,
                                                     limit=limit,
                                                     balance=balance)
        except BudgetNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except CurrencyNotAllowedException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_budget_by_id(budget_id: str):
        """delete_budget_by_id function"""
        try:
            BudgetService.delete_budget_by_id(budget_id)
            return {"message": f"Budget with provided id, {budget_id} has been deleted."}
        except BudgetNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) from e

    @staticmethod
    def read_budgets_funds_per_category_by_user_id(user_id: str) -> Dict[str, list[Budget]]:
        """read_budgets_funds_per_category_by_user_id function"""
        budgets = BudgetService.read_budgets_funds_per_category_by_user_id(user_id)
        if budgets:
            return budgets
        raise HTTPException(status_code=400, detail=f"Budgets with provided user id {user_id} do not exist.")
