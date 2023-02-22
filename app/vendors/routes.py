"""Vendors module."""
from fastapi import APIRouter, Depends

from app.users.controllers.user_auth_controller import JWTBearer
from app.vendors.controllers import VendorController
from app.vendors.schemas import VendorSchema, VendorSchemaIn, VendorSchemaUpdate, VendorSchemaUpdateIsActive, \
    VendorSchemaUpdateCashOnly

vendor_router = APIRouter(tags=["Vendors"], prefix="/api/vendors")


@vendor_router.post("/add-new-vendor", response_model=VendorSchema,
                    dependencies=[Depends(JWTBearer("USER"))])
def create_vendor(vendor: VendorSchemaIn):
    """create_vendor route"""
    vendor = VendorController.create_vendor(vendor.name,
                                            vendor.address,
                                            vendor.category_id,
                                            vendor.cash_only)
    return vendor


@vendor_router.get("/id", response_model=VendorSchema,
                   dependencies=[Depends(JWTBearer("USER"))])
def get_vendor_by_id(vendor_id: str):
    """get_vendor_by_id route"""
    return VendorController.read_vendor_by_id(vendor_id)


@vendor_router.get("/get-vendors-by-category-id", response_model=list[VendorSchema],
                   dependencies=[Depends(JWTBearer("USER"))])
def get_vendors_by_category_id(category_id: str):
    """get_vendors_by_category_id route"""
    return VendorController.read_vendors_by_category_id(category_id)


@vendor_router.get("/get-vendor-by-name", response_model=VendorSchema,
                   dependencies=[Depends(JWTBearer("USER"))])
def get_vendor_by_name(name: str):
    """get_vendor_by_name route"""
    return VendorController.read_vendor_by_name(name)


@vendor_router.get("/get-all-vendors", response_model=list[VendorSchema],
                   dependencies=[Depends(JWTBearer("USER"))])
def get_all_vendors():
    """get_all_vendors route"""
    return VendorController.read_all_vendors()


@vendor_router.put("/update/is_active", response_model=VendorSchema,
                   dependencies=[Depends(JWTBearer("ADMIN"))])
def update_vendor_is_active(vendor: VendorSchemaUpdateIsActive):
    """update_vendor_is_active route"""
    return VendorController.update_vendor_is_active(vendor.vendor_id, vendor.is_active)


@vendor_router.put("/update/cash-only", response_model=VendorSchema,
                   dependencies=[Depends(JWTBearer("ADMIN"))])
def update_vendor_cash_only(vendor: VendorSchemaUpdateCashOnly):
    """update_vendor_cash_only route"""
    return VendorController.update_vendor_cash_only(vendor.vendor_id, vendor.cash_only)


@vendor_router.put("/update", response_model=VendorSchema,
                   dependencies=[Depends(JWTBearer("USER"))])
def update_vendor_by_id(vendor_id: str, vendor: VendorSchemaUpdate = None):
    """update_vendor_by_id route"""
    return VendorController.update_vendor_by_id(vendor_id,
                                                vendor.name,
                                                vendor.address)


@vendor_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_vendor_by_id(vendor_id: str):
    """delete_vendor_by_id route"""
    return VendorController.delete_vendor_by_id(vendor_id)
