from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.users.exceptions.role_exceptions import RoleNotFoundException
from app.users.services import RoleService


class RoleController:

    @staticmethod
    def create_role(role_type: str):
        try:
            role = RoleService.create_role(role_type)
            return role
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Role of this type {role_type} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_role_by_id(role_id: str):
        role = RoleService.read_role_by_id(role_id)
        if role:
            return role
        else:
            raise HTTPException(status_code=400, detail=f"Role with provided id {role_id} does not exist")

    @staticmethod
    def read_role_by_type(role_type: str):
        role = RoleService.read_role_by_type(role_type)
        if role:
            return role
        else:
            raise HTTPException(status_code=400, detail=f"Role with provided type {role_type} does not exist")

    @staticmethod
    def read_all_roles():
        roles = RoleService.read_all_roles()
        return roles

    @staticmethod
    def delete_role_by_id(role_id: str):
        try:
            RoleService.delete_role_by_id(role_id)
            return {"message": f"Role with provided id, {role_id} has been deleted."}
        except RoleNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
