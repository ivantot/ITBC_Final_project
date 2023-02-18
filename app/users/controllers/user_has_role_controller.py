
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.users.exceptions import UserNotActiveException
from app.users.exceptions.user_has_role_exceptions import UserHasRoleNotFoundException
from app.users.services import UserHasRoleService


class UserHasRoleController:

    @staticmethod
    def create_user_has_role(user_id: str, role_id: str):
        try:
            user_has_role = UserHasRoleService.create_user_has_role(user_id, role_id)
            return user_has_role
        except UserNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Combination of user and provided role already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_user_has_role_by_id(user_has_role_id: str):
        user_has_role = UserHasRoleService.read_user_has_role_by_id(user_has_role_id)
        if user_has_role:
            return user_has_role
        else:
            raise HTTPException(status_code=400, detail=f"Combination of user with provided role does not exist.")

    @staticmethod
    def read_user_has_roles_by_user_id(user_id: str):
        user_has_roles = UserHasRoleService.read_user_has_roles_by_user_id(user_id)
        return user_has_roles

    @staticmethod
    def read_all_users_have_roles():
        users_have_roles = UserHasRoleService.read_all_users_have_roles()
        return users_have_roles

    @staticmethod
    def delete_user_has_role_by_id(user_has_role_id: str):
        try:
            UserHasRoleService.delete_user_has_role_by_id(user_has_role_id)
            return {"message": f"Combination of user with provided role has been deleted."}
        except UserHasRoleNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
