from app.db import SessionLocal
from app.money_accounts.repositiories import MoneyAccountRepository


class MoneyAccountService:

    @staticmethod
    def create_money_account(name: str, user_id: str, currency: str = "DIN",
                             balance: float = 0.0):
        with SessionLocal() as db:
            try:
                money_account_repository = MoneyAccountRepository(db)
                return money_account_repository.create_money_account(name, user_id, currency, balance)
            except Exception as e:
                raise e

    @staticmethod
    def read_money_account_by_id(money_account_id: str):
        with SessionLocal() as db:
            money_account_repository = MoneyAccountRepository(db)
            return money_account_repository.read_money_account_by_id(money_account_id)

    @staticmethod
    def read_money_account_by_user_id(user_id: str):
        with SessionLocal() as db:
            money_account_repository = MoneyAccountRepository(db)
            return money_account_repository.read_money_account_by_user_id(user_id)

    @staticmethod
    def read_all_money_accounts():
        with SessionLocal() as db:
            money_account_repository = MoneyAccountRepository(db)
            return money_account_repository.read_all_money_accounts()

    @staticmethod
    def read_money_accounts_by_currency(currency: str):
        with SessionLocal() as db:
            money_account_repository = MoneyAccountRepository(db)
            return money_account_repository.read_money_accounts_by_currency(currency)

    @staticmethod
    def update_money_account_is_active(money_account_id: str, is_active: bool):
        with SessionLocal() as db:
            try:
                money_account_repository = MoneyAccountRepository(db)
                return money_account_repository.update_money_account_is_active(money_account_id, is_active)
            except Exception as e:
                raise e

    @staticmethod
    def update_money_account_by_id(money_account_id: str,
                                   user_id: str = None,
                                   name: str = None,
                                   currency: str = None,
                                   balance: float = None):
        with SessionLocal() as db:
            try:
                money_account_repository = MoneyAccountRepository(db)
                return money_account_repository.update_money_account_by_id(money_account_id,
                                                                           user_id,
                                                                           name,
                                                                           currency,
                                                                           balance)
            except Exception as e:
                raise e

    @staticmethod
    def delete_money_account_by_id(money_account_id: str):
        try:
            with SessionLocal() as db:
                money_account_repository = MoneyAccountRepository(db)
                return money_account_repository.delete_money_account_by_id(money_account_id)
        except Exception as e:
            raise e
