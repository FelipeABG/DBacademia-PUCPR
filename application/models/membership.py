from models import Base, Customer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, DECIMAL, VARCHAR, Enum

class Membership(Base):
    __tablename__ = 'membership'

    id: Mapped[int] = mapped_column('id', Integer(), primary_key=True, autoincrement=True, nullable=False)
    price: Mapped[float] = mapped_column('price', DECIMAL(8,2), nullable=False)
    membership_name: Mapped[str] = mapped_column('membership_name', VARCHAR(45), nullable=False)
    membership_type: Mapped[list] = mapped_column('membership_type', Enum('mensal', 'trimestral', 'semestral', 'anual'), nullable=False)
    customer_id:  Mapped[int] = mapped_column('customer_id', Integer(), ForeignKey(Customer.id), nullable=False)