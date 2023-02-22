"""Transactions repositories module."""
from datetime import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.transactions.models import Transaction


class TransactionRepository:
    """TransactionRepository class"""
    def __init__(self, db: Session):
        self.db = db

    def create_transaction(self,
                           amount: float,
                           user_id: str,
                           vendor_id: str,
                           outbound: bool = True,
                           currency: str = "DIN",
                           cash_payment: bool = True) -> Transaction:
        """create_transaction function"""
        try:
            transaction = Transaction(amount,
                                      user_id,
                                      vendor_id,
                                      outbound,
                                      currency,
                                      cash_payment)
            self.db.add(transaction)
            self.db.commit()
            self.db.refresh(transaction)
            return transaction
        except IntegrityError as e:
            raise e

    def read_transaction_by_id(self, transaction_id: str) -> Transaction:
        """read_transaction_by_id function"""
        transaction = self.db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
        return transaction

    def read_transactions_by_user_id(self, user_id: str) -> [Transaction]:
        """read_transactions_by_user_id function"""
        transactions = self.db.query(Transaction).filter(Transaction.user_id == user_id).all()
        return transactions

    def read_transactions_by_vendor_id(self, vendor_id: str) -> [Transaction]:
        """read_transactions_by_vendor_id function"""
        transactions = self.db.query(Transaction).filter(Transaction.vendor_id == vendor_id).all()
        return transactions

    def read_all_transactions(self) -> [Transaction]:
        """read_all_transactions function"""
        transactions = self.db.query(Transaction).all()
        return transactions

    def update_transaction_is_valid(self, transaction_id: str, is_valid: bool) -> Transaction:
        """update_transaction_is_valid function"""
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
        """delete_transaction_by_id function"""
        try:
            transaction = self.db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
            self.db.delete(transaction)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def read_transactions_in_time_by_user_id(self, user_id: str, start_date: str, end_date: str) -> [Transaction]:
        """read_transactions_in_time_by_user_id function"""
        transactions = self.db.query(Transaction).filter(Transaction.user_id == user_id,
                                                         Transaction.transaction_time.between
                                                         (datetime.strptime(start_date, "%Y-%m-%d"),
                                                          datetime.strptime(end_date, "%Y-%m-%d"))).all()
        return transactions
