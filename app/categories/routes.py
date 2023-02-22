"""Categories module."""
from fastapi import APIRouter, Depends

from app.categories.controllers import CategoryController
from app.categories.schemas import CategorySchema, CategorySchemaIn, CategorySchemaUpdate, CategorySchemaUpdateIsActive
from app.users.controllers.user_auth_controller import JWTBearer

category_router = APIRouter(tags=["Categories"], prefix="/api/categories")


@category_router.post("/add-new-category", response_model=CategorySchema,
                      dependencies=[Depends(JWTBearer("USER"))])
def create_category(category: CategorySchemaIn):
    """create_category route"""
    category = CategoryController.create_category(category.name, category.description)
    return category


@category_router.get("/id", response_model=CategorySchema,
                     dependencies=[Depends(JWTBearer("USER"))])
def get_category_by_id(category_id: str):
    """get_category_by_id route"""
    return CategoryController.read_category_by_id(category_id)


@category_router.get("/get-category-by-name", response_model=CategorySchema,
                     dependencies=[Depends(JWTBearer("USER"))])
def get_category_by_name(name: str):
    """get_category_by_name route"""
    return CategoryController.read_category_by_name(name)


@category_router.get("/get-all-categories", response_model=list[CategorySchema],
                     dependencies=[Depends(JWTBearer("ADMIN"))])
def get_all_categories():
    """get_all_categories route"""
    return CategoryController.read_all_categories()


@category_router.put("/update/is_active", response_model=CategorySchema,
                     dependencies=[Depends(JWTBearer("ADMIN"))])
def update_category_is_active(category: CategorySchemaUpdateIsActive):
    """update_category_is_active route"""
    return CategoryController.update_category_is_active(category.category_id, category.is_active)


@category_router.put("/update", response_model=CategorySchema,
                     dependencies=[Depends(JWTBearer("USER"))])
def update_category_by_id(category_id: str, category: CategorySchemaUpdate = None):
    """update_category_by_id route"""
    return CategoryController.update_category_by_id(category_id,
                                                    category.name,
                                                    category.description)


@category_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_category_by_id(category_id: str):
    """delete_category_by_id route"""
    return CategoryController.delete_category_by_id(category_id)
