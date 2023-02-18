from app.budgets.exceptions import BudgetNotFoundException, BudgetNotActiveException
from app.budgets.repositories import BudgetRepository
from app.db import SessionLocal
from app.money_accounts.exceptions import MoneyAccountNotFoundException, MoneyAccountNotActiveException
from app.money_accounts.repositiories import MoneyAccountRepository
from app.transactions.exceptions import TransactionNotFoundException
from app.transactions.repositories import TransactionRepository
from app.users.exceptions import UserNotActiveException, UserNotFoundException
from app.users.reporistories import UserRepository
from app.vendors.exceptions import VendorNotActiveException, VendorNotFoundException
from app.vendors.repositories import VendorRepository


class TransactionService:

    @staticmethod
    def create_transaction(amount: float,
                           user_id: str,
                           vendor_id: str,
                           outbound: bool = True,
                           currency: str = "DIN",
                           cash_payment: bool = True):
        with SessionLocal() as db:
            try:
                transaction_repository = TransactionRepository(db)
                user_repository = UserRepository(db)
                vendor_repository = VendorRepository(db)
                budget_repository = BudgetRepository(db)
                money_account_repository = MoneyAccountRepository(db)
                user = user_repository.read_user_by_id(user_id)
                if not user:
                    raise UserNotFoundException(message="User not found in the system.", code=404)
                if not user.is_active:
                    raise UserNotActiveException(message="User not active. Activate user to enable "
                                                         "transaction assignment.", code=401)
                vendor = vendor_repository.read_vendor_by_id(vendor_id)
                if not vendor:
                    raise VendorNotFoundException(message="Vendor not found in the system.", code=404)
                if not vendor.is_active:
                    raise VendorNotActiveException(message="Vendor not active. Activate vendor to enable "
                                                           "transaction assignment.", code=401)
                budgets = budget_repository.read_budgets_by_user_id(user_id)
                budget_categories = []
                for budget in budgets:
                    budget_categories.append(budget.category.category_id)
                    if budget.category_id == vendor.category_id:
                        relevant_budget = budget
                if vendor.category_id not in budget_categories:
                    raise BudgetNotFoundException(message="User has no budget for selected category. "
                                                          "Create a budget.", code=404)
                if not relevant_budget.is_active:
                    raise BudgetNotActiveException(message="Budget not active. Activate budget to enable "
                                                           "transaction assignment.", code=401)
                money_account = money_account_repository.read_money_account_by_user_id(user_id)
                if not money_account:
                    raise MoneyAccountNotFoundException(message="Money account not found for the user. "
                                                                "Create money account to enable transactions.",
                                                        code=404)
                if not money_account.is_active:
                    raise MoneyAccountNotActiveException(message="Money account not active. Activate money account"
                                                                 " to enable transaction assignment.", code=401)
                return transaction_repository.create_transaction(amount,
                                                                 user_id,
                                                                 vendor_id,
                                                                 outbound,
                                                                 currency,
                                                                 cash_payment)
            except Exception as e:
                raise e

    @staticmethod
    def read_transaction_by_id(transaction_id: str):
        with SessionLocal() as db:
            transaction_repository = TransactionRepository(db)
            return transaction_repository.read_transaction_by_id(transaction_id)

    @staticmethod
    def read_transactions_by_user_id(user_id: str):
        with SessionLocal() as db:
            transaction_repository = TransactionRepository(db)
            return transaction_repository.read_transactions_by_user_id(user_id)

    @staticmethod
    def read_transactions_by_vendor_id(vendor_id: str):
        with SessionLocal() as db:
            transaction_repository = TransactionRepository(db)
            return transaction_repository.read_transactions_by_vendor_id(vendor_id)

    @staticmethod
    def read_all_transactions():
        with SessionLocal() as db:
            transaction_repository = TransactionRepository(db)
            return transaction_repository.read_all_transactions()

    @staticmethod
    def update_transaction_is_valid(transaction_id: str, is_valid: bool):
        with SessionLocal() as db:
            try:
                transaction_repository = TransactionRepository(db)
                transaction = transaction_repository.read_transaction_by_id(transaction_id)
                if not transaction:
                    raise TransactionNotFoundException(message="Transaction not found in the system.",
                                                       code=404)
                return transaction_repository.update_transaction_is_valid(transaction_id, is_valid)
            except Exception as e:
                raise e

    @staticmethod
    def delete_transaction_by_id(transaction_id: str):
        try:
            with SessionLocal() as db:
                transaction_repository = TransactionRepository(db)
                transaction = transaction_repository.read_transaction_by_id(transaction_id)
                if not transaction:
                    raise TransactionNotFoundException(message="Transaction not found in the system.",
                                                       code=404)
                return transaction_repository.delete_transaction_by_id(transaction_id)
        except Exception as e:
            raise e
