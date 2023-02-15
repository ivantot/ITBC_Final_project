from fastapi import HTTPException

from app.budgets.services import BudgetServices


class BudgetController:

    @staticmethod
    def create_budget(name: str,
                      user_id: str,
                      category_id: str,
                      start_date: str,
                      end_date: str,
                      currency: str = "DIN",
                      balance: float = 0.0):
        try:
            budget = BudgetServices.create_budget(name,
                                                  user_id,
                                                  category_id,
                                                  start_date,
                                                  end_date,
                                                  currency,
                                                  balance)
            return budget
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_budget_by_id(budget_id: str):
        budget = BudgetServices.read_budget_by_id(budget_id)
        if budget:
            return budget
        else:
            raise HTTPException(status_code=400, detail=f"Budget with provided id {budget_id} does not exist.")

    @staticmethod
    def read_budgets_by_user_id(user_id: str):
        budgets = BudgetServices.read_budgets_by_user_id(user_id)
        if budgets:
            return budgets
        else:
            raise HTTPException(status_code=400, detail=f"Budgets with provided user id {user_id} do not exist.")

    @staticmethod
    def read_budgets_by_category_id(category_id: str):
        budgets = BudgetServices.read_budgets_by_category_id(category_id)
        if budgets:
            return budgets
        else:
            raise HTTPException(status_code=400,
                                detail=f"Budgets with provided category id {category_id} do not exist.")

    @staticmethod
    def read_budgets_by_currency(currency: str):
        budgets = BudgetServices.read_budgets_by_currency(currency)
        if budgets:
            return budgets
        else:
            raise HTTPException(status_code=400,
                                detail=f"Budgets with provided currency {currency} do not exist.")

    @staticmethod
    def read_all_budgets():
        budgets = BudgetServices.read_all_budgets()
        return budgets

    @staticmethod
    def update_budget_is_active(budget_id: str, is_active: bool):
        try:
            return BudgetServices.update_budget_is_active(budget_id, is_active)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_budget_by_id(budget_id: str,
                            name: str = None,
                            user_id: str = None,
                            category_id: str = None,
                            start_date: str = None,
                            end_date: str = None,
                            currency: str = None,
                            balance: float = None):
        try:
            return BudgetServices.update_budget_by_id(budget_id,
                                                      name,
                                                      user_id,
                                                      category_id,
                                                      start_date,
                                                      end_date,
                                                      currency,
                                                      balance)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_budget_by_id(budget_id: str):
        try:
            BudgetServices.delete_budget_by_id(budget_id)
            return {"message": f"Budget with provided id, {budget_id} has been deleted."}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
