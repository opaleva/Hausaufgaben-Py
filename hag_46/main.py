from sqlalchemy import create_engine, Column, Float, String, ForeignKey
from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.util.langhelpers import _symbol

engine: MockConnection = create_engine("postgresql+psycopg2://postgres:*****@localhost/airports", echo=True)
Base = declarative_base()


class Airport(Base):
    __tablename__: str = 'Airports'
    airport_code: Column = Column(String(3), primary_key=True)
    airport_name: Column = Column(String(100), nullable=False)
    city: Column = Column(String(100), nullable=False)
    based_airline: Column = Column(String(3), ForeignKey("Airlines.airline_id"))
    longitude: Column = Column(Float, nullable=False)
    latitude: Column = Column(Float, nullable=False)
    timezone: Column = Column(String(12), nullable=False)
    Airline: _symbol = relationship("Airline")


class Airline(Base):
    __tablename__: str = 'Airlines'
    airline_id: Column = Column(String(3), primary_key=True)
    airline: Column = Column(String(100), nullable=False)
    Airport: _symbol = relationship("Airport", overlaps="Airline")


Base.metadata.create_all(engine)
