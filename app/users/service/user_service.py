from app.db import SessionLocal
from app.users.reporistories import UserRepository


class UserServices:

    @staticmethod
    def create_user(email, password):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.create_user(email, password)
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
