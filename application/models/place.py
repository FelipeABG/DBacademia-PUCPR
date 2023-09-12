from models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, VARCHAR, DECIMAL, SmallInteger

class Place(Base):
    __tablename__ = 'place'

    id: Mapped[int] = mapped_column('id', Integer(), primary_key=True, autoincrement=True, nullable=False)
    place_name: Mapped[str] = mapped_column('place_name', VARCHAR(45), nullable=False)
    rent_price: Mapped[float] = mapped_column('rent_price', DECIMAL(8,2), nullable=False)
    cep: Mapped[str] = mapped_column('cep', VARCHAR(10), nullable=False)
    phone_number: Mapped[str] = mapped_column('phone_number', SmallInteger(), nullable=False)
    city: Mapped[str] = mapped_column('city', VARCHAR(20), nullable=False)
    neighborhood: Mapped[str] = mapped_column('neighborhood', VARCHAR(45), nullable=False)
    street: Mapped[str] = mapped_column('street', VARCHAR(100), nullable=False)
    place_state: Mapped[str] = mapped_column('place_state', VARCHAR(2), nullable=False)