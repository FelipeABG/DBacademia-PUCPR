from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, VARCHAR, Enum, DECIMAL, SmallInteger

engine = create_engine('mysql+pymysql://root:root@localhost:3306/academia')
Session = sessionmaker(bind=engine)

class Products(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column('id', Integer(), primary_key=True, autoincrement=True, nullable=False)
    product_name:Mapped[str] = mapped_column('product_name', VARCHAR(256), nullable=False)
    product_type: Mapped[list] = mapped_column('product_type', Enum('suplemento', 'comida', 'bebida'), nullable=False)
    price: Mapped[float] = mapped_column('price', DECIMAL(8,2), nullable=False)
    amount: Mapped[int] = mapped_column('amount', SmallInteger(), nullable=False)

    def create_product(product_name, product_type, price, amount):
        session = Session()
        new_product = Products(product_name=product_name, product_type=product_type, price=price, amount=amount)
        session.add(new_product)
        session.commit()
        session.close()
    
    def update_product(id, product_name=None, product_type=None, price=None, amount=None):
        session = Session()
        product = session.query(Products).filter_by(id=id).first()
        if product:
            if product_name is not None:
                product.product_name = product_name
            if product_type is not None:
                product.product_type = product_type
            if price is not None:
                product.price = price
            if amount is not None:
                product.amount = amount
            session.commit()
        session.close()
    
    def get_product_by_id(id):
        session = Session()
        product = session.query(Products).filter_by(id=id).first()
        session.close()
        return product


