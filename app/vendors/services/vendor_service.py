"""Vendors services module."""
from app.categories.exceprtions import CategoryNotActiveException, CategoryNotFoundException
from app.categories.repositories import CategoryRepository
from app.db import SessionLocal
from app.vendors.exceptions import VendorNotFoundException
from app.vendors.repositories import VendorRepository


class VendorService:
    """VendorService class"""
    @staticmethod
    def create_vendor(name: str,
                      address: str,
                      category_id: str,
                      cash_only: bool = False):
        """create_vendor function"""
        with SessionLocal() as db:
            try:
                vendor_repository = VendorRepository(db)
                category_repository = CategoryRepository(db)
                category = category_repository.read_category_by_id(category_id)
                if not category:
                    raise CategoryNotFoundException(message="Category not found in the system.", code=404)
                if not category.is_active:
                    raise CategoryNotActiveException(message="Category not active. Activate category to enable "
                                                             "vendor assignment.", code=401)
                return vendor_repository.create_vendor(name, address, category_id, cash_only)
            except Exception as e:
                raise e

    @staticmethod
    def read_vendor_by_id(vendor_id: str):
        """read_vendor_by_id function"""
        with SessionLocal() as db:
            vendor_repository = VendorRepository(db)
            return vendor_repository.read_vendor_by_id(vendor_id)

    @staticmethod
    def read_vendors_by_category_id(category_id: str):
        """read_vendors_by_category_id function"""
        with SessionLocal() as db:
            vendor_repository = VendorRepository(db)
            return vendor_repository.read_vendors_by_category_id(category_id)

    @staticmethod
    def read_vendor_by_name(name: str):
        """read_vendor_by_name function"""
        with SessionLocal() as db:
            vendor_repository = VendorRepository(db)
            return vendor_repository.read_vendor_by_name(name)

    @staticmethod
    def read_all_vendors():
        """read_all_vendors function"""
        with SessionLocal() as db:
            vendor_repository = VendorRepository(db)
            return vendor_repository.read_all_vendors()

    @staticmethod
    def update_vendor_is_active(vendor_id: str, is_active: bool):
        """update_vendor_is_active function"""
        with SessionLocal() as db:
            try:
                vendor_repository = VendorRepository(db)
                vendor = vendor_repository.read_vendor_by_id(vendor_id)
                if not vendor:
                    raise VendorNotFoundException(message="Vendor not found in the system.",
                                                  code=404)
                return vendor_repository.update_vendor_is_active(vendor_id, is_active)
            except Exception as e:
                raise e

    @staticmethod
    def update_vendor_cash_only(vendor_id: str, cash_only: bool):
        """update_vendor_cash_only function"""
        with SessionLocal() as db:
            try:
                vendor_repository = VendorRepository(db)
                vendor = vendor_repository.read_vendor_by_id(vendor_id)
                if not vendor:
                    raise VendorNotFoundException(message="Vendor not found in the system.", code=404)
                return vendor_repository.update_vendor_cash_only(vendor_id, cash_only)
            except Exception as e:
                raise e

    @staticmethod
    def update_vendor_by_id(vendor_id: str, name: str = None, address: str = None):
        """update_vendor_by_id function"""
        with SessionLocal() as db:
            try:
                vendor_repository = VendorRepository(db)
                vendor = vendor_repository.read_vendor_by_id(vendor_id)
                if not vendor:
                    raise VendorNotFoundException(message="Vendor not found in the system.",
                                                  code=404)
                return vendor_repository.update_vendor_by_id(vendor_id, name, address)
            except Exception as e:
                raise e

    @staticmethod
    def delete_vendor_by_id(vendor_id: str):
        """delete_vendor_by_id function"""
        try:
            with SessionLocal() as db:
                vendor_repository = VendorRepository(db)
                vendor = vendor_repository.read_vendor_by_id(vendor_id)
                if not vendor:
                    raise VendorNotFoundException(message="Vendor not found in the system.",
                                                  code=404)
                return vendor_repository.delete_vendor_by_id(vendor_id)
        except Exception as e:
            raise e
