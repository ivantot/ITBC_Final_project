"""Users controllers module."""
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.users.exceptions import UserInvalidPassword, UserNotFoundException, UserNotActiveException
from app.users.services import UserService, UserHasRoleService, RoleService, signJWT


class UserController:
    """UserController class """
    @staticmethod
    def create_user(email, password):
        """create_user function """
        try:
            user = UserService.create_user(email, password)
            return user
        except IntegrityError as exc:
            raise HTTPException(status_code=400, detail=f"User with provided email - {email} already exists.") from exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def read_user_by_id(user_id: str):
        """read_user_by_id function """
        user = UserService.read_user_by_id(user_id)
        if user:
            return user
        raise HTTPException(status_code=400, detail=f"User with provided id {user_id} does not exist.")

    @staticmethod
    def read_all_users():
        """read_all_users function """
        users = UserService.read_all_users()
        return users

    @staticmethod
    def read_all_active_users():
        """read_all_active_users function """
        users = UserService.read_all_active_users()
        return users

    @staticmethod
    def read_all_admins():
        """read_all_admins function """
        admins = UserService.read_all_admins()
        return admins

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        """update_user_is_active function """
        try:
            return UserService.update_user_is_active(user_id, is_active)
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_user_by_id(user_id: str):
        """delete_user_by_id function """
        try:
            UserService.delete_user_by_id(user_id)
            return {"message": f"User with provided id, {user_id} has been deleted."}
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) from e

    @staticmethod
    def login_user(email, password):
        """login_user function """
        try:
            user = UserService.login_user(email, password)
            roles_objects = UserHasRoleService.read_user_has_roles_by_user_id(user.user_id)
            roles = []
            for role in roles_objects:
                roles.append(RoleService.read_role_by_id(role.role_id).role_type)
            if "ADMIN" in roles:
                return signJWT(user.user_id, "ADMIN")
            if "PRO_USER" in roles:
                return signJWT(user.user_id, "PRO_USER")
            return signJWT(user.user_id, "USER")
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except UserNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
