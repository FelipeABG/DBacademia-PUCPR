from models import Base, Employee, GymClass, Customer, Purchase, Membership
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Enum, DateTime, DECIMAL, ForeignKey

class Billing(Base):
    __tablename__ = 'billing'
    
    id: Mapped[int] = mapped_column('id', Integer(), primary_key=True, nullable=False, autoincrement=True)
    payment_method: Mapped[list] = mapped_column('payment_method', Enum("credit card", "debit card", "PIX"), nullable=False)
    total: Mapped[float] = mapped_column('total', DECIMAL(8,2), nullable=False)
    billing_datetime: Mapped[str] = mapped_column('billing_datetime', DateTime(), nullable=False)
    due_datetime: Mapped[str] = mapped_column('due_datetime', DateTime(), nullable=False)
    employee_id: Mapped[int] = mapped_column('employee_id', ForeignKey(Employee.id), nullable=False)
    class_id: Mapped[int] = mapped_column('class_id', ForeignKey(GymClass.id), nullable=False)
    customer_id: Mapped[int] = mapped_column('customer_id', ForeignKey(Customer.id), nullable=False)
    purchase_id: Mapped[int] = mapped_column('purchase_id', ForeignKey(Purchase.id), nullable=False)
    membership_id: Mapped[int] = mapped_column('membership_id', ForeignKey(Membership.id), nullable=False)


