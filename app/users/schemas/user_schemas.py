from app.users.schemas.user_has_role_schemas import UserHasRoleOnlySchema
from pydantic import BaseModel, UUID4, EmailStr


class UserSchema(BaseModel):
    user_id: UUID4
    email: str
    password: str
    is_active: bool

    class Config:
        orm_mode = True


class UserWithRolesSchema(BaseModel):
    user_id: UUID4
    email: str
    password: str
    is_active: bool
    roles: list[UserHasRoleOnlySchema]

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
