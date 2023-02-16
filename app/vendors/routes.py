from fastapi import APIRouter, Depends

from app.users.controllers.user_auth_controller import JWTBearer
from app.vendors.controllers import VendorController
from app.vendors.schemas import VendorSchema, VendorSchemaIn, VendorSchemaUpdate

vendor_router = APIRouter(tags=["Vendors"], prefix="/api/vendors")


@vendor_router.post("/add-new-vendor", response_model=VendorSchema)
def create_vendor(vendor: VendorSchemaIn):
    vendor = VendorController.create_vendor(vendor.name,
                                            vendor.address,
                                            vendor.category_id,
                                            vendor.cash_only)
    return vendor


@vendor_router.get("/id", response_model=VendorSchema)
def get_vendor_by_id(vendor_id: str):
    return VendorController.read_vendor_by_id(vendor_id)


@vendor_router.get("/get-vendors-by-category-id", response_model=list[VendorSchema])
def get_vendors_by_category_id(category_id: str):
    return VendorController.read_vendors_by_category_id(category_id)


@vendor_router.get("/get-vendor-by-name", response_model=VendorSchema)
def get_vendor_by_name(name: str):
    return VendorController.read_vendor_by_name(name)


@vendor_router.get("/get-all-vendors", response_model=list[VendorSchema])
def get_all_vendors():
    return VendorController.read_all_vendors()


@vendor_router.put("/update/is_active", response_model=VendorSchema)
def update_vendor_is_active(vendor_id: str, is_active: bool):
    return VendorController.update_vendor_is_active(vendor_id, is_active)


@vendor_router.put("/update/cash-only", response_model=VendorSchema)
def update_vendor_cash_only(vendor_id: str, cash_only: bool):
    return VendorController.update_vendor_cash_only(vendor_id, cash_only)


@vendor_router.put("/update", response_model=VendorSchema)
def update_vendor_by_id(vendor_id: str, vendor: VendorSchemaUpdate = None):
    return VendorController.update_vendor_by_id(vendor_id,
                                                vendor.name,
                                                vendor.address)


@vendor_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_vendor_by_id(vendor_id: str):
    return VendorController.delete_vendor_by_id(vendor_id)
