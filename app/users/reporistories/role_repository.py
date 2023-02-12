from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.models import Role


class RoleRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_role(self, role_type) -> Role:
        try:
            role = Role(role_type)
            self.db.add(role)
            self.db.commit()
            self.db.refresh(role)
            return role
        except IntegrityError as e:
            raise e

    def read_role_by_id(self, role_id: str) -> Role:
        role = self.db.query(Role).filter(Role.role_id == role_id).first()
        return role

    def read_role_by_type(self, role_type: str) -> Role:
        role = self.db.query(Role).filter(Role.role_type == role_type).first()
        return role

    def read_all_roles(self) -> list[Role]:
        roles = self.db.query(Role).all()
        return roles

    def delete_role_by_id(self, role_id: str) -> bool:
        try:
            role = self.db.query(Role).filter(Role.role_id == role_id).first()
            self.db.delete(role)
            self.db.commit()
            return True
        except Exception as e:
            raise e

