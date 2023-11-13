from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Employee, GymClass, Customer, Purchase, Membership
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Enum, DateTime, DECIMAL, ForeignKey

engine = create_engine('mysql+pymysql://root:root@localhost:3306/academia')
Session = sessionmaker(bind=engine)
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

    def create_billing(payment_method, total, billing_datetime, due_datetime, 
                        employee_id, class_id, customer_id, purchase_id, membership_id):
        session = Session()
        novo_faturamento = Billing(payment_method=payment_method, total=total,
                                    billing_datetime=billing_datetime, due_datetime=due_datetime,
                                    employee_id=employee_id, class_id=class_id,
                                    customer_id=customer_id, purchase_id=purchase_id,
                                    membership_id=membership_id)
        session.add(novo_faturamento)
        session.commit()
        session.close()


    def update_billing(id, payment_method, total, billing_datetime, due_datetime, 
                            employee_id, class_id, customer_id, purchase_id, membership_id):
        session = Session()
        faturamento_atualizado = session.query(Billing).filter_by(id=id).first()
        if faturamento_atualizado:
            faturamento_atualizado.payment_method = payment_method
            faturamento_atualizado.total = total
            faturamento_atualizado.billing_datetime = billing_datetime
            faturamento_atualizado.due_datetime = due_datetime
            faturamento_atualizado.employee_id = employee_id
            faturamento_atualizado.class_id = class_id
            faturamento_atualizado.customer_id = customer_id
            faturamento_atualizado.purchase_id = purchase_id
            faturamento_atualizado.membership_id = membership_id
            session.commit()
        session.close()

    def view_billing():
        session = Session()
        faturamentos = session.query(Billing).all()
        session.close()
        return faturamentos
