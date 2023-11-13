from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

instance = f'mysql+pymysql://root:root@localhost:3306/academia'

engine = create_engine(instance)
Session = sessionmaker(bind=engine)


if not database_exists(instance):
    create_database(instance)

def create_db():
    Base.metadata.create_all(engine)

