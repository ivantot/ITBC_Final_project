from app.db import SessionLocal
from app.vendors.repositories import VendorRepository


class VendorService:

    @staticmethod
    def create_vendor(name: str,
                      address: str,
                      category_id: str,
                      cash_only: bool = False):
        with SessionLocal() as db:
            try:
                vendor_repository = VendorRepository(db)
                return vendor_repository.create_vendor(name, address, category_id, cash_only)
            except Exception as e:
                raise e

    @staticmethod
    def read_vendor_by_id(vendor_id: str):
        with SessionLocal() as db:
            vendor_repository = VendorRepository(db)
            return vendor_repository.read_vendor_by_id(vendor_id)

    @staticmethod
    def read_vendors_by_category_id(category_id: str):
        with SessionLocal() as db:
            vendor_repository = VendorRepository(db)
            return vendor_repository.read_vendors_by_category_id(category_id)

    @staticmethod
    def read_vendor_by_name(name: str):
        with SessionLocal() as db:
            vendor_repository = VendorRepository(db)
            return vendor_repository.read_vendor_by_name(name)

    @staticmethod
    def read_all_vendors():
        with SessionLocal() as db:
            vendor_repository = VendorRepository(db)
            return vendor_repository.read_all_vendors()

    @staticmethod
    def update_vendor_is_active(vendor_id: str, is_active: bool):
        with SessionLocal() as db:
            try:
                vendor_repository = VendorRepository(db)
                return vendor_repository.update_vendor_is_active(vendor_id, is_active)
            except Exception as e:
                raise e

    @staticmethod
    def update_vendor_cash_only(vendor_id: str, cash_only: bool):
        with SessionLocal() as db:
            try:
                vendor_repository = VendorRepository(db)
                return vendor_repository.update_vendor_cash_only(vendor_id, cash_only)
            except Exception as e:
                raise e

    @staticmethod
    def update_vendor_by_id(vendor_id: str, name: str = None, address: str = None):
        with SessionLocal() as db:
            try:
                vendor_repository = VendorRepository(db)
                return vendor_repository.update_vendor_by_id(vendor_id, name, address)
            except Exception as e:
                raise e

    @staticmethod
    def delete_vendor_by_id(vendor_id: str):
        try:
            with SessionLocal() as db:
                vendor_repository = VendorRepository(db)
                return vendor_repository.delete_vendor_by_id(vendor_id)
        except Exception as e:
            raise e
