import hashlib

from app.db import SessionLocal
from app.users.exceptions import UserInvalidPassword
from app.users.reporistories import UserRepository, UserHasRoleRepository, RoleRepository


class UserService:

    @staticmethod
    def create_user(email, password):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(email, hashed_password)
            except Exception as e:
                raise e

    @staticmethod
    def read_user_by_id(user_id: str):
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.read_user_by_id(user_id)

    @staticmethod
    def read_all_users():
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.read_all_users()

    @staticmethod
    def read_all_admins():
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user_has_role_repository = UserHasRoleRepository(db)
                role_repository = RoleRepository(db)
                users = user_repository.read_all_users()
                admin_role_id = role_repository.read_role_by_type("ADMIN").role_id
                admins = []
                for user in users:
                    user_has_roles = user_has_role_repository.read_user_has_roles_by_user_id(user.user_id)
                    for user_has_role in user_has_roles:
                        if user_has_role.role_id == admin_role_id:
                            admins.append(user)
                return admins
            except Exception as e:
                raise e

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_active(user_id, is_active)
            except Exception as e:
                raise e

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id)
        except Exception as e:
            raise e

    @staticmethod
    def login_user(email: str, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.read_user_by_email(email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Invalid password for user", code=401)
                return user
            except Exception as e:
                raise e
