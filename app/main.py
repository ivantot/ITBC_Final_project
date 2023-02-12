import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db import Base, engine
from app.users.routes import user_router, role_router, admin_router, user_has_role_router

Base.metadata.create_all(bind=engine)


def init_app():
    application = FastAPI()
    application.include_router(admin_router)
    application.include_router(user_router)
    application.include_router(role_router)
    application.include_router(user_has_role_router)

    return application


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    uvicorn.run(app)
