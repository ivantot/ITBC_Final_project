"""Money account controllers module."""
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.money_accounts.exceptions import MoneyAccountNotFoundException, CurrencyNotAllowedException
from app.money_accounts.services import MoneyAccountService
from app.users.exceptions import UserNotActiveException, UserNotFoundException


class MoneyAccountController:
    """MoneyAccountController class"""

    @staticmethod
    def create_money_account(name: str, user_id: str, currency: str = "DIN",
                             balance: float = 0.0):
        """create_money_account function"""
        try:
            money_account = MoneyAccountService.create_money_account(name, user_id, currency, balance)
            return money_account
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except UserNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except CurrencyNotAllowedException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except IntegrityError as exc:
            raise HTTPException(status_code=400, detail=f"Money account with provided user id - {user_id} already "
                                                        f"exists.") from exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def read_money_account_by_id(money_account_id: str):
        """read_money_account_by_id function"""
        money_account = MoneyAccountService.read_money_account_by_id(money_account_id)
        if money_account:
            return money_account
        raise HTTPException(status_code=400, detail=f"Money account with provided id {money_account_id} does not "
                                                    f"exist.")

    @staticmethod
    def read_money_account_by_user_id(user_id: str):
        """read_money_account_by_user_id function"""
        money_account = MoneyAccountService.read_money_account_by_user_id(user_id)
        if money_account:
            return money_account
        raise HTTPException(status_code=400, detail=f"Money account with provided user id {user_id} does "
                                                    f"not exist.")

    @staticmethod
    def read_money_accounts_by_currency(currency: str):
        """read_money_accounts_by_currency function"""
        try:
            money_account = MoneyAccountService.read_money_accounts_by_currency(currency)
            return money_account
        except MoneyAccountNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) from e

    @staticmethod
    def read_all_money_accounts():
        """read_all_money_accounts function"""
        money_accounts = MoneyAccountService.read_all_money_accounts()
        return money_accounts

    @staticmethod
    def update_money_account_is_active(money_account_id: str, is_active: bool):
        """update_money_account_is_active function"""
        try:
            return MoneyAccountService.update_money_account_is_active(money_account_id, is_active)
        except MoneyAccountNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_money_account_by_id(money_account_id: str,
                                   user_id: str = None,
                                   name: str = None,
                                   currency: str = None,
                                   balance: float = None):
        """update_money_account_by_id function"""
        try:
            return MoneyAccountService.update_money_account_by_id(money_account_id,
                                                                  user_id,
                                                                  name,
                                                                  currency,
                                                                  balance)
        except CurrencyNotAllowedException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except MoneyAccountNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_money_account_by_id(money_account_id: str):
        """delete_money_account_by_id function"""
        try:
            MoneyAccountService.delete_money_account_by_id(money_account_id)
            return {"message": f"Money account with provided id, {money_account_id} has been deleted."}
        except MoneyAccountNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) from e
