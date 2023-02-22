"""Transactions controllers module."""
from fastapi import HTTPException

from app.budgets.exceptions import BudgetNotFoundException, BudgetNotActiveException, TransactionBudgetTimeException
from app.money_accounts.exceptions import MoneyAccountNotFoundException, MoneyAccountNotActiveException, \
    CurrencyNotAllowedException, NotEnoughFundsInMoneyAccountException
from app.transactions.exceptions import TransactionNotFoundException, TransactionCashOnlyException, \
    IllegalParameterException
from app.transactions.services import TransactionService
from app.users.exceptions import UserNotActiveException, UserNotFoundException
from app.vendors.exceptions import VendorNotActiveException, VendorNotFoundException


class TransactionController:
    """TransactionController class"""

    @staticmethod
    def create_transaction(amount: float,
                           user_id: str,
                           vendor_id: str,
                           outbound: bool = True,
                           currency: str = "DIN",
                           cash_payment: bool = True):
        """create_transaction function"""
        try:
            transaction = TransactionService.create_transaction(amount,
                                                                user_id,
                                                                vendor_id,
                                                                outbound,
                                                                currency,
                                                                cash_payment)
            return transaction
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except UserNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except VendorNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except VendorNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except BudgetNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except BudgetNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except MoneyAccountNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except MoneyAccountNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except TransactionCashOnlyException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except CurrencyNotAllowedException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except NotEnoughFundsInMoneyAccountException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except TransactionBudgetTimeException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def read_transaction_by_id(transaction_id: str):
        """read_transaction_by_id function"""
        transaction = TransactionService.read_transaction_by_id(transaction_id)
        if transaction:
            return transaction
        raise HTTPException(status_code=400, detail=f"Transaction with provided id"
                                                    f" {transaction_id} does not exist.")

    @staticmethod
    def read_transactions_by_user_id(user_id: str):
        """read_transactions_by_user_id function"""
        transactions = TransactionService.read_transactions_by_user_id(user_id)
        if transactions:
            return transactions
        raise HTTPException(status_code=400, detail=f"Transactions with provided user id {user_id} do not exist.")

    @staticmethod
    def read_transactions_by_vendor_id(vendor_id: str):
        """read_transactions_by_vendor_id function"""
        transactions = TransactionService.read_transactions_by_vendor_id(vendor_id)
        if transactions:
            return transactions
        raise HTTPException(status_code=400, detail=f"Transactions with provided "
                                                    f"vendor id {vendor_id} do not exist.")

    @staticmethod
    def read_all_transactions():
        """read_all_transactions function"""
        transactions = TransactionService.read_all_transactions()
        return transactions

    @staticmethod
    def update_transaction_is_valid(transaction_id: str, is_valid: bool):
        """update_transaction_is_valid function"""
        try:
            return TransactionService.update_transaction_is_valid(transaction_id, is_valid)
        except TransactionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_transaction_by_id(transaction_id: str):
        """delete_transaction_by_id function"""
        try:
            TransactionService.delete_transaction_by_id(transaction_id)
            return {"message": f"Transaction with provided id, {transaction_id} has been deleted."}
        except TransactionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) from e

    @staticmethod
    def read_transactions_in_time_by_user_id(user_id: str, start_date: str, end_date: str):
        """read_transactions_in_time_by_user_id function"""
        transactions = TransactionService.read_transactions_in_time_by_user_id(user_id, start_date, end_date)
        if transactions:
            return transactions
        if not TransactionService.read_transactions_by_user_id(user_id):
            raise HTTPException(status_code=400, detail=f"Transactions with provided user id {user_id} do not exist.")
        raise HTTPException(status_code=400, detail=f"No transactions between {start_date} and {end_date}.")

    @staticmethod
    def read_spending_habits_by_user_id(user_id: str):
        """read_spending_habits_by_user_id function"""
        transactions = TransactionService.read_spending_habits_by_user_id(user_id)
        if transactions:
            return transactions
        raise HTTPException(status_code=400, detail=f"Transactions with provided user id {user_id} do not exist.")

    @staticmethod
    def read_number_of_transactions_for_vendors_per_category():
        """read_number_of_transactions_for_vendors_per_category function"""
        transactions = TransactionService.read_number_of_transactions_for_vendors_per_category()
        if transactions:
            return transactions
        raise HTTPException(status_code=400, detail="No transactions at all.")

    @staticmethod
    def read_favorite_vendors_per_category():
        """read_favorite_vendors_per_category function"""
        transactions = TransactionService.read_favorite_vendors_per_category()
        if transactions:
            return transactions
        raise HTTPException(status_code=400, detail="No transactions at all.")

    @staticmethod
    def read_favorite_means_of_payment_by_user(user_id: str):
        """read_favorite_means_of_payment_by_user function"""
        transactions = TransactionService.read_favorite_means_of_payment_by_user(user_id)
        if transactions:
            return transactions
        raise HTTPException(status_code=400, detail="No transactions at all.")

    @staticmethod
    def read_inbound_outbound_payments_by_user(user_id: str, transaction_type: str = "outbound"):
        """read_inbound_outbound_payments_by_user function"""
        try:
            return TransactionService.read_inbound_outbound_payments_by_user(user_id, transaction_type)
        except TransactionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except IllegalParameterException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) from e
