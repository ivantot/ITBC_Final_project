"""Users controllers module."""
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.users.exceptions import UserNotActiveException
from app.users.exceptions.user_has_role_exceptions import UserHasRoleNotFoundException
from app.users.services import UserHasRoleService


class UserHasRoleController:
    """UserHasRoleController class"""
    @staticmethod
    def create_user_has_role(user_id: str, role_id: str):
        """create_user_has_role function"""
        try:
            user_has_role = UserHasRoleService.create_user_has_role(user_id, role_id)
            return user_has_role
        except UserNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except IntegrityError as exc:
            raise HTTPException(status_code=400, detail="Combination of user and provided role already exists.")\
                from exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def read_user_has_role_by_id(user_has_role_id: str):
        """read_user_has_role_by_id function"""
        user_has_role = UserHasRoleService.read_user_has_role_by_id(user_has_role_id)
        if user_has_role:
            return user_has_role
        raise HTTPException(status_code=400, detail="Combination of user with provided role does not exist.")

    @staticmethod
    def read_user_has_roles_by_user_id(user_id: str):
        """read_user_has_roles_by_user_id function"""
        user_has_roles = UserHasRoleService.read_user_has_roles_by_user_id(user_id)
        return user_has_roles

    @staticmethod
    def read_all_users_have_roles():
        """read_all_users_have_roles function"""
        users_have_roles = UserHasRoleService.read_all_users_have_roles()
        return users_have_roles

    @staticmethod
    def delete_user_has_role_by_id(user_has_role_id: str):
        """delete_user_has_role_by_id function"""
        try:
            UserHasRoleService.delete_user_has_role_by_id(user_has_role_id)
            return {"message": "Combination of user with provided role has been deleted."}
        except UserHasRoleNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) from e
