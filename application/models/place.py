from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, VARCHAR, DECIMAL, SmallInteger

engine = create_engine('mysql+pymysql://root:root@localhost:3306/academia')
Session = sessionmaker(bind=engine)

class Place(Base):
    __tablename__ = 'place'

    id: Mapped[int] = mapped_column('id', Integer(), primary_key=True, autoincrement=True, nullable=False)
    place_name: Mapped[str] = mapped_column('place_name', VARCHAR(45), nullable=False)
    rent_price: Mapped[float] = mapped_column('rent_price', DECIMAL(8,2), nullable=False)
    cep: Mapped[str] = mapped_column('cep', VARCHAR(10), nullable=False)
    phone_number: Mapped[str] = mapped_column('phone_number', VARCHAR(45), nullable=False)
    city: Mapped[str] = mapped_column('city', VARCHAR(20), nullable=False)
    neighborhood: Mapped[str] = mapped_column('neighborhood', VARCHAR(45), nullable=False)
    street: Mapped[str] = mapped_column('street', VARCHAR(100), nullable=False)
    place_state: Mapped[str] = mapped_column('place_state', VARCHAR(20), nullable=False)

    employee: Mapped[list["Employee"]] = relationship("Employee", backref="place")
    products: Mapped[list["Products"]] = relationship("Products", secondary= "place_has_products", backref="pplace")

    def create_place(place_name, rent_price, cep, phone_number, city, neighborhood, street, place_state):
        session = Session()
        new_place = Place(place_name=place_name, rent_price=rent_price, cep=cep, phone_number=phone_number,
                        city=city, neighborhood=neighborhood, street=street, place_state=place_state)
        session.add(new_place)
        session.commit()
        session.close()
    
    def update_place(id, place_name=None, rent_price=None, cep=None, phone_number=None,
                 city=None, neighborhood=None, street=None, place_state=None):
        session = Session()
        place = session.query(Place).filter_by(id=id).first()
        if place:
            if place_name is not None:
                place.place_name = place_name
            if rent_price is not None:
                place.rent_price = rent_price
            if cep is not None:
                place.cep = cep
            if phone_number is not None:
                place.phone_number = phone_number
            if city is not None:
                place.city = city
            if neighborhood is not None:
                place.neighborhood = neighborhood
            if street is not None:
                place.street = street
            if place_state is not None:
                place.place_state = place_state
            session.commit()
        session.close()
    
    def get_place_by_id(id):
        session = Session()
        place = session.query(Place).filter_by(id=id).first()
        session.close()
        return place


