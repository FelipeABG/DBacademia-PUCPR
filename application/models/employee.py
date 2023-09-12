from models import Base, People, Place
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, VARCHAR, DECIMAL

class Employee(Base):
    __tablename__ = 'employee'

    id: Mapped[int] = mapped_column('id', Integer(), ForeignKey(People.id), primary_key=True, nullable=False)
    position: Mapped[str]  = mapped_column('position', VARCHAR(45), nullable=False)
    salary: Mapped[float] = mapped_column('salary', DECIMAL(8,2), nullable=False)
    place_id: Mapped[int] = mapped_column('place_id', Integer(), ForeignKey(Place.id), nullable=False)

    