from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class PaletteDb(Base):
    __tablename__ = "paletts"
    pk = Column('pk', Integer, primary_key=True)
    name = Column('name', String)
    capacity = Column('capacity', Float)

    def __init__(self, pk, name, capacity):
        self.pk = pk
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return f'pk={self.pk}, name={self.name}, capacity={self.capacity}'


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
