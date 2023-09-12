from models import Base, People
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer

class Customer(Base):
    __tablename__ = 'costumer'

    id: Mapped[int] = mapped_column('id', Integer(), ForeignKey(People.id), nullable=False, primary_key=True)
    