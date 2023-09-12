from models import Base, Customer, Employee
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, DECIMAL, DateTime

class PhysicalAssessment(Base):
    __tablename__ = 'physical_assessment'

    height: Mapped[float] = mapped_column('height', DECIMAL(3,2), nullable=False)
    weight: Mapped[float] = mapped_column('weight', DECIMAL(4,2), nullable=False)
    assessment_datetime: Mapped[str] = mapped_column('assessment_datetime', DateTime(), nullable=False)
    customer_id: Mapped[int] = mapped_column('customer_id', Integer(), ForeignKey(Customer.id), nullable=False)
    employee_id: Mapped[int] = mapped_column('employee_id', Integer(), ForeignKey(Employee.id), nullable=False)
    
