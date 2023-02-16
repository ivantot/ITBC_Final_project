from fastapi import HTTPException

from app.transactions.services import TransactionService


class TransactionController:

    @staticmethod
    def create_transaction(amount: float,
                           user_id: str,
                           vendor_id: str,
                           outbound: bool = True,
                           currency: str = "DIN"):
        try:
            transaction = TransactionService.create_transaction(amount,
                                                                user_id,
                                                                vendor_id,
                                                                outbound,
                                                                currency)
            return transaction
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
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_transaction_by_id(transaction_id: str):
        try:
            TransactionService.delete_transaction_by_id(transaction_id)
            return {"message": f"Transaction with provided id, {transaction_id} has been deleted."}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))