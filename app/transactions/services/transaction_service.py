import datetime

from app.budgets.exceptions import BudgetNotFoundException, BudgetNotActiveException, TransactionBudgetTimeException
from app.budgets.repositories import BudgetRepository
from app.categories.repositories import CategoryRepository
from app.db import SessionLocal
from app.money_accounts.exceptions import MoneyAccountNotFoundException, MoneyAccountNotActiveException, \
    CurrencyNotAllowedException, NotEnoughFundsInMoneyAccountException
from app.money_accounts.repositiories import MoneyAccountRepository
from app.transactions.exceptions import TransactionNotFoundException, TransactionCashOnlyException
from app.transactions.repositories import TransactionRepository
from app.users.exceptions import UserNotActiveException, UserNotFoundException
from app.users.reporistories import UserRepository
from app.utils import convert_money_by_currency
from app.vendors.exceptions import VendorNotActiveException, VendorNotFoundException
from app.vendors.repositories import VendorRepository

from app.config import settings

CURRENCIES = settings.CURRENCIES.split(",")


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
                category_repository = CategoryRepository(db)
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
                category = category_repository.read_category_by_id(vendor.category_id)
                budgets = budget_repository.read_budgets_by_user_id(user_id)
                budget_categories = []
                for budget in budgets:
                    budget_categories.append(budget.category.category_id)
                    if budget.category_id == vendor.category_id:
                        relevant_budget = budget
                if vendor.category_id not in budget_categories:
                    raise BudgetNotFoundException(message=f"User has no budget for {category.name}. "
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
                if vendor.cash_only and not cash_payment:
                    raise TransactionCashOnlyException(message="Vendor accepts only cash payments, "
                                                               "other means are currently unavailable.",
                                                       code=404)
                if currency not in CURRENCIES:
                    raise CurrencyNotAllowedException(message="Currency not allowed. Use DIN or EUR.", code=401)
                if money_account.currency != currency:
                    money_account_amount = convert_money_by_currency(amount, currency, money_account.currency)
                else:
                    money_account_amount = amount
                if outbound and money_account.balance - money_account_amount < 0:
                    raise NotEnoughFundsInMoneyAccountException(message="Not enough funds in money account. "
                                                                        "Check balance.", code=401)
                if not (relevant_budget.start_date < datetime.datetime.utcnow().date() < relevant_budget.end_date):
                    raise TransactionBudgetTimeException(message="Transaction is not occurring within budget validity "
                                                                 "period. Check budget start and end date.", code=401)
                money_account_repository.update_money_account_by_id(money_account_id=money_account.money_account_id,
                                                                    balance=money_account.balance - money_account_amount
                                                                    if outbound
                                                                    else money_account.balance + money_account_amount)
                if relevant_budget.currency != currency:
                    budget_amount = convert_money_by_currency(amount, currency, relevant_budget.currency)
                else:
                    budget_amount = amount
                budget_repository.update_budget_by_id(budget_id=relevant_budget.budget_id,
                                                      balance=relevant_budget.balance + budget_amount)
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

    @staticmethod
    def read_transactions_in_time_by_user_id(user_id: str, start_date: str, end_date: str):
        with SessionLocal() as db:
            transaction_repository = TransactionRepository(db)
            return transaction_repository.read_transactions_in_time_by_user_id(user_id, start_date, end_date)

    @staticmethod
    def show_spending_habits_by_user_id(user_id: str) -> dict[str, str]:
        with SessionLocal() as db:
            transaction_repository = TransactionRepository(db)
            transactions = transaction_repository.read_transactions_by_user_id(user_id)
            total_spent_by_category = {}
            total_amount_spent = 0
            for transaction in transactions:
                if transaction.outbound:
                    if transaction.currency != "DIN":
                        converted_amount = convert_money_by_currency(transaction.amount, transaction.currency, "DIN")
                    else:
                        converted_amount = transaction.amount
                    if transaction.vendor.category.name not in total_spent_by_category:
                        total_spent_by_category[transaction.vendor.category.name] = converted_amount
                    else:
                        total_spent_by_category[transaction.vendor.category.name] += converted_amount
                    total_amount_spent += converted_amount
            unpacked_spending_habits = {k: str(round((v/total_amount_spent)*100, 2))+"%"
                                        for (k, v) in total_spent_by_category.items()}
            unpacked_spending_habits["total amount spent"] = str(total_amount_spent)+" DIN"
            return unpacked_spending_habits
