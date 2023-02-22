"""Categories repositories module."""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.categories.exceprtions import CategoryNotFoundException
from app.categories.models import Category


class CategoryRepository:
    """CategoryRepository class"""
    def __init__(self, db: Session):
        self.db = db

    def create_category(self, name: str, description: str) -> Category:
        """create_category function"""
        try:
            category = Category(name, description)
            self.db.add(category)
            self.db.commit()
            self.db.refresh(category)
            return category
        except IntegrityError as e:
            raise e

    def read_category_by_id(self, category_id: str) -> Category:
        """read_category_by_id function"""
        category = self.db.query(Category).filter(Category.category_id == category_id).first()
        return category

    def read_all_categories(self) -> [Category]:
        """read_all_categories function"""
        categories = self.db.query(Category).all()
        return categories

    def read_category_by_name(self, name: str) -> Category:
        """read_category_by_name function"""
        category = self.db.query(Category).filter(Category.name == name).first()
        return category

    def update_category_is_active(self, category_id: str, is_active: bool) -> Category:
        """update_category_is_active function"""
        try:
            category = self.db.query(Category).filter(Category.category_id == category_id).first()
            category.is_active = is_active
            self.db.add(category)
            self.db.commit()
            self.db.refresh(category)
            return category
        except Exception as e:
            raise e

    def update_category_by_id(self, category_id: str, name: str = None, description: str = None) -> Category:
        """update_category_by_id function"""
        try:
            category = self.db.query(Category).filter(Category.category_id == category_id).first()
            if category is None:
                raise CategoryNotFoundException(f"Category with provided ID: {category_id} not found.", 400)
            if name is not None:
                category.name = name
            if description is not None:
                category.description = description
            self.db.add(category)
            self.db.commit()
            self.db.refresh(category)
            return category
        except Exception as e:
            raise e

    def delete_category_by_id(self, category_id: str) -> bool:
        """delete_category_by_id function"""
        try:
            category = self.db.query(Category).filter(Category.category_id == category_id).first()
            self.db.delete(category)
            self.db.commit()
            return True
        except Exception as e:
            raise e
