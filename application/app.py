from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import Session

instance = "mysql+pymysql://root:root@localhost:3306/academia"

if not database_exists(instance):
    create_database(instance)

engine = create_engine(instance)

session = Session(engine)