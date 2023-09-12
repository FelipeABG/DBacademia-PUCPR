from models import Base, Purchase, Products
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer

class PurchaseHasProducts(Base):
    __tablename__ = 'purchase_has_products'
    
    purchase_id: Mapped[int] = mapped_column('purchase_id', Integer(), ForeignKey(Purchase.id), primary_key=True, nullable=False)
    product_id:  Mapped[int] = mapped_column('product_id', Integer(), ForeignKey(Products.id), primary_key=True, nullable=False)