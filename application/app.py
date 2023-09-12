from models import *
from services.db import engine

def create_db():
    Base.metadata.create_all(engine)

create_db()