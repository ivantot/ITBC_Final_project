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

    @staticmethod
    def create_transaction(amount: float,
                           user_id: str,
                           vendor_id: str,
                           outbound: bool = True,
                           currency: str = "DIN",
                           cash_payment: bool = True):
        try:
            transaction = TransactionService.create_transaction(amount,
                                                                user_id,
                                                                vendor_id,
                                                                outbound,
                                                                currency,
                                                                cash_payment)
            return transaction
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except VendorNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except VendorNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except BudgetNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except BudgetNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except MoneyAccountNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except MoneyAccountNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except TransactionCashOnlyException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except CurrencyNotAllowedException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except NotEnoughFundsInMoneyAccountException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except TransactionBudgetTimeException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_transaction_by_id(transaction_id: str):
        transaction = TransactionService.read_transaction_by_id(transaction_id)
        if transaction:
            return transaction
        else:
            raise HTTPException(status_code=400, detail=f"Transaction with provided id"
                                                        f" {transaction_id} does not exist.")

    @staticmethod
    def read_transactions_by_user_id(user_id: str):
        transactions = TransactionService.read_transactions_by_user_id(user_id)
        if transactions:
            return transactions
        else:
            raise HTTPException(status_code=400, detail=f"Transactions with provided user id {user_id} do not exist.")

    @staticmethod
    def read_transactions_by_vendor_id(vendor_id: str):
        transactions = TransactionService.read_transactions_by_vendor_id(vendor_id)
        if transactions:
            return transactions
        else:
            raise HTTPException(status_code=400, detail=f"Transactions with provided "
                                                        f"vendor id {vendor_id} do not exist.")

    @staticmethod
    def read_all_transactions():
        transactions = TransactionService.read_all_transactions()
        return transactions

    @staticmethod
    def update_transaction_is_valid(transaction_id: str, is_valid: bool):
        try:
            return TransactionService.update_transaction_is_valid(transaction_id, is_valid)
        except TransactionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_transaction_by_id(transaction_id: str):
        try:
            TransactionService.delete_transaction_by_id(transaction_id)
            return {"message": f"Transaction with provided id, {transaction_id} has been deleted."}
        except TransactionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def read_transactions_in_time_by_user_id(user_id: str, start_date: str, end_date: str):
        transactions = TransactionService.read_transactions_in_time_by_user_id(user_id, start_date, end_date)
        if transactions:
            return transactions
        elif not TransactionService.read_transactions_by_user_id(user_id):
            raise HTTPException(status_code=400, detail=f"Transactions with provided user id {user_id} do not exist.")
        else:
            raise HTTPException(status_code=400, detail=f"No transactions between {start_date} and {end_date}.")

    @staticmethod
    def read_spending_habits_by_user_id(user_id: str):
        transactions = TransactionService.read_spending_habits_by_user_id(user_id)
        if transactions:
            return transactions
        else:
            raise HTTPException(status_code=400, detail=f"Transactions with provided user id {user_id} do not exist.")

    @staticmethod
    def read_number_of_transactions_for_vendors_per_category():
        transactions = TransactionService.read_number_of_transactions_for_vendors_per_category()
        if transactions:
            return transactions
        else:
            raise HTTPException(status_code=400, detail=f"No transactions at all.")

    @staticmethod
    def read_favorite_vendors_per_category():
        transactions = TransactionService.read_favorite_vendors_per_category()
        if transactions:
            return transactions
        else:
            raise HTTPException(status_code=400, detail=f"No transactions at all.")

    @staticmethod
    def read_favorite_means_of_payment_by_user(user_id: str):
        transactions = TransactionService.read_favorite_means_of_payment_by_user(user_id)
        if transactions:
            return transactions
        else:
            raise HTTPException(status_code=400, detail=f"No transactions at all.")

    @staticmethod
    def read_inbound_outbound_payments_by_user(user_id: str, transaction_type: str = "outbound"):
        try:
            return TransactionService.read_inbound_outbound_payments_by_user(user_id, transaction_type)
        except TransactionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IllegalParameterException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
