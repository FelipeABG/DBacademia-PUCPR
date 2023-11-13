from models import Base, Place, Products
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, DateTime

class PlaceHasProducts(Base):
    __tablename__ = 'place_has_products'
    
    place_id: Mapped[int] = mapped_column('place_id', Integer(), ForeignKey(Place.id), primary_key=True, nullable=False)
    product_id:  Mapped[int] = mapped_column('product_id', Integer(), ForeignKey(Products.id), primary_key=True, nullable=False)
    aquisition_datetime: Mapped[str] = mapped_column('aquisition_datetime', DateTime(), nullable=False)