from models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, VARCHAR, Enum, DECIMAL, SmallInteger

class Products(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column('id', Integer(), primary_key=True, autoincrement=True, nullable=False)
    product_name:Mapped[str] = mapped_column('product_name', VARCHAR(256), nullable=False)
    product_type: Mapped[list] = mapped_column('product_type', Enum('suplemento', 'comida', 'bebida'), nullable=False)
    price: Mapped[float] = mapped_column('price', DECIMAL(8,2), nullable=False)
    amount: Mapped[int] = mapped_column('amount', SmallInteger(), nullable=False)