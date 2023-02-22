"""Vendors controllers module."""
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.categories.exceprtions import CategoryNotActiveException, CategoryNotFoundException
from app.vendors.exceptions import VendorNotFoundException
from app.vendors.services import VendorService


class VendorController:
    """VendorController class"""
    @staticmethod
    def create_vendor(name: str,
                      address: str,
                      category_id: str,
                      cash_only: bool = False):
        """create_vendor function"""
        try:
            vendor = VendorService.create_vendor(name, address, category_id, cash_only)
            return vendor
        except CategoryNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except CategoryNotActiveException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except IntegrityError as exc:
            raise HTTPException(status_code=400, detail=f"Vendor with provided name - {name} already exists.") from exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def read_vendor_by_id(vendor_id: str):
        """read_vendor_by_id function"""
        vendor = VendorService.read_vendor_by_id(vendor_id)
        if vendor:
            return vendor
        raise HTTPException(status_code=400, detail=f"Vendor with provided id {vendor_id} does not exist.")

    @staticmethod
    def read_vendors_by_category_id(category_id: str):
        """read_vendors_by_category_id function"""
        vendor = VendorService.read_vendors_by_category_id(category_id)
        if vendor:
            return vendor
        raise HTTPException(status_code=400, detail=f"Vendors with provided id {category_id} do not exist.")

    @staticmethod
    def read_vendor_by_name(name: str):
        """read_vendor_by_name function"""
        vendor = VendorService.read_vendor_by_name(name)
        if vendor:
            return vendor
        raise HTTPException(status_code=400, detail=f"Vendor with provided name {name} does not exist.")

    @staticmethod
    def read_all_vendors():
        """read_all_vendors function"""
        vendors = VendorService.read_all_vendors()
        return vendors

    @staticmethod
    def update_vendor_is_active(vendor_id: str, is_active: bool):
        """update_vendor_is_active function"""
        try:
            return VendorService.update_vendor_is_active(vendor_id, is_active)
        except VendorNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_vendor_cash_only(vendor_id: str, cash_only: bool):
        """update_vendor_cash_only function"""
        try:
            return VendorService.update_vendor_cash_only(vendor_id, cash_only)
        except VendorNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_vendor_by_id(vendor_id: str, name: str = None, address: str = None):
        """update_vendor_by_id function"""
        try:
            return VendorService.update_vendor_by_id(vendor_id, name, address)
        except VendorNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_vendor_by_id(vendor_id: str):
        """delete_vendor_by_id function"""
        try:
            VendorService.delete_vendor_by_id(vendor_id)
            return {"message": f"Vendor with provided id, {vendor_id} has been deleted."}
        except VendorNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) from e
