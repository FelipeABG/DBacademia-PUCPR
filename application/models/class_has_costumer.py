from models import Base, GymClass, Customer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer

class ClassHasCostumer(Base):
    __tablename__ = 'class_has_costumer'
    
    class_id: Mapped[int] = mapped_column('class_id', Integer(), ForeignKey(GymClass.id), nullable=False, primary_key=True)
    customer_id: Mapped[int] = mapped_column('customer_id', Integer(), ForeignKey(Customer.id), nullable=False, primary_key=True)
