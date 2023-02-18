from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.users.exceptions import UserInvalidPassword, UserNotFoundException, UserNotActiveException
from app.users.services import UserService, UserHasRoleService, RoleService, signJWT


class UserController:

    @staticmethod
    def create_user(email, password):
        try:
            user = UserService.create_user(email, password)
            return user
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User with provided email - {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_user_by_id(user_id: str):
        user = UserService.read_user_by_id(user_id)
        if user:
            return user
        else:
            raise HTTPException(status_code=400, detail=f"User with provided id {user_id} does not exist.")

    @staticmethod
    def read_all_users():
        users = UserService.read_all_users()
        return users

    @staticmethod
    def read_all_active_users():
        users = UserService.read_all_active_users()
        return users

    @staticmethod
    def read_all_admins():
        admins = UserService.read_all_admins()
        return admins

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        try:
            return UserService.update_user_is_active(user_id, is_active)
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            UserService.delete_user_by_id(user_id)
            return {"message": f"User with provided id, {user_id} has been deleted."}
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def login_user(email, password):
        try:
            user = UserService.login_user(email, password)
            roles_objects = UserHasRoleService.read_user_has_roles_by_user_id(user.user_id)
            roles = []
            for role in roles_objects:
                roles.append(RoleService.read_role_by_id(role.role_id).role_type)
            if "ADMIN" in roles:
                return signJWT(user.user_id, "ADMIN")
            elif "PRO_USER" in roles:
                return signJWT(user.user_id, "PRO_USER")
            return signJWT(user.user_id, "USER")
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
