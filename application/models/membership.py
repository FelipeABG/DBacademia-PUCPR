from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Customer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, DECIMAL, VARCHAR, Enum

engine = create_engine('mysql+pymysql://root:root@localhost:3306/academia')
Session = sessionmaker(bind=engine)

class Membership(Base):
    __tablename__ = 'membership'

    id: Mapped[int] = mapped_column('id', Integer(), primary_key=True, autoincrement=True, nullable=False)
    price: Mapped[float] = mapped_column('price', DECIMAL(8,2), nullable=False)
    membership_name: Mapped[str] = mapped_column('membership_name', VARCHAR(45), nullable=False)
    membership_type: Mapped[list] = mapped_column('membership_type', Enum('mensal', 'trimestral', 'semestral', 'anual'), nullable=False)
    customer_id:  Mapped[int] = mapped_column('customer_id', Integer(), ForeignKey(Customer.id), nullable=False)

    def create_membership(price, membership_name, membership_type, customer_id):
        session = Session()
        new_membership = Membership(price=price, membership_name=membership_name,
                                    membership_type=membership_type, customer_id=customer_id)
        session.add(new_membership)
        session.commit()
        session.close()

    def update_membership(id, price=None, membership_name=None, membership_type=None, customer_id=None):
        session = Session()
        membership = session.query(Membership).filter_by(id=id).first()
        if membership:
            if price is not None:
                membership.price = price
            if membership_name is not None:
                membership.membership_name = membership_name
            if membership_type is not None:
                membership.membership_type = membership_type
            if customer_id is not None:
                membership.customer_id = customer_id
            session.commit()
        session.close()

    def get_membership_by_id(id):
        session = Session()
        membership = session.query(Membership).filter_by(id=id).first()
        session.close()
        return membership


