"""App module."""
import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.budgets import budget_router
from app.categories import category_router
from app.db import Base, engine
from app.money_accounts import money_account_router
from app.transactions import transaction_router
from app.users import user_router, role_router, admin_router, user_has_role_router
from app.vendors import vendor_router

Base.metadata.create_all(bind=engine)


def init_app():
    """init_app docstring"""
    application = FastAPI()
    application.include_router(admin_router)
    application.include_router(user_router)
    application.include_router(role_router)
    application.include_router(user_has_role_router)
    application.include_router(category_router)
    application.include_router(money_account_router)
    application.include_router(budget_router)
    application.include_router(vendor_router)
    application.include_router(transaction_router)

    return application


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    """hello_world docstring"""
    return RedirectResponse('/docs')


if __name__ == '__main__':
    uvicorn.run(app)
