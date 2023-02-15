from fastapi import APIRouter, Depends

from app.money_accounts.controllers import MoneyAccountController
from app.money_accounts.schemas import MoneyAccountSchema, MoneyAccountSchemaIn, MoneyAccountSchemaUpdate
from app.users.controllers.user_auth_controller import JWTBearer

money_account_router = APIRouter(tags=["Money Accounts"], prefix="/api/money_accounts")


@money_account_router.post("/add-new-money_account", response_model=MoneyAccountSchema)
def create_category(money_account: MoneyAccountSchemaIn):
    money_account = MoneyAccountController.create_money_account(money_account.name,
                                                                money_account.user_id,
                                                                money_account.currency,
                                                                money_account.balance)
    return money_account


@money_account_router.get("/id", response_model=MoneyAccountSchema)
def get_money_account_by_id(money_account_id: str):
    return MoneyAccountController.read_money_account_by_id(money_account_id)


@money_account_router.get("/get-money_account-by-user-id", response_model=MoneyAccountSchema)
def get_money_account_by_user_id(user_id: str):
    return MoneyAccountController.read_money_account_by_user_id(user_id)


@money_account_router.get("/get-money_accounts-by-currency", response_model=list[MoneyAccountSchema])
def get_money_accounts_by_currency(currency: str):
    return MoneyAccountController.read_money_accounts_by_currency(currency)


@money_account_router.get("/get-all-money_accounts", response_model=list[MoneyAccountSchema])
def get_all_money_accounts():
    return MoneyAccountController.read_all_money_accounts()


@money_account_router.put("/update/is_active", response_model=MoneyAccountSchema)
def update_money_account_is_active(money_account_id: str, is_active: bool):
    return MoneyAccountController.update_money_account_is_active(money_account_id, is_active)


@money_account_router.put("/update", response_model=MoneyAccountSchema)
def update_money_account_by_id(money_account_id: str, money_account: MoneyAccountSchemaUpdate = None):
    return MoneyAccountController.update_money_account_by_id(money_account_id,
                                                             money_account.name,
                                                             money_account.user_id,
                                                             money_account.currency,
                                                             money_account.balance)


@money_account_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_money_account_by_id(money_account_id: str):
    return MoneyAccountController.delete_money_account_by_id(money_account_id)
