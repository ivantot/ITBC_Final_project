from app.budgets.exceptions import BudgetNotFoundException, StartAfterEndDateException, \
    ActiveBudgetForCategoryExistsException
from app.budgets.repositories import BudgetRepository
from app.categories.exceprtions import CategoryNotActiveException, CategoryNotFoundException
from app.categories.repositories import CategoryRepository
from app.db import SessionLocal
from app.money_accounts.exceptions import CurrencyNotAllowedException
from app.users.exceptions import UserNotActiveException, UserNotFoundException
from app.users.reporistories import UserRepository

from app.config import settings

CURRENCIES = settings.CURRENCIES.split(",")


class BudgetService:

    @staticmethod
    def create_budget(name: str,
                      user_id: str,
                      category_id: str,
                      start_date: str,
                      end_date: str,
                      limit: float,
                      currency: str = "DIN",
                      balance: float = 0.0):
        with SessionLocal() as db:
            try:
                budget_repository = BudgetRepository(db)
                user_repository = UserRepository(db)
                category_repository = CategoryRepository(db)
                user = user_repository.read_user_by_id(user_id)
                if not user:
                    raise UserNotFoundException(message="User not found in the system.", code=404)
                if not user.is_active:
                    raise UserNotActiveException(message="User not active. Activate user to enable budget assignment.",
                                                 code=401)
                category = category_repository.read_category_by_id(category_id)
                if not category:
                    raise CategoryNotFoundException(message="Category not found in the system.", code=404)
                if not category.is_active:
                    raise CategoryNotActiveException(message="Category not active. Activate category to enable "
                                                             "budget assignment.", code=401)
                users_budgets = budget_repository.read_budgets_by_user_id(user_id)
                for budget in users_budgets:
                    if budget.category_id == category_id:
                        if budget.is_active:
                            raise ActiveBudgetForCategoryExistsException(message="Active budget for selected category"
                                                                                 "already exists. Deactivate and create"
                                                                                 "new budget, or use existing.",
                                                                         code=401)
                if start_date > end_date:
                    raise StartAfterEndDateException(message="Start date must be before end date.", code=401)
                if currency not in CURRENCIES:
                    raise CurrencyNotAllowedException(message="Currency not allowed. Use DIN or EUR.", code=401)
                return budget_repository.create_budget(name,
                                                       user_id,
                                                       category_id,
                                                       start_date,
                                                       end_date,
                                                       limit,
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
                budget = budget_repository.read_budget_by_id(budget_id)
                if not budget:
                    raise BudgetNotFoundException(message="Budget not found in the system.",
                                                  code=404)
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
                            limit: float = None,
                            balance: float = None):
        with SessionLocal() as db:
            try:
                budget_repository = BudgetRepository(db)
                budget = budget_repository.read_budget_by_id(budget_id)
                if not budget:
                    raise BudgetNotFoundException(message="Budget not found in the system.", code=404)
                if currency and currency not in CURRENCIES:
                    raise CurrencyNotAllowedException(message="Currency not allowed. Use DIN or EUR.", code=401)
                return budget_repository.update_budget_by_id(budget_id=budget_id,
                                                             name=name,
                                                             user_id=user_id,
                                                             category_id=category_id,
                                                             start_date=start_date,
                                                             end_date=end_date,
                                                             currency=currency,
                                                             limit=limit,
                                                             balance=balance)
            except Exception as e:
                raise e

    @staticmethod
    def delete_budget_by_id(budget_id: str):
        try:
            with SessionLocal() as db:
                budget_repository = BudgetRepository(db)
                budget = budget_repository.read_budget_by_id(budget_id)
                if not budget:
                    raise BudgetNotFoundException(message="Budget not found in the system.",
                                                  code=404)
                return budget_repository.delete_budget_by_id(budget_id)
        except Exception as e:
            raise e
