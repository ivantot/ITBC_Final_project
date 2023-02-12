from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.models import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, email, password) -> User:
        try:
            user = User(email, password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def read_user_by_id(self, user_id: str) -> User:
        user = self.db.query(User).filter(User.user_id == user_id).first()
        return user

    def read_all_users(self) -> [User]:
        users = self.db.query(User).all()
        return users

    def read_user_by_email(self, email: str) -> User:
        user = self.db.query(User).filter(User.email == email).first()
        return user

    def update_user_is_active(self, user_id: str, is_active: bool) -> User:
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            user.is_active = is_active
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def delete_user_by_id(self, user_id: str) -> bool:
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            raise e
