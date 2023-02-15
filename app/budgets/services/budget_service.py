from app.budgets.repositories import BudgetRepository
from app.db import SessionLocal


class BudgetServices:

    @staticmethod
    def create_budget(name: str,
                      user_id: str,
                      category_id: str,
                      start_date: str,
                      end_date: str,
                      currency: str = "DIN",
                      balance: float = 0.0):
        with SessionLocal() as db:
            try:
                budget_repository = BudgetRepository(db)
                return budget_repository.create_budget(name,
                                                       user_id,
                                                       category_id,
                                                       start_date,
                                                       end_date,
                                                       currency,
                                                       balance)
            except Exception as e:
                raise e

    @staticmethod
    def read_budget_by_id(budget_id: str):
        with SessionLocal() as db:
            budget_repository = BudgetRepository(db)
            return budget_repository.read_budget_by_id(budget_id)

    @staticmethod
    def read_budgets_by_user_id(user_id: str):
        with SessionLocal() as db:
            budget_repository = BudgetRepository(db)
            return budget_repository.read_budgets_by_user_id(user_id)

    @staticmethod
    def read_budgets_by_category_id(category_id: str):
        with SessionLocal() as db:
            budget_repository = BudgetRepository(db)
            return budget_repository.read_budgets_by_category_id(category_id)

    @staticmethod
    def read_all_budgets():
        with SessionLocal() as db:
            budget_repository = BudgetRepository(db)
            return budget_repository.read_all_budgets()

    @staticmethod
    def read_budgets_by_currency(currency: str):
        with SessionLocal() as db:
            budget_repository = BudgetRepository(db)
            return budget_repository.read_budgets_by_currency(currency)

    @staticmethod
    def update_budget_is_active(budget_id: str, is_active: bool):
        with SessionLocal() as db:
            try:
                budget_repository = BudgetRepository(db)
                return budget_repository.update_budget_is_active(budget_id, is_active)
            except Exception as e:
                raise e

    @staticmethod
    def update_budget_by_id(budget_id: str,
                            name: str = None,
                            user_id: str = None,
                            category_id: str = None,
                            start_date: str = None,
                            end_date: str = None,
                            currency: str = None,
                            balance: float = None):
        with SessionLocal() as db:
            try:
                budget_repository = BudgetRepository(db)
                return budget_repository.update_budget_by_id(budget_id,
                                                             name,
                                                             user_id,
                                                             category_id,
                                                             start_date,
                                                             end_date,
                                                             currency,
                                                             balance)
            except Exception as e:
                raise e

    @staticmethod
    def delete_budget_by_id(budget_id: str):
        try:
            with SessionLocal() as db:
                budget_repository = BudgetRepository(db)
                return budget_repository.delete_budget_by_id(budget_id)
        except Exception as e:
            raise e
