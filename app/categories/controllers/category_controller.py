from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.categories.services import CategoryServices


class CategoryController:

    @staticmethod
    def create_category(name: str, description: str):
        try:
            category = CategoryServices.create_category(name, description)
            return category
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Category with provided name - {name} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_category_by_id(category_id: str):
        category = CategoryServices.read_category_by_id(category_id)
        if category:
            return category
        else:
            raise HTTPException(status_code=400, detail=f"Category with provided id {category_id} does not exist")

    @staticmethod
    def read_category_by_name(name: str):
        category = CategoryServices.read_category_by_name(name)
        if category:
            return category
        else:
            raise HTTPException(status_code=400, detail=f"Category with provided name {name} does not exist")

    @staticmethod
    def read_all_categories():
        categories = CategoryServices.read_all_categories()
        return categories

    @staticmethod
    def update_category_is_active(category_id: str, is_active: bool):
        try:
            return CategoryServices.update_category_is_active(category_id, is_active)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_category_by_id(category_id: str, name: str = None, description: str = None):
        try:
            return CategoryServices.update_category_by_id(category_id, name, description)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_category_by_id(category_id: str):
        try:
            CategoryServices.delete_category_by_id(category_id)
            return {"message": f"Category with provided id, {category_id} has been deleted."}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
