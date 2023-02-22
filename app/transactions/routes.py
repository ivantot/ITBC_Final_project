"""Transactions module."""
from typing import Tuple
from fastapi import APIRouter, Depends

from app.transactions.controllers import TransactionController
from app.transactions.schemas import TransactionSchema, TransactionSchemaIn, TransactionVendorSchema, \
    TransactionInOutboundSchema, TransactionSchemaUpdateIsValid
from app.users.controllers.user_auth_controller import JWTBearer

transaction_router = APIRouter(tags=["Transactions"], prefix="/api/transactions")


@transaction_router.post("/add-new-transaction", response_model=TransactionSchema,
                         dependencies=[Depends(JWTBearer("USER"))])
def create_transaction(transaction: TransactionSchemaIn):
    """create_transaction route"""
    transaction = TransactionController.create_transaction(amount=transaction.amount,
                                                           user_id=transaction.user_id,
                                                           vendor_id=transaction.vendor_id,
                                                           outbound=transaction.outbound,
                                                           currency=transaction.currency,
                                                           cash_payment=transaction.cash_payment)
    return transaction


@transaction_router.get("/id", response_model=TransactionSchema,
                        dependencies=[Depends(JWTBearer("USER"))])
def get_transaction_by_id(transaction_id: str):
    """get_transaction_by_id route"""
    return TransactionController.read_transaction_by_id(transaction_id)


@transaction_router.get("/get-transactions-by-user-id", response_model=list[TransactionSchema],
                        dependencies=[Depends(JWTBearer("USER"))])
def get_transactions_by_user_id(user_id: str):
    """get_transactions_by_user_id route"""
    return TransactionController.read_transactions_by_user_id(user_id)


@transaction_router.get("/get-transactions-by-vendor-id", response_model=list[TransactionVendorSchema],
                        dependencies=[Depends(JWTBearer("USER"))])
def get_transactions_by_vendor_id(vendor_id: str):
    """get_transactions_by_vendor_id route"""
    return TransactionController.read_transactions_by_vendor_id(vendor_id)


@transaction_router.get("/get-all-transactions", response_model=list[TransactionSchema],
                        dependencies=[Depends(JWTBearer("ADMIN"))])
def get_all_transactions():
    """get_all_transactions route"""
    return TransactionController.read_all_transactions()


@transaction_router.put("/update/is_valid", response_model=TransactionSchema,
                        dependencies=[Depends(JWTBearer("ADMIN"))])
def update_transaction_is_valid(transaction: TransactionSchemaUpdateIsValid):
    """update_transaction_is_valid route"""
    return TransactionController.update_transaction_is_valid(transaction.transaction_id,
                                                             transaction.is_valid)


@transaction_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_transaction_by_id(transaction_id: str):
    """delete_transaction_by_id route"""
    return TransactionController.delete_transaction_by_id(transaction_id)


@transaction_router.get("/get-transactions-in-time-by-user-id", response_model=list[TransactionSchema],
                        dependencies=[Depends(JWTBearer("USER"))])
def get_transactions_in_time_by_user_id(user_id: str, start_date: str, end_date: str):
    """get_transactions_in_time_by_user_id route"""
    return TransactionController.read_transactions_in_time_by_user_id(user_id, start_date, end_date)


@transaction_router.get("/get-spending-habits-user-id", response_model=dict[str, str],
                        dependencies=[Depends(JWTBearer("USER"))])
def get_spending_habits_by_user_id(user_id: str):
    """get_spending_habits_by_user_id route"""
    return TransactionController.read_spending_habits_by_user_id(user_id)


@transaction_router.get("/get-number-of-transactions-for-vendors-per-category",
                        dependencies=[Depends(JWTBearer("USER"))])
def get_number_of_transactions_for_vendors_per_category():
    """get_number_of_transactions_for_vendors_per_category route"""
    return TransactionController.read_number_of_transactions_for_vendors_per_category()


@transaction_router.get("/get-favorite-vendors-per-category",
                        dependencies=[Depends(JWTBearer("USER"))])
def get_favorite_vendors_per_category():
    """get_favorite_vendors_per_category route"""
    return TransactionController.read_favorite_vendors_per_category()


@transaction_router.get("/get-favorite-means-of-payment-by-user",
                        dependencies=[Depends(JWTBearer("USER"))])
def get_favorite_means_of_payment_by_user(user_id: str):
    """get_favorite_means_of_payment_by_user route"""
    return TransactionController.read_favorite_means_of_payment_by_user(user_id)


@transaction_router.get("/get-inbound-outbound-payments-by-user",
                        response_model=Tuple[list[TransactionInOutboundSchema], str],
                        dependencies=[Depends(JWTBearer("USER"))])
def get_inbound_outbound_payments_by_user(user_id: str, transaction_type: str = "outbound"):
    """get_inbound_outbound_payments_by_user route"""
    return TransactionController.read_inbound_outbound_payments_by_user(user_id, transaction_type)
