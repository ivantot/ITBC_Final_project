from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.transactions.models import Transaction


class TransactionRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_transaction(self,
                           amount: float,
                           user_id: str,
                           vendor_id: str,
                           outbound: bool = True,
                           currency: str = "DIN") -> Transaction:
        try:
            transaction = Transaction(amount,
                                      user_id,
                                      vendor_id,
                                      outbound,
                                      currency)
            self.db.add(transaction)
            self.db.commit()
            self.db.refresh(transaction)
            return transaction
        except IntegrityError as e:
            raise e

    def read_transaction_by_id(self, transaction_id: str) -> Transaction:
        transaction = self.db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
        return transaction

    def read_transactions_by_user_id(self, user_id: str) -> [Transaction]:
        transactions = self.db.query(Transaction).filter(Transaction.user_id == user_id).all()
        return transactions

    def read_transactions_by_vendor_id(self, vendor_id: str) -> [Transaction]:
        transactions = self.db.query(Transaction).filter(Transaction.vendor_id == vendor_id).all()
        return transactions

    def read_all_transactions(self) -> [Transaction]:
        transactions = self.db.query(Transaction).all()
        return transactions

    def update_transaction_is_valid(self, transaction_id: str, is_valid: bool) -> Transaction:
        try:
            transaction = self.db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
            transaction.is_valid = is_valid
            self.db.add(transaction)
            self.db.commit()
            self.db.refresh(transaction)
            return transaction
        except Exception as e:
            raise e

    def delete_transaction_by_id(self, transaction_id: str) -> bool:
        try:
            transaction = self.db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
            self.db.delete(transaction)
            self.db.commit()
            return True
        except Exception as e:
            raise e
