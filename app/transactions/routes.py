from typing import Tuple
from fastapi import APIRouter, Depends

from app.transactions.controllers import TransactionController
from app.transactions.schemas import TransactionSchema, TransactionSchemaIn, TransactionVendorSchema, \
    TransactionInOutboundSchema
from app.users.controllers.user_auth_controller import JWTBearer

transaction_router = APIRouter(tags=["Transactions"], prefix="/api/transactions")


@transaction_router.post("/add-new-transaction", response_model=TransactionSchema)
def create_vendor(transaction: TransactionSchemaIn):
    transaction = TransactionController.create_transaction(amount=transaction.amount,
                                                           user_id=transaction.user_id,
                                                           vendor_id=transaction.vendor_id,
                                                           outbound=transaction.outbound,
                                                           currency=transaction.currency,
                                                           cash_payment=transaction.cash_payment)
    return transaction


@transaction_router.get("/id", response_model=TransactionSchema)
def get_transaction_by_id(transaction_id: str):
    return TransactionController.read_transaction_by_id(transaction_id)


@transaction_router.get("/get-transactions-by-user-id", response_model=list[TransactionSchema])
def get_transactions_by_user_id(user_id: str):
    return TransactionController.read_transactions_by_user_id(user_id)


@transaction_router.get("/get-transactions-by-vendor-id", response_model=list[TransactionVendorSchema])
def get_transactions_by_vendor_id(vendor_id: str):
    return TransactionController.read_transactions_by_vendor_id(vendor_id)


@transaction_router.get("/get-all-transactions", response_model=list[TransactionSchema])
def get_all_transactions():
    return TransactionController.read_all_transactions()


@transaction_router.put("/update/is_valid", response_model=TransactionSchema)
def update_transaction_is_valid(transaction_id: str, is_valid: bool):
    return TransactionController.update_transaction_is_valid(transaction_id, is_valid)


@transaction_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_transaction_by_id(transaction_id: str):
    return TransactionController.delete_transaction_by_id(transaction_id)


@transaction_router.get("/get-transactions-in-time-by-user-id", response_model=list[TransactionSchema])
def get_transactions_in_time_by_user_id(user_id: str, start_date: str, end_date: str):
    return TransactionController.read_transactions_in_time_by_user_id(user_id, start_date, end_date)


@transaction_router.get("/get-spending-habits-user-id", response_model=dict[str, str])
def get_spending_habits_by_user_id(user_id: str):
    return TransactionController.read_spending_habits_by_user_id(user_id)


@transaction_router.get("/get-number-of-transactions-for-vendors-per-category")
def get_number_of_transactions_for_vendors_per_category():
    return TransactionController.read_number_of_transactions_for_vendors_per_category()


@transaction_router.get("/get-favorite-vendors-per-category")
def get_favorite_vendors_per_category():
    return TransactionController.read_favorite_vendors_per_category()


@transaction_router.get("/get-favorite-means-of-payment-by-user")
def get_favorite_means_of_payment_by_user(user_id: str):
    return TransactionController.read_favorite_means_of_payment_by_user(user_id)


@transaction_router.get("/get-inbound-outbound-payments-by-user",
                        response_model=Tuple[list[TransactionInOutboundSchema], str])
def get_inbound_outbound_payments_by_user(user_id: str, transaction_type: str = "outbound"):
    return TransactionController.read_inbound_outbound_payments_by_user(user_id, transaction_type)
