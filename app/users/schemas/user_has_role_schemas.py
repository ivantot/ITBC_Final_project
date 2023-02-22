"""Users schemas module."""
from pydantic import BaseModel, UUID4
from app.users.schemas.role_schemas import RoleSchema


class UserHasRoleSchema(BaseModel):
    """UserHasRoleSchema class"""
    user_has_role_id: UUID4
    user_id: str
    role_id: str
    role: RoleSchema

    class Config:
        """Config class"""
        orm_mode = True


class UserHasRoleOnlySchema(BaseModel):
    """UserHasRoleOnlySchema class"""
    role: RoleSchema

    class Config:
        """Config class"""
        orm_mode = True


class UserHasRoleSchemaIn(BaseModel):
    """UserHasRoleSchemaIn class"""
    user_id: str
    role_id: str

    class Config:
        """Config class"""
        orm_mode = True
