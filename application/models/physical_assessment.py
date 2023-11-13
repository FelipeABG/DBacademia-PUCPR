from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Customer, Employee
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, DECIMAL, DateTime

engine = create_engine('mysql+pymysql://root:root@localhost:3306/academia')
Session = sessionmaker(bind=engine)

class PhysicalAssessment(Base):
    __tablename__ = 'physical_assessment'

    height: Mapped[float] = mapped_column('height', DECIMAL(3,2), nullable=False)
    weight: Mapped[float] = mapped_column('weight', DECIMAL(4,2), nullable=False)
    assessment_datetime: Mapped[str] = mapped_column('assessment_datetime', DateTime(), nullable=False)
    customer_id: Mapped[int] = mapped_column('customer_id', Integer(), ForeignKey(Customer.id), nullable=False, primary_key=True)
    employee_id: Mapped[int] = mapped_column('employee_id', Integer(), ForeignKey(Employee.id), nullable=False)
    
    def create_physical_assessment(height, weight, assessment_datetime, customer_id, employee_id):
        session = Session()
        new_assessment = PhysicalAssessment(height=height, weight=weight, assessment_datetime=assessment_datetime, customer_id=customer_id, employee_id=employee_id)
        session.add(new_assessment)
        session.commit()
        session.close()

    def update_physical_assessment(customer_id, employee_id, height=None, weight=None, assessment_datetime=None):
        session = Session()
        assessment = session.query(PhysicalAssessment).filter_by(customer_id=customer_id, employee_id=employee_id).first()
        if assessment:
            if height is not None:
                assessment.height = height
            if weight is not None:
                assessment.weight = weight
            if assessment_datetime is not None:
                assessment.assessment_datetime = assessment_datetime
            session.commit()
        session.close()
    
    def get_physical_assessment(customer_id, employee_id):
        session = Session()
        assessment = session.query(PhysicalAssessment).filter_by(customer_id=customer_id, employee_id=employee_id).first()
        session.close()
        return assessment


