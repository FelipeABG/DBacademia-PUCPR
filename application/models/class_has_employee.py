from models import Base, GymClass, Employee
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer

class ClassHasEmployee(Base):
    __tablename__ = 'class_has_employee'

    class_id: Mapped[int] = mapped_column('class_id', Integer(), ForeignKey(GymClass.id), nullable=False, primary_key=True)
    employee_id: Mapped[int] = mapped_column('employee_id', Integer(), ForeignKey(Employee.id), nullable=False, primary_key=True)
    