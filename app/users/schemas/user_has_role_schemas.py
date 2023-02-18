from pydantic import BaseModel, UUID4
from app.users.schemas.role_schemas import RoleSchema


class UserHasRoleSchema(BaseModel):
    user_has_role_id: UUID4
    user_id: str
    role_id: str
    role: RoleSchema

    class Config:
        orm_mode = True


class UserHasRoleOnlySchema(BaseModel):
    role: RoleSchema

    class Config:
        orm_mode = True


class UserHasRoleSchemaIn(BaseModel):
    user_id: str
    role_id: str

    class Config:
        orm_mode = True
