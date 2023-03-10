"""Money account services module."""
from app.db import SessionLocal
from app.money_accounts.exceptions import MoneyAccountNotFoundException, CurrencyNotAllowedException
from app.money_accounts.repositiories import MoneyAccountRepository
from app.users.exceptions import UserNotActiveException, UserNotFoundException
from app.users.reporistories import UserRepository

from app.config import settings

CURRENCIES = settings.CURRENCIES.split(",")


class MoneyAccountService:
    """MoneyAccountService class"""
    @staticmethod
    def create_money_account(name: str, user_id: str, currency: str = "DIN",
                             balance: float = 0.0):
        """create_money_account function"""
        with SessionLocal() as db:
            try:
                money_account_repository = MoneyAccountRepository(db)
                user_repository = UserRepository(db)
                user = user_repository.read_user_by_id(user_id)
                if not user:
                    raise UserNotFoundException(message="User not found in the system.", code=404)
                if not user.is_active:
                    raise UserNotActiveException(message="User not active. Activate user to enable role assignment.",
                                                 code=401)
                if currency not in CURRENCIES:
                    raise CurrencyNotAllowedException(message="Currency not allowed. Use DIN or EUR.", code=401)
                return money_account_repository.create_money_account(name, user_id, currency, balance)
            except Exception as e:
                raise e

    @staticmethod
    def read_money_account_by_id(money_account_id: str):
        """read_money_account_by_id function"""
        with SessionLocal() as db:
            money_account_repository = MoneyAccountRepository(db)
            return money_account_repository.read_money_account_by_id(money_account_id)

    @staticmethod
    def read_money_account_by_user_id(user_id: str):
        """read_money_account_by_user_id function"""
        with SessionLocal() as db:
            money_account_repository = MoneyAccountRepository(db)
            return money_account_repository.read_money_account_by_user_id(user_id)

    @staticmethod
    def read_all_money_accounts():
        """read_all_money_accounts function"""
        with SessionLocal() as db:
            money_account_repository = MoneyAccountRepository(db)
            return money_account_repository.read_all_money_accounts()

    @staticmethod
    def read_money_accounts_by_currency(currency: str):
        """read_money_accounts_by_currency function"""
        with SessionLocal() as db:
            try:
                money_account_repository = MoneyAccountRepository(db)
                money_accounts = money_account_repository.read_money_accounts_by_currency(currency)
                if not money_accounts:
                    raise MoneyAccountNotFoundException(message=f"Money account with currency {currency} "
                                                                f"not found in the system.",
                                                        code=404)
                return money_accounts
            except Exception as e:
                raise e

    @staticmethod
    def update_money_account_is_active(money_account_id: str, is_active: bool):
        """update_money_account_is_active function"""
        with SessionLocal() as db:
            try:
                money_account_repository = MoneyAccountRepository(db)
                money_account = money_account_repository.read_money_account_by_id(money_account_id)
                if not money_account:
                    raise MoneyAccountNotFoundException(message="Money account not found in the system.",
                                                        code=404)
                return money_account_repository.update_money_account_is_active(money_account_id, is_active)
            except Exception as e:
                raise e

    @staticmethod
    def update_money_account_by_id(money_account_id: str,
                                   user_id: str = None,
                                   name: str = None,
                                   currency: str = None,
                                   balance: float = None):
        """update_money_account_by_id function"""
        with SessionLocal() as db:
            try:
                money_account_repository = MoneyAccountRepository(db)
                money_account = money_account_repository.read_money_account_by_id(money_account_id)
                if not money_account:
                    raise MoneyAccountNotFoundException(message="Money account not found in the system.",
                                                        code=404)
                if currency and currency not in CURRENCIES:
                    raise CurrencyNotAllowedException(message="Currency not allowed. Use DIN or EUR.", code=401)
                return money_account_repository.update_money_account_by_id(money_account_id,
                                                                           user_id,
                                                                           name,
                                                                           currency,
                                                                           balance)
            except Exception as e:
                raise e

    @staticmethod
    def delete_money_account_by_id(money_account_id: str):
        """delete_money_account_by_id function"""
        try:
            with SessionLocal() as db:
                money_account_repository = MoneyAccountRepository(db)
                money_account = money_account_repository.read_money_account_by_id(money_account_id)
                if not money_account:
                    raise MoneyAccountNotFoundException(message="Money account not found in the system.",
                                                        code=404)
                return money_account_repository.delete_money_account_by_id(money_account_id)
        except Exception as e:
            raise e
