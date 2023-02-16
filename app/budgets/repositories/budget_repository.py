from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.budgets.exceptions import BudgetNotFoundException
from app.budgets.models import Budget


class BudgetRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_budget(self,
                      name: str,
                      user_id: str,
                      category_id: str,
                      start_date: str,
                      end_date: str,
                      currency: str = "DIN",
                      balance: float = 0.0) -> Budget:
        try:
            budget = Budget(name,
                            user_id,
                            category_id,
                            start_date,
                            end_date,
                            currency,
                            balance)
            self.db.add(budget)
            self.db.commit()
            self.db.refresh(budget)
            return budget
        except IntegrityError as e:
            raise e

    def read_budget_by_id(self, budget_id: str) -> Budget:
        budget = self.db.query(Budget).filter(Budget.category_id == budget_id).first()
        return budget

    def read_budgets_by_user_id(self, user_id: str) -> [Budget]:
        budgets = self.db.query(Budget).filter(Budget.user_id == user_id).all()
        return budgets

    def read_budgets_by_category_id(self, category_id: str) -> [Budget]:
        budgets = self.db.query(Budget).filter(Budget.category_id == category_id).all()
        return budgets

    def read_all_budgets(self) -> [Budget]:
        budgets = self.db.query(Budget).all()
        return budgets

    def read_budgets_by_currency(self, currency: str) -> [Budget]:
        budgets = self.db.query(Budget).filter(Budget.currency == currency).all()
        return budgets

    def update_budget_is_active(self, budget_id: str, is_active: bool) -> Budget:
        try:
            budget = self.db.query(Budget).filter(Budget.budget_id == budget_id).first()
            budget.is_active = is_active
            self.db.add(budget)
            self.db.commit()
            self.db.refresh(budget)
            return budget
        except Exception as e:
            raise e

    def update_budget_by_id(self, budget_id: str,
                            name: str = None,
                            user_id: str = None,
                            category_id: str = None,
                            start_date: str = None,
                            end_date: str = None,
                            currency: str = None,
                            balance: float = None) -> Budget:
        try:
            budget = self.db.query(Budget).filter(Budget.budget_id == budget_id).first()
            if budget is None:
                raise BudgetNotFoundException(f"Budget with provided ID: {budget_id} not found.", 400)
            if name is not None:
                budget.name = name
            if user_id is not None:
                budget.user_id = user_id
            if category_id is not None:
                budget.category_id = category_id
            if start_date is not None:
                budget.start_date = start_date
            if end_date is not None:
                budget.end_date = end_date
            if currency is not None:
                budget.currency = currency
            if balance is not None:
                budget.balance = balance
            self.db.add(budget)
            self.db.commit()
            self.db.refresh(budget)
            return budget
        except Exception as e:
            raise e

    def delete_budget_by_id(self, budget_id: str) -> bool:
        try:
            budget = self.db.query(Budget).filter(Budget.money_account_id == budget_id).first()
            self.db.delete(budget)
            self.db.commit()
            return True
        except Exception as e:
            raise e