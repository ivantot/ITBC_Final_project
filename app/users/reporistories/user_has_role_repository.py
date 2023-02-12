from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.models import UserHasRole, User


class UserHasRoleRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user_has_role(self, user_id: str, role_id: str) -> UserHasRole:
        try:
            user_has_role = UserHasRole(user_id, role_id)
            self.db.add(user_has_role)
            self.db.commit()
            self.db.refresh(user_has_role)
            return user_has_role
        except IntegrityError as e:
            raise e

    def read_user_has_role_by_id(self, user_has_role_id: str) -> UserHasRole:
        user_has_role = self.db.query(UserHasRole).filter(UserHasRole.user_has_role_id == user_has_role_id).first()
        return user_has_role

    def read_user_has_roles_by_user_id(self, user_id: str) -> list[UserHasRole]:
        user_has_roles = self.db.query(UserHasRole).filter(UserHasRole.user_id == user_id).all()
        return user_has_roles

    def delete_user_has_role_by_id(self, user_has_role_id: str) -> bool:
        try:
            user_has_role = self.db.query(UserHasRole).filter(UserHasRole.user_has_role_id == user_has_role_id).first()
            self.db.delete(user_has_role)
            self.db.commit()
            return True
        except Exception as e:
            raise e
