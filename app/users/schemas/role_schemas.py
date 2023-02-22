"""Users schemas module."""
from pydantic import BaseModel, UUID4


class RoleSchema(BaseModel):
    """RoleSchema class"""
    role_id: UUID4
    role_type: str

    class Config:
        """Config class"""
        orm_mode = True


class RoleSchemaIn(BaseModel):
    """RoleSchemaIn class"""
    role_type: str

    class Config:
        """Config class"""
        orm_mode = True
