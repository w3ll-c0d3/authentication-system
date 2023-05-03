from sqlmodel import SQLModel, Session, create_engine
from pathlib import Path

# Create Database
DB_PATH = Path() / 'connection' / 'database.db'
engine = create_engine(f'sqlite:///{DB_PATH}', future=True, echo=True)
SQLModel.metadata.create_all(engine)


class Database():
    
    def __init__(self, db_name):
        self.db_name = db_name

    def connect():
        session = Session(engine) 
        return session
