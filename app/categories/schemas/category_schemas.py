from typing import Union, Optional
from pydantic import BaseModel, UUID4


class CategorySchema(BaseModel):
    category_id: UUID4
    name: str
    description: str
    is_active: bool

    class Config:
        orm_mode = True


class CategorySchemaIn(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class CategorySchemaUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True
