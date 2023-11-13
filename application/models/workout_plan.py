from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Customer, Employee
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, VARCHAR, SmallInteger, Date

engine = create_engine('mysql+pymysql://root:root@localhost:3306/academia')
Session = sessionmaker(bind=engine)

class WorkoutPlan(Base):
    __tablename__ = 'workout_plan'

    exercises: Mapped[str] = mapped_column('exercises', VARCHAR(150), nullable=False)
    start_date: Mapped[str] = mapped_column('start_date', Date(), nullable=False)
    days: Mapped[int] = mapped_column('days', SmallInteger(), nullable=False)
    customer_id: Mapped[int] = mapped_column('customer_id', Integer(), ForeignKey(Customer.id), nullable=False, primary_key=True)
    employee_id: Mapped[int] = mapped_column('employee_id', Integer(), ForeignKey(Employee.id), nullable=False)

    def create_workout_plan(exercises, start_date, days, customer_id, employee_id):
        session = Session()
        new_workout_plan = WorkoutPlan(exercises=exercises, start_date=start_date, days=days,
                                        customer_id=customer_id, employee_id=employee_id)
        session.add(new_workout_plan)
        session.commit()
        session.close()

    def update_workout_plan(customer_id, employee_id, exercises=None, start_date=None, days=None):
        session = Session()
        workout_plan = session.query(WorkoutPlan).filter_by(customer_id=customer_id, employee_id=employee_id).first()
        if workout_plan:
            if exercises is not None:
                workout_plan.exercises = exercises
            if start_date is not None:
                workout_plan.start_date = start_date
            if days is not None:
                workout_plan.days = days
            session.commit()
        session.close()

    def get_workout_plan(customer_id, employee_id):
        session = Session()
        workout_plan = session.query(WorkoutPlan).filter_by(customer_id=customer_id, employee_id=employee_id).first()
        session.close()
        return workout_plan


