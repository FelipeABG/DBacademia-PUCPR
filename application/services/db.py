from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine

instance = f'mysql+pymysql://root:Bbag2508!@localhost:3306/academia'

if not database_exists(instance):
    create_database(instance)

engine = create_engine(instance, echo=True)