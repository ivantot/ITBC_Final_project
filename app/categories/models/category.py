from uuid import uuid4

from sqlalchemy import Column, String, Boolean

from app.db import Base


class Category(Base):
    __tablename__ = "categories"
    category_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(100), unique=True)
    description = Column(String(200))
    is_active = Column(Boolean, default=True)

    def __init__(self, name: str, description: str, is_active: bool = True):
        self.name = name
        self.description = description
        self.is_active = is_active
