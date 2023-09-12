from models import Base, Customer, Employee
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, VARCHAR, SmallInteger, Date

class WorkoutPlan(Base):
    __tablename__ = 'workout_plan'

    exercises: Mapped[str] = mapped_column('exercises', VARCHAR(150), nullable=False)
    start_date: Mapped[str] = mapped_column('start_date', Date(), nullable=False)
    days: Mapped[int] = mapped_column('days', SmallInteger(3), nullable=False)
    customer_id: Mapped[int] = mapped_column('customer_id', Integer(), ForeignKey(Customer.id), nullable=False)
    employee_id: Mapped[int] = mapped_column('employee_id', Integer(), ForeignKey(Employee.id), nullable=False)