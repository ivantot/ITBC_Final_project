"""Users services module."""
from app.db import SessionLocal
from app.users.exceptions.role_exceptions import RoleNotFoundException
from app.users.reporistories import RoleRepository


class RoleService:
    """RoleService class"""
    @staticmethod
    def create_role(role_type: str):
        """create_role function"""
        with SessionLocal() as db:
            try:
                role_repository = RoleRepository(db)
                return role_repository.create_role(role_type)
            except Exception as e:
                raise e

    @staticmethod
    def read_role_by_id(role_id: str):
        """read_role_by_id function"""
        with SessionLocal() as db:
            role_repository = RoleRepository(db)
            return role_repository.read_role_by_id(role_id)

    @staticmethod
    def read_role_by_type(role_type: str):
        """read_role_by_type function"""
        with SessionLocal() as db:
            role_repository = RoleRepository(db)
            return role_repository.read_role_by_type(role_type)

    @staticmethod
    def read_all_roles():
        """read_all_roles function"""
        with SessionLocal() as db:
            role_repository = RoleRepository(db)
            return role_repository.read_all_roles()

    @staticmethod
    def delete_role_by_id(role_id: str):
        """delete_role_by_id function"""
        try:
            with SessionLocal() as db:
                role_repository = RoleRepository(db)
                role = role_repository.read_role_by_id(role_id)
                if not role:
                    raise RoleNotFoundException(message="Role not found in the system.", code=404)
                return role_repository.delete_role_by_id(role_id)
        except Exception as e:
            raise e
