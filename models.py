from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ksiezniczki(Base):
    __tablename__ = "ksiezniczki"

    id = Column(Integer, primary_key=True, autoincrement=True)
    imie = Column(String(64))
    czy_dziewica = Column(Boolean)
    szerokosc = Column(Integer)
    wysokosc = Column(Integer)

class Smoki(Base):
    __tablename__ = "smoki"

    id = Column(Integer, primary_key=True, autoincrement=True)
    szerokosc = Column(Integer)
    wysokosc = Column(Integer)


if __name__ == '__main__':
    from database import engine
    Base.metadata.create_all(engine)
