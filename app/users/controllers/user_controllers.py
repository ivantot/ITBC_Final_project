from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.users.exceptions import UserInvalidPassword
from app.users.services import UserServices, UserHasRoleServices, RoleServices, signJWT


class UserController:

    @staticmethod
    def create_user(email, password):
        try:
            user = UserServices.create_user(email, password)
            return user
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User with provided email - {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_user_by_id(user_id: str):
        user = UserServices.read_user_by_id(user_id)
        if user:
            return user
        else:
            raise HTTPException(status_code=400, detail=f"User with provided id {user_id} does not exist.")

    @staticmethod
    def read_all_users():
        users = UserServices.read_all_users()
        return users

    @staticmethod
    def read_all_admins():
        admins = UserServices.read_all_admins()
        return admins

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        try:
            return UserServices.update_user_is_active(user_id, is_active)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            UserServices.delete_user_by_id(user_id)
            return {"message": f"User with provided id, {user_id} has been deleted."}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def login_user(email, password):
        try:
            user = UserServices.login_user(email, password)
            roles_objects = UserHasRoleServices.read_user_has_roles_by_user_id(user.user_id)
            roles = []
            for role in roles_objects:
                roles.append(RoleServices.read_role_by_id(role.role_id).role_type)
            if "ADMIN" in roles:
                return signJWT(user.user_id, "ADMIN")
            elif "PRO_USER" in roles:
                return signJWT(user.user_id, "PRO_USER")
            return signJWT(user.user_id, "USER")
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
