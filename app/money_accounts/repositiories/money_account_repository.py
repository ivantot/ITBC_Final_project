"""Money account repositories module."""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.money_accounts.exceptions import MoneyAccountNotFoundException
from app.money_accounts.models import MoneyAccount


class MoneyAccountRepository:
    """MoneyAccountRepository class"""
    def __init__(self, db: Session):
        self.db = db

    def create_money_account(self, name: str, user_id: str, currency: str = "DIN",
                             balance: float = 0.0) -> MoneyAccount:
        """create_money_account function"""
        try:
            money_account = MoneyAccount(name, user_id, currency, balance)
            self.db.add(money_account)
            self.db.commit()
            self.db.refresh(money_account)
            return money_account
        except IntegrityError as e:
            raise e

    def read_money_account_by_id(self, money_account_id: str) -> MoneyAccount:
        """read_money_account_by_id function"""
        money_account = self.db.query(MoneyAccount).filter(MoneyAccount.money_account_id == money_account_id).first()
        return money_account

    def read_money_account_by_user_id(self, user_id: str) -> MoneyAccount:
        """read_money_account_by_user_id function"""
        money_account = self.db.query(MoneyAccount).filter(MoneyAccount.user_id == user_id).first()
        return money_account

    def read_all_money_accounts(self) -> [MoneyAccount]:
        """read_all_money_accounts function"""
        money_accounts = self.db.query(MoneyAccount).all()
        return money_accounts

    def read_money_accounts_by_currency(self, currency: str) -> [MoneyAccount]:
        """read_money_accounts_by_currency function"""
        money_accounts = self.db.query(MoneyAccount).filter(MoneyAccount.currency == currency).all()
        return money_accounts

    def update_money_account_is_active(self, money_account_id: str, is_active: bool) -> MoneyAccount:
        """update_money_account_is_active function"""
        try:
            money_account = self.db.query(MoneyAccount).filter(
                MoneyAccount.money_account_id == money_account_id).first()
            money_account.is_active = is_active
            self.db.add(money_account)
            self.db.commit()
            self.db.refresh(money_account)
            return money_account
        except Exception as e:
            raise e

    def update_money_account_by_id(self, money_account_id: str,
                                   user_id: str = None,
                                   name: str = None,
                                   currency: str = None,
                                   balance: float = None) -> MoneyAccount:
        """update_money_account_by_id function"""
        try:
            money_account = self.db.query(MoneyAccount).filter(
                MoneyAccount.money_account_id == money_account_id).first()
            if money_account is None:
                raise MoneyAccountNotFoundException(f"Money account with provided ID: {money_account_id} not found.",
                                                    400)
            if user_id is not None:
                money_account.user_id = user_id
            if name is not None:
                money_account.name = name
            if currency is not None:
                money_account.currency = currency
            if balance is not None:
                money_account.balance = balance
            self.db.add(money_account)
            self.db.commit()
            self.db.refresh(money_account)
            return money_account
        except Exception as e:
            raise e

    def delete_money_account_by_id(self, money_account_id: str) -> bool:
        """delete_money_account_by_id function"""
        try:
            money_account = self.db.query(MoneyAccount).filter(
                MoneyAccount.money_account_id == money_account_id).first()
            self.db.delete(money_account)
            self.db.commit()
            return True
        except Exception as e:
            raise e
