from app.db import SessionLocal
from app.transactions.repositories import TransactionRepository


class TransactionService:

    @staticmethod
    def create_transaction(amount: float,
                           user_id: str,
                           vendor_id: str,
                           outbound: bool = True,
                           currency: str = "DIN"):
        with SessionLocal() as db:
            try:
                transaction_repository = TransactionRepository(db)
                return transaction_repository.create_transaction(amount,
                                                                 user_id,
                                                                 vendor_id,
                                                                 outbound,
                                                                 currency)
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
                return transaction_repository.update_transaction_is_valid(transaction_id, is_valid)
            except Exception as e:
                raise e

    @staticmethod
    def delete_transaction_by_id(transaction_id: str):
        try:
            with SessionLocal() as db:
                transaction_repository = TransactionRepository(db)
                return transaction_repository.delete_transaction_by_id(transaction_id)
        except Exception as e:
            raise e
