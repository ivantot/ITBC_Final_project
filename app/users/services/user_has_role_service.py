from app.db import SessionLocal
from app.users.exceptions import UserNotActiveException
from app.users.exceptions.user_has_role_exceptions import UserHasRoleNotFoundException
from app.users.reporistories import UserHasRoleRepository, UserRepository


class UserHasRoleService:

    @staticmethod
    def create_user_has_role(user_id: str, role_id: str):
        with SessionLocal() as db:
            try:
                user_has_role_repository = UserHasRoleRepository(db)
                user_repository = UserRepository(db)
                user = user_repository.read_user_by_id(user_id)
                if not user.is_active:
                    raise UserNotActiveException(message="User not active. Activate user to enable role assignment.",
                                                 code=401)
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
    def read_all_users_have_roles():
        with SessionLocal() as db:
            user_has_role_repository = UserHasRoleRepository(db)
            return user_has_role_repository.read_all_users_have_roles()

    @staticmethod
    def delete_user_has_role_by_id(user_has_role_id: str):
        try:
            with SessionLocal() as db:
                user_has_role_repository = UserHasRoleRepository(db)
                user_has_role = user_has_role_repository.read_user_has_role_by_id(user_has_role_id)
                if not user_has_role:
                    raise UserHasRoleNotFoundException(message="Combination of user and role not found in the system.",
                                                       code=404)
                return user_has_role_repository.delete_user_has_role_by_id(user_has_role_id)
        except Exception as e:
            raise e
