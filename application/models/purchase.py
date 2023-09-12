from models import Base, Customer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, DECIMAL

class Purchase(Base):
    __tablename__ = 'purchase'

    id: Mapped[int] = mapped_column('id', Integer(), primary_key=True, autoincrement=True, nullable=False)
    price: Mapped[float] = mapped_column('price', DECIMAL(8,2), nullable=False)
    costumer_id: Mapped[int] = mapped_column('costumer_id', Integer(), ForeignKey(Customer.id), nullable=False)