from pydantic import BaseModel, UUID4, EmailStr


class UserSchema(BaseModel):
    user_id: UUID4
    email: str
    password: str
    is_active: bool

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
