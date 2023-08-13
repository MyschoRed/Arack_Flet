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

# p_a = session.query(Palette).filter(Palette.name.like("%A%")).all()
# print(p_a)
# p_b = session.query(Palette).filter(Palette.name.like("%B%")).all()


# for p in range(48):
#     if p < 9:
#         session.add(Palette(pk=p, name=f'A0{p + 1}', capacity=2000))
#         session.commit()
#
#     elif p < 24:
#         session.add(Palette(pk=p, name=f'A{p + 1}', capacity=2000))
#         session.commit()
#
#     elif p < 24 +9:
#         session.add(Palette(pk=p, name=f'B0{p - 24}', capacity=2000))
#         session.commit()
#
#     else:
#         session.add(Palette(pk=p, name=f'B{p - 24}', capacity=2000))
#         session.commit()
