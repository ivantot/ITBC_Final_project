"""Transactions services module."""
import datetime

from app.budgets.exceptions import BudgetNotFoundException, BudgetNotActiveException, TransactionBudgetTimeException
from app.budgets.repositories import BudgetRepository
from app.categories.repositories import CategoryRepository
from app.db import SessionLocal
from app.money_accounts.exceptions import MoneyAccountNotFoundException, MoneyAccountNotActiveException, \
    CurrencyNotAllowedException, NotEnoughFundsInMoneyAccountException
from app.money_accounts.repositiories import MoneyAccountRepository
from app.transactions.exceptions import TransactionNotFoundException, TransactionCashOnlyException, \
    IllegalParameterException
from app.transactions.repositories import TransactionRepository
from app.users.exceptions import UserNotActiveException, UserNotFoundException
from app.users.reporistories import UserRepository
from app.utils import convert_money_by_currency, EmailServices
from app.vendors.exceptions import VendorNotActiveException, VendorNotFoundException
from app.vendors.repositories import VendorRepository

from app.config import settings

CURRENCIES = settings.CURRENCIES.split(",")


class TransactionService:
    """TransactionService class"""

    @staticmethod
    def create_transaction(amount: float,
                           user_id: str,
                           vendor_id: str,
                           outbound: bool = True,
                           currency: str = "DIN",
                           cash_payment: bool = True):
        """create_transaction function"""
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
                    EmailServices.send_money_account_warning_email(email=user.email,
                                                                   amount=round(amount, 2),
                                                                   vendor_name=vendor.name,
                                                                   transaction_currency=currency,
                                                                   balance=round(money_account.balance, 2),
                                                                   money_account_currency=money_account.currency,
                                                                   user=user.email)
                    raise NotEnoughFundsInMoneyAccountException(message="Not enough funds in money account. "
                                                                        "Check balance.", code=401)
                if not relevant_budget.start_date < datetime.datetime.utcnow().date() < relevant_budget.end_date:
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
        """read_transaction_by_id function"""
        with SessionLocal() as db:
            transaction_repository = TransactionRepository(db)
            return transaction_repository.read_transaction_by_id(transaction_id)

    @staticmethod
    def read_transactions_by_user_id(user_id: str):
        """read_transactions_by_user_id function"""
        with SessionLocal() as db:
            transaction_repository = TransactionRepository(db)
            return transaction_repository.read_transactions_by_user_id(user_id)

    @staticmethod
    def read_transactions_by_vendor_id(vendor_id: str):
        """read_transactions_by_vendor_id function"""
        with SessionLocal() as db:
            transaction_repository = TransactionRepository(db)
            return transaction_repository.read_transactions_by_vendor_id(vendor_id)

    @staticmethod
    def read_all_transactions():
        """read_all_transactions function"""
        with SessionLocal() as db:
            transaction_repository = TransactionRepository(db)
            return transaction_repository.read_all_transactions()

    @staticmethod
    def update_transaction_is_valid(transaction_id: str, is_valid: bool):
        """update_transaction_is_valid function"""
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
        """delete_transaction_by_id function"""
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
        """read_transactions_in_time_by_user_id function"""
        with SessionLocal() as db:
            transaction_repository = TransactionRepository(db)
            return transaction_repository.read_transactions_in_time_by_user_id(user_id, start_date, end_date)

    @staticmethod
    def read_spending_habits_by_user_id(user_id: str) -> dict[str, str]:
        """read_spending_habits_by_user_id function"""
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
            unpacked_spending_habits = {k: str(round((v / total_amount_spent) * 100, 2)) + "%"
                                        for (k, v) in total_spent_by_category.items()}
            unpacked_spending_habits["total amount spent"] = str(total_amount_spent) + " DIN"
            return unpacked_spending_habits

    @staticmethod
    def read_number_of_transactions_for_vendors_per_category():
        """read_number_of_transactions_for_vendors_per_category function"""
        with SessionLocal() as db:
            transaction_repository = TransactionRepository(db)
            category_repository = CategoryRepository(db)
            vendor_repository = VendorRepository(db)
            categories = category_repository.read_all_categories()
            transactions = transaction_repository.read_all_transactions()
            vendors = vendor_repository.read_all_vendors()
            transactions_by_vendor = {}
            favorite_by_category = {}
            for vendor in vendors:
                transactions_by_vendor[vendor.name] = 0
                for transaction in transactions:
                    if transaction.vendor.name == vendor.name:
                        transactions_by_vendor[vendor.name] += 1
            for category in categories:
                favorite_by_category[category.name] = []
                for vendor in transactions_by_vendor:
                    vendor_obj = vendor_repository.read_vendor_by_name(vendor)
                    if vendor_obj.category.name == category.name:
                        favorite_by_category[category.name].append((vendor_obj.name,
                                                                    transactions_by_vendor[vendor]))
            return favorite_by_category

    @staticmethod
    def read_favorite_vendors_per_category():
        """read_favorite_vendors_per_category function"""
        data = TransactionService().read_number_of_transactions_for_vendors_per_category()
        for category in data:
            data[category].sort(key=lambda x: x[1], reverse=True)
            data[category] = data[category][0][0]
        return data

    @staticmethod
    def read_favorite_means_of_payment_by_user(user_id: str):
        """read_favorite_means_of_payment_by_user function"""
        with SessionLocal() as db:
            transaction_repository = TransactionRepository(db)
            transactions = transaction_repository.read_transactions_by_user_id(user_id)
            means_of_payment = {"cash": 0, "non-cash": 0}
            for transaction in transactions:
                if transaction.cash_payment:
                    means_of_payment["cash"] += 1
                else:
                    means_of_payment["non-cash"] += 1
            return means_of_payment

    @staticmethod
    def read_inbound_outbound_payments_by_user(user_id: str, transaction_type: str = "outbound"):
        """read_inbound_outbound_payments_by_user function"""
        with SessionLocal() as db:
            transaction_repository = TransactionRepository(db)
            transactions = transaction_repository.read_transactions_by_user_id(user_id)
            inbound_transactions = []
            inbound_counter = 0
            outbound_transactions = []
            outbound_counter = 0
            for transaction in transactions:
                if transaction.outbound:
                    outbound_transactions.append(transaction)
                    outbound_counter += 1
                else:
                    inbound_transactions.append(transaction)
                    inbound_counter += 1
            if transaction_type == "outbound":
                if not outbound_transactions:
                    raise TransactionNotFoundException(message="No outbound transactions found in the system.",
                                                       code=404)
                return outbound_transactions, f"User made {outbound_counter} outbound transactions."
            if transaction_type == "inbound":
                if not inbound_transactions:
                    raise TransactionNotFoundException(message="No inbound transactions found in the system.",
                                                       code=404)
                return inbound_transactions, f"User made {inbound_counter} inbound transactions."
            raise IllegalParameterException(message="Only inbound and outbound available as transaction type.",
                                            code=401)
