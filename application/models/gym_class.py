from models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, DateTime, Enum, DECIMAL

class GymClass(Base):
    __tablename__ = 'class'

    id: Mapped[int] = mapped_column('id', Integer(), primary_key=True, autoincrement=True, nullable=False)
    class_datetime: Mapped[str] = mapped_column('class_datetime', DateTime(), nullable=False)
    class_type: Mapped[list] = mapped_column('class_type', Enum('spinning', 'zumba', 'pilates'), nullable=False)
    price: Mapped(float) = mapped_column('price', DECIMAL(5,2), nullable=False)