from sqlalchemy import Column, Integer, VARCHAR, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base  

engine = create_engine('mysql+pymysql://root:root@localhost:3306/academia')
Session = sessionmaker(bind=engine)

class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    person_name = Column(VARCHAR(45), nullable=False)
    cpf = Column(VARCHAR(11), nullable=False, unique=True)
    phone = Column(VARCHAR(11), nullable=False)
    birth_date = Column(Date, nullable=False)

    def create_person(person_name, cpf, phone, birth_date):
        session = Session() 
        new_person = People(person_name=person_name, cpf=cpf, phone=phone, birth_date=birth_date)
        session.add(new_person)
        session.commit() 
        session.close()  

    def update_person(id, person_name=None, cpf=None, phone=None, birth_date=None):
        session = Session()
        person = session.query(People).filter_by(id=id).first()
        if person:
            if person_name is not None:
                person.person_name = person_name
            if cpf is not None:
                person.cpf = cpf
            if phone is not None:
                person.phone = phone
            if birth_date is not None:
                person.birth_date = birth_date
            session.commit()
        session.close()

    def get_person_by_id(id):
        session = Session()
        person = session.query(People).filter_by(id=id).first()
        session.close()
        return person
