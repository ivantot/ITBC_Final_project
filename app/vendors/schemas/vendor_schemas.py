"""Vendors schemas module."""
from typing import Optional
from pydantic import BaseModel, UUID4

from app.categories.schemas import CategorySchema


class VendorSchema(BaseModel):
    """VendorSchema class"""
    vendor_id: UUID4
    name: str
    address: str
    category_id: str
    cash_only: bool
    is_active: bool
    category: CategorySchema

    class Config:
        """Config class"""
        orm_mode = True


class VendorSchemaIn(BaseModel):
    """VendorSchemaIn class"""
    name: str
    address: str
    category_id: str
    cash_only: bool

    class Config:
        """Config class"""
        orm_mode = True


class VendorSchemaUpdate(BaseModel):
    """VendorSchemaUpdate class"""
    name: Optional[str]
    address: Optional[str]

    class Config:
        """Config class"""
        orm_mode = True


class VendorSchemaUpdateIsActive(BaseModel):
    """VendorSchemaUpdateIsActive class"""
    vendor_id: str
    is_active: bool

    class Config:
        """Config class"""
        orm_mode = True


class VendorSchemaUpdateCashOnly(BaseModel):
    """VendorSchemaUpdateCashOnly class"""
    vendor_id: str
    cash_only: bool

    class Config:
        """Config class"""
        orm_mode = True
