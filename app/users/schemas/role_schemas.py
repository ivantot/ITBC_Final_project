from pydantic import BaseModel, UUID4


class RoleSchema(BaseModel):
    role_id: UUID4
    role_type: str

    class Config:
        orm_mode = True


class RoleSchemaIn(BaseModel):
    role_type: str

    class Config:
        orm_mode = True
