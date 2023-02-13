from fastapi import APIRouter, Depends

from app.categories.controllers import CategoryController
from app.categories.schemas import CategorySchema, CategorySchemaIn, CategorySchemaUpdate
from app.users.controllers.user_auth_controller import JWTBearer

category_router = APIRouter(tags=["Categories"], prefix="/api/categories")


@category_router.post("/add-new-category", response_model=CategorySchema)
def create_category(category: CategorySchemaIn):
    category = CategoryController.create_category(category.name, category.description)
    return category


@category_router.get("/id", response_model=CategorySchema)
def get_category_by_id(category_id: str):
    return CategoryController.read_category_by_id(category_id)


@category_router.get("/get-category-by-name", response_model=CategorySchema)
def get_category_by_name(name: str):
    return CategoryController.read_category_by_name(name)


@category_router.get("/get-all-categories", response_model=list[CategorySchema])
def get_all_categories():
    return CategoryController.read_all_categories()


@category_router.put("/update/is_active", response_model=CategorySchema)
def update_category_is_active(category_id: str, is_active: bool):
    return CategoryController.update_category_is_active(category_id, is_active)


@category_router.put("/update", response_model=CategorySchema)
def update_category_by_id(category_id, name, description):
    return CategoryController.update_category_by_id(category_id,
                                                    name,
                                                    description)


@category_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_category_by_id(category_id: str):
    return CategoryController.delete_category_by_id(category_id)
