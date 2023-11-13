from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from typing import List 
from models import Base, People, Place
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, VARCHAR, DECIMAL

engine = create_engine('mysql+pymysql://root:root@localhost:3306/academia')
Session = sessionmaker(bind=engine)

class Employee(Base):
    __tablename__ = 'employee'

    id: Mapped[int] = mapped_column('id', Integer(), ForeignKey(People.id), primary_key=True, autoincrement=True, nullable=False)
    position: Mapped[str]  = mapped_column('position', VARCHAR(45), nullable=False)
    salary: Mapped[float] = mapped_column('salary', DECIMAL(8,2), nullable=False)
    place_id: Mapped[int] = mapped_column('place_id', Integer(), ForeignKey(Place.id), nullable=False)
    person_id: Mapped[int] = mapped_column('person_id', Integer(), ForeignKey(People.id), nullable=False)
    
    physical_assesment: Mapped[List["PhysicalAssessment"]] = relationship("PhysicalAssessment", backref="employee")
    workout_plan: Mapped[list["WorkoutPlan"]] = relationship("WorkoutPlan", backref="employee")
    billing: Mapped[list["Billing"]] = relationship("Billing", backref="employee")

    def create_employee(position, salary, place_id, person_id):
        session = Session()
        new_employee = Employee(position=position, salary=salary, place_id=place_id, person_id=person_id)
        session.add(new_employee)
        session.commit()
        session.close()

    def update_employee(id, position=None, salary=None, place_id=None, person_id=None):
        session = Session()
        employee = session.query(Employee).filter_by(id=id).first()
        if employee:
            if position is not None:
                employee.position = position
            if salary is not None:
                employee.salary = salary
            if place_id is not None:
                employee.place_id = place_id
            if person_id is not None:
                employee.person_id = person_id
            session.commit()
        session.close()

    def get_employee_by_id(id):
        session = Session()
        employee = session.query(Employee).filter_by(id=id).first()
        session.close()
        return employee


