"""Categories module."""
from app.categories.exceprtions import CategoryNotFoundException
from app.categories.repositories import CategoryRepository
from app.db import SessionLocal


class CategoryService:
    """CategoryService class"""
    @staticmethod
    def create_category(name: str, description: str):
        """create_category function"""
        with SessionLocal() as db:
            try:
                category_repository = CategoryRepository(db)
                return category_repository.create_category(name, description)
            except Exception as e:
                raise e

    @staticmethod
    def read_category_by_id(category_id: str):
        """read_category_by_id function"""
        with SessionLocal() as db:
            category_repository = CategoryRepository(db)
            return category_repository.read_category_by_id(category_id)

    @staticmethod
    def read_category_by_name(name: str):
        """read_category_by_name function"""
        with SessionLocal() as db:
            category_repository = CategoryRepository(db)
            return category_repository.read_category_by_name(name)

    @staticmethod
    def read_all_categories():
        """read_all_categories function"""
        with SessionLocal() as db:
            category_repository = CategoryRepository(db)
            return category_repository.read_all_categories()

    @staticmethod
    def update_category_is_active(category_id: str, is_active: bool):
        """update_category_is_active function"""
        with SessionLocal() as db:
            try:
                category_repository = CategoryRepository(db)
                category = category_repository.read_category_by_id(category_id)
                if not category:
                    raise CategoryNotFoundException(message="Category not found in the system.",
                                                    code=404)
                return category_repository.update_category_is_active(category_id, is_active)
            except Exception as e:
                raise e

    @staticmethod
    def update_category_by_id(category_id: str, name: str = None, description: str = None):
        """update_category_by_id function"""
        with SessionLocal() as db:
            try:
                category_repository = CategoryRepository(db)
                category = category_repository.read_category_by_id(category_id)
                if not category:
                    raise CategoryNotFoundException(message="Category not found in the system.",
                                                    code=404)
                return category_repository.update_category_by_id(category_id, name, description)
            except Exception as e:
                raise e

    @staticmethod
    def delete_category_by_id(category_id: str):
        """delete_category_by_id function"""
        try:
            with SessionLocal() as db:
                category_repository = CategoryRepository(db)
                category = category_repository.read_category_by_id(category_id)
                if not category:
                    raise CategoryNotFoundException(message="Category not found in the system.", code=404)
                return category_repository.delete_category_by_id(category_id)
        except Exception as e:
            raise e
