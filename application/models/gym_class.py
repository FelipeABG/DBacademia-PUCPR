from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, DateTime, Enum, DECIMAL

engine = create_engine('mysql+pymysql://root:root@localhost:3306/academia')
Session = sessionmaker(bind=engine)

class GymClass(Base):
    __tablename__ = 'class'

    id: Mapped[int] = mapped_column('id', Integer(), primary_key=True, autoincrement=True, nullable=False)
    class_datetime: Mapped[str] = mapped_column('class_datetime', DateTime(), nullable=False)
    class_type: Mapped[list] = mapped_column('class_type', Enum('spinning', 'zumba', 'pilates'), nullable=False)
    price: Mapped[float] = mapped_column('price', DECIMAL(5,2), nullable=False)

    billing: Mapped[list["Billing"]] = relationship("Billing", backref="class")
    employee: Mapped[list["Employee"]] = relationship("Employee", secondary= "class_has_employee", backref="class")
    customer: Mapped[list["Customer"]] = relationship("Customer", secondary= "class_has_customer", backref="class")

    def create_gym_class(class_datetime, class_type, price):
        session = Session()
        new_class = GymClass(class_datetime=class_datetime, class_type=class_type, price=price)
        session.add(new_class)
        session.commit()
        session.close()
    
    def update_gym_class(id, class_datetime=None, class_type=None, price=None):
        session = Session()
        gym_class = session.query(GymClass).filter_by(id=id).first()
        if gym_class:
            if class_datetime is not None:
                gym_class.class_datetime = class_datetime
            if class_type is not None:
                gym_class.class_type = class_type
            if price is not None:
                gym_class.price = price
            session.commit()
        session.close()

    def get_gym_class_by_id(id):
        session = Session()
        gym_class = session.query(GymClass).filter_by(id=id).first()
        session.close()
        return gym_class


