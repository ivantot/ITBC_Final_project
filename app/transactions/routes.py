from fastapi import APIRouter, Depends

from app.transactions.controllers import TransactionController
from app.transactions.schemas import TransactionSchema, TransactionSchemaIn
from app.users.controllers.user_auth_controller import JWTBearer

transaction_router = APIRouter(tags=["Transactions"], prefix="/api/transactions")


@transaction_router.post("/add-new-transaction", response_model=TransactionSchema)
def create_vendor(transaction: TransactionSchemaIn):
    transaction = TransactionController.create_transaction(transaction.amount,
                                                           transaction.user_id,
                                                           transaction.vendor_id,
                                                           transaction.outbound,
                                                           transaction.currency,
                                                           transaction.cash_payment)
    return transaction


@transaction_router.get("/id", response_model=TransactionSchema)
def get_transaction_by_id(transaction_id: str):
    return TransactionController.read_transaction_by_id(transaction_id)


@transaction_router.get("/get-transactions-by-user-id", response_model=list[TransactionSchema])
def get_transactions_by_user_id(user_id: str):
    return TransactionController.read_transactions_by_user_id(user_id)


@transaction_router.get("/get-transactions-by-vendor-id", response_model=list[TransactionSchema])
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
