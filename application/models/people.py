from models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, VARCHAR, Date

class People(Base):
    __tablename__ = 'people'

    id: Mapped[int] = mapped_column('id', Integer(), primary_key=True, autoincrement=True, nullable=False)
    person_name: Mapped[str] = mapped_column('person_name', VARCHAR(45), nullable=False)
    cpf: Mapped[str] = mapped_column('cpf', VARCHAR(11), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column('phone', VARCHAR(11), nullable=False)
    birth_date: Mapped[str] = mapped_column('birth_date', Date(), nullable=False)