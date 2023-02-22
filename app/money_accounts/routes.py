"""Money accounts module."""
from fastapi import APIRouter, Depends

from app.money_accounts.controllers import MoneyAccountController
from app.money_accounts.schemas import MoneyAccountSchema, MoneyAccountSchemaIn, MoneyAccountSchemaUpdate, \
    MoneyAccountSchemaUpdateIsActive
from app.users.controllers.user_auth_controller import JWTBearer

money_account_router = APIRouter(tags=["Money Accounts"], prefix="/api/money_accounts")


@money_account_router.post("/add-new-money_account", response_model=MoneyAccountSchema,
                           dependencies=[Depends(JWTBearer("USER"))])
def create_money_account(money_account: MoneyAccountSchemaIn):
    """create_money_account route"""
    money_account = MoneyAccountController.create_money_account(money_account.name,
                                                                money_account.user_id,
                                                                money_account.currency,
                                                                money_account.balance)
    return money_account


@money_account_router.get("/id", response_model=MoneyAccountSchema,
                          dependencies=[Depends(JWTBearer("USER"))])
def get_money_account_by_id(money_account_id: str):
    """get_money_account_by_id route"""
    return MoneyAccountController.read_money_account_by_id(money_account_id)


@money_account_router.get("/get-money_account-by-user-id", response_model=MoneyAccountSchema,
                          dependencies=[Depends(JWTBearer("USER"))])
def get_money_account_by_user_id(user_id: str):
    """get_money_account_by_user_id route"""
    return MoneyAccountController.read_money_account_by_user_id(user_id)


@money_account_router.get("/get-money_accounts-by-currency", response_model=list[MoneyAccountSchema],
                          dependencies=[Depends(JWTBearer("ADMIN"))])
def get_money_accounts_by_currency(currency: str):
    """get_money_accounts_by_currency route"""
    return MoneyAccountController.read_money_accounts_by_currency(currency)


@money_account_router.get("/get-all-money_accounts", response_model=list[MoneyAccountSchema],
                          dependencies=[Depends(JWTBearer("ADMIN"))])
def get_all_money_accounts():
    """get_all_money_accounts route"""
    return MoneyAccountController.read_all_money_accounts()


@money_account_router.put("/update/is_active", response_model=MoneyAccountSchema,
                          dependencies=[Depends(JWTBearer("ADMIN"))])
def update_money_account_is_active(money_account: MoneyAccountSchemaUpdateIsActive):
    """update_money_account_is_active route"""
    return MoneyAccountController.update_money_account_is_active(money_account.money_account_id,
                                                                 money_account.is_active)


@money_account_router.put("/update", response_model=MoneyAccountSchema,
                          dependencies=[Depends(JWTBearer("USER"))])
def update_money_account_by_id(money_account_id: str, money_account: MoneyAccountSchemaUpdate = None):
    """update_money_account_by_id route"""
    return MoneyAccountController.update_money_account_by_id(money_account_id,
                                                             money_account.name,
                                                             money_account.user_id,
                                                             money_account.currency,
                                                             money_account.balance)


@money_account_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_money_account_by_id(money_account_id: str):
    """delete_money_account_by_id route"""
    return MoneyAccountController.delete_money_account_by_id(money_account_id)
