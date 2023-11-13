from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, People
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer

engine = create_engine('mysql+pymysql://root:root@localhost:3306/academia')
Session = sessionmaker(bind=engine)

class Customer(Base):
    __tablename__ = 'customer'

    id: Mapped[int] = mapped_column('id', Integer(), ForeignKey(People.id), nullable=False, primary_key=True)

    physical_assesment: Mapped[list["PhysicalAssessment"]] = relationship("PhysicalAssessment", backref="customer")
    purchase: Mapped[list["Purchase"]] = relationship("Purchase", backref="customer")


    def create_customer(id, physical_assesment=None, purchase=None):
        session = Session()
        novo_cliente = Customer(id=id, physical_assesment=physical_assesment, purchase=purchase)
        session.add(novo_cliente)
        session.commit()
        session.close()

    def update_customer(id, physical_assesment=None, purchase=None):
        session = Session()
        cliente_atualizado = session.query(Customer).filter_by(id=id).first()
        if cliente_atualizado:
            cliente_atualizado.physical_assesment = physical_assesment
            cliente_atualizado.purchase = purchase
            session.commit()
        session.close()

    def view_customer(id):
        session = Session()
        cliente = session.query(Customer).filter_by(id=id).first()
        session.close()
        return cliente
