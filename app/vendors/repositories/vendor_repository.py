"""Vendors repositories module."""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.vendors.exceptions import VendorNotFoundException
from app.vendors.models import Vendor


class VendorRepository:
    """VendorRepository class"""
    def __init__(self, db: Session):
        self.db = db

    def create_vendor(self,
                      name: str,
                      address: str,
                      category_id: str,
                      cash_only: bool = False) -> Vendor:
        """create_vendor function"""
        try:
            vendor = Vendor(name, address, category_id, cash_only)
            self.db.add(vendor)
            self.db.commit()
            self.db.refresh(vendor)
            return vendor
        except IntegrityError as e:
            raise e

    def read_vendor_by_id(self, vendor_id: str) -> Vendor:
        """read_vendor_by_id function"""
        vendor = self.db.query(Vendor).filter(Vendor.vendor_id == vendor_id).first()
        return vendor

    def read_vendors_by_category_id(self, category_id: str) -> [Vendor]:
        """read_vendors_by_category_id function"""
        vendors = self.db.query(Vendor).filter(Vendor.category_id == category_id).all()
        return vendors

    def read_vendor_by_name(self, name: str) -> Vendor:
        """read_vendor_by_name function"""
        vendor = self.db.query(Vendor).filter(Vendor.name == name).first()
        return vendor

    def read_all_vendors(self) -> [Vendor]:
        """read_all_vendors function"""
        vendors = self.db.query(Vendor).all()
        return vendors

    def update_vendor_is_active(self, vendor_id: str, is_active: bool) -> Vendor:
        """update_vendor_is_active function"""
        try:
            vendor = self.db.query(Vendor).filter(Vendor.vendor_id == vendor_id).first()
            vendor.is_active = is_active
            self.db.add(vendor)
            self.db.commit()
            self.db.refresh(vendor)
            return vendor
        except Exception as e:
            raise e

    def update_vendor_cash_only(self, vendor_id: str, cash_only: bool) -> Vendor:
        """update_vendor_cash_only function"""
        try:
            vendor = self.db.query(Vendor).filter(Vendor.vendor_id == vendor_id).first()
            vendor.cash_only = cash_only
            self.db.add(vendor)
            self.db.commit()
            self.db.refresh(vendor)
            return vendor
        except Exception as e:
            raise e

    def update_vendor_by_id(self, vendor_id: str, name: str = None, address: str = None) -> Vendor:
        """update_vendor_by_id function"""
        try:
            vendor = self.db.query(Vendor).filter(Vendor.vendor_id == vendor_id).first()
            if vendor is None:
                raise VendorNotFoundException(f"Vendor with provided ID: {vendor_id} not found.", 400)
            if name is not None:
                vendor.name = name
            if address is not None:
                vendor.address = address
            self.db.add(vendor)
            self.db.commit()
            self.db.refresh(vendor)
            return vendor
        except Exception as e:
            raise e

    def delete_vendor_by_id(self, vendor_id: str) -> bool:
        """delete_vendor_by_id function"""
        try:
            vendor = self.db.query(Vendor).filter(Vendor.vendor_id == vendor_id).first()
            self.db.delete(vendor)
            self.db.commit()
            return True
        except Exception as e:
            raise e
