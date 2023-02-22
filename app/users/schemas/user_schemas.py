"""Users schemas module."""
from pydantic import BaseModel, UUID4, EmailStr
from app.users.schemas.user_has_role_schemas import UserHasRoleOnlySchema


class UserSchema(BaseModel):
    """UserSchema class"""
    user_id: UUID4
    email: str
    password: str
    is_active: bool

    class Config:
        """Config class"""
        orm_mode = True


class UserWithRolesSchema(BaseModel):
    """UserWithRolesSchema class"""
    user_id: UUID4
    email: str
    password: str
    is_active: bool
    roles: list[UserHasRoleOnlySchema]

    class Config:
        """Config class"""
        orm_mode = True


class UserSchemaIn(BaseModel):
    """UserSchemaIn class"""
    email: EmailStr
    password: str

    class Config:
        """Config class"""
        orm_mode = True


class UserSchemaUpdateIsActive(BaseModel):
    """UserSchemaUpdateIsActive class"""
    user_id: str
    is_active: bool

    class Config:
        """Config class"""
        orm_mode = True
