from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Customer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, DECIMAL

engine = create_engine('mysql+pymysql://root:root@localhost:3306/academia')
Session = sessionmaker(bind=engine)

class Purchase(Base):
    __tablename__ = 'purchase'

    id: Mapped[int] = mapped_column('id', Integer(), primary_key=True, autoincrement=True, nullable=False)
    price: Mapped[float] = mapped_column('price', DECIMAL(8,2), nullable=False)
    costumer_id: Mapped[int] = mapped_column('costumer_id', Integer(), ForeignKey(Customer.id), nullable=False)

    billing: Mapped[list["Billing"]] = relationship("Billing", backref="purchase")
    products: Mapped[list["Products"]] = relationship("Products", secondary= "purchase_has_products", backref="purchase")

    def create_purchase(price, customer_id):
        session = Session()
        new_purchase = Purchase(price=price, costumer_id=customer_id)
        session.add(new_purchase)
        session.commit()
        session.close()

    def update_purchase(id, price=None, customer_id=None):
        session = Session()
        purchase = session.query(Purchase).filter_by(id=id).first()
        if purchase:
            if price is not None:
                purchase.price = price
            if customer_id is not None:
                purchase.costumer_id = customer_id
            session.commit()
        session.close()

    def get_purchase_by_id(id):
        session = Session()
        purchase = session.query(Purchase).filter_by(id=id).first()
        session.close()
        return purchase


