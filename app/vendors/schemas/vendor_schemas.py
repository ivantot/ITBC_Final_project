from typing import Optional
from pydantic import BaseModel, UUID4

from app.categories.schemas import CategorySchema


class VendorSchema(BaseModel):
    vendor_id: UUID4
    name: str
    address: str
    category_id: str
    cash_only: bool
    is_active: bool
    category: CategorySchema

    class Config:
        orm_mode = True


class VendorSchemaIn(BaseModel):
    name: str
    address: str
    category_id: str
    cash_only: bool

    class Config:
        orm_mode = True


class VendorSchemaUpdate(BaseModel):
    name: Optional[str]
    address: Optional[str]

    class Config:
        orm_mode = True

