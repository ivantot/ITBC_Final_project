from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.vendors.services import VendorService


class VendorController:

    @staticmethod
    def create_vendor(name: str,
                      address: str,
                      category_id: str,
                      cash_only: bool = False):
        try:
            vendor = VendorService.create_vendor(name, address, category_id, cash_only)
            return vendor
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Vendor with provided name - {name} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_vendor_by_id(vendor_id: str):
        vendor = VendorService.read_vendor_by_id(vendor_id)
        if vendor:
            return vendor
        else:
            raise HTTPException(status_code=400, detail=f"Vendor with provided id {vendor_id} does not exist.")

    @staticmethod
    def read_vendors_by_category_id(category_id: str):
        vendor = VendorService.read_vendors_by_category_id(category_id)
        if vendor:
            return vendor
        else:
            raise HTTPException(status_code=400, detail=f"Vendors with provided id {category_id} do not exist.")

    @staticmethod
    def read_vendor_by_name(name: str):
        vendor = VendorService.read_vendor_by_name(name)
        if vendor:
            return vendor
        else:
            raise HTTPException(status_code=400, detail=f"Vendor with provided name {name} does not exist.")

    @staticmethod
    def read_all_vendors():
        vendors = VendorService.read_all_vendors()
        return vendors

    @staticmethod
    def update_vendor_is_active(vendor_id: str, is_active: bool):
        try:
            return VendorService.update_vendor_is_active(vendor_id, is_active)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_vendor_cash_only(vendor_id: str, cash_only: bool):
        try:
            return VendorService.update_vendor_cash_only(vendor_id, cash_only)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_vendor_by_id(vendor_id: str, name: str = None, address: str = None):
        try:
            return VendorService.update_vendor_by_id(vendor_id, name, address)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_vendor_by_id(vendor_id: str):
        try:
            VendorService.delete_vendor_by_id(vendor_id)
            return {"message": f"Vendor with provided id, {vendor_id} has been deleted."}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
