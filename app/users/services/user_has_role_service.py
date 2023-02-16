from app.db import SessionLocal
from app.users.reporistories import UserHasRoleRepository


class UserHasRoleService:

    @staticmethod
    def create_user_has_role(user_id: str, role_id: str):
        with SessionLocal() as db:
            try:
                user_has_role_repository = UserHasRoleRepository(db)
                return user_has_role_repository.create_user_has_role(user_id, role_id)
            except Exception as e:
                raise e

    @staticmethod
    def read_user_has_role_by_id(user_has_role_id: str):
        with SessionLocal() as db:
            user_has_role_repository = UserHasRoleRepository(db)
            return user_has_role_repository.read_user_has_role_by_id(user_has_role_id)

    @staticmethod
    def read_user_has_roles_by_user_id(user_id: str):
        with SessionLocal() as db:
            user_has_role_repository = UserHasRoleRepository(db)
            return user_has_role_repository.read_user_has_roles_by_user_id(user_id)

    @staticmethod
    def delete_user_has_role_by_id(user_has_role_id: str):
        try:
            with SessionLocal() as db:
                user_has_role_repository = UserHasRoleRepository(db)
                return user_has_role_repository.delete_user_has_role_by_id(user_has_role_id)
        except Exception as e:
            raise e
