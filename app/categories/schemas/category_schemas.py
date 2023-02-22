"""Categories schemas module."""
from typing import Optional
from pydantic import BaseModel, UUID4


class CategorySchema(BaseModel):
    """CategorySchema class"""
    category_id: UUID4
    name: str
    description: str
    is_active: bool

    class Config:
        """Config class"""
        orm_mode = True


class CategorySchemaIn(BaseModel):
    """CategorySchemaIn class"""
    name: str
    description: str

    class Config:
        """Config class"""
        orm_mode = True


class CategorySchemaUpdate(BaseModel):
    """CategorySchemaUpdate class"""
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        """Config class"""
        orm_mode = True


class CategorySchemaUpdateIsActive(BaseModel):
    """CategorySchemaUpdateIsActive class"""
    category_id: str
    is_active: bool

    class Config:
        """Config class"""
        orm_mode = True
