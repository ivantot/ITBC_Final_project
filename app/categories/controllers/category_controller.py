"""Categories controllers module."""
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.categories.exceprtions import CategoryNotFoundException
from app.categories.services import CategoryService


class CategoryController:
    """CategoryController class"""
    @staticmethod
    def create_category(name: str, description: str):
        """create_category function"""
        try:
            category = CategoryService.create_category(name, description)
            return category
        except IntegrityError as exc:
            raise HTTPException(status_code=400, detail=f"Category with provided name - {name} already exists.")\
                from exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def read_category_by_id(category_id: str):
        """read_category_by_id function"""
        category = CategoryService.read_category_by_id(category_id)
        if category:
            return category
        raise HTTPException(status_code=400, detail=f"Category with provided id {category_id} does not exist")

    @staticmethod
    def read_category_by_name(name: str):
        """read_category_by_name function"""
        category = CategoryService.read_category_by_name(name)
        if category:
            return category
        raise HTTPException(status_code=400, detail=f"Category with provided name {name} does not exist")

    @staticmethod
    def read_all_categories():
        """read_all_categories function"""
        categories = CategoryService.read_all_categories()
        return categories

    @staticmethod
    def update_category_is_active(category_id: str, is_active: bool):
        """update_category_is_active function"""
        try:
            return CategoryService.update_category_is_active(category_id, is_active)
        except CategoryNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_category_by_id(category_id: str, name: str = None, description: str = None):
        """update_category_by_id function"""
        try:
            return CategoryService.update_category_by_id(category_id, name, description)
        except CategoryNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_category_by_id(category_id: str):
        """delete_category_by_id function"""
        try:
            CategoryService.delete_category_by_id(category_id)
            return {"message": f"Category with provided id, {category_id} has been deleted."}
        except CategoryNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) from e
