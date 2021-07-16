from sqlalchemy import create_engine
from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.orm import sessionmaker
from main import Airport, Airline

engine: MockConnection = create_engine("postgresql+psycopg2://postgres:*****@localhost/airports", echo=True)
session: sessionmaker = sessionmaker(bind=engine)
s = session()

s.add_all([Airline(airline_id="AFL", airline="Aeroflot"),
           Airline(airline_id="CPA", airline="Cathay Pacific"),
           Airline(airline_id="DLH", airline="Deutsche Lufthansa AG"),
           Airline(airline_id="GIA", airline="Garuda Indonesia")])

s.commit()

s.add_all([Airport(airport_code="CGK", airport_name="Soekarno–Hatta International Airport",
                   city="West Jakarta", based_airline="GIA", latitude=-6.125556, longitude=106.655830,
                   timezone="UTC+8"),
           Airport(airport_code="FRA", airport_name="Frankfurt Airport",
                   city="Frankfurt am Main", based_airline="DLH", latitude=50.033333, longitude=8.570556,
                   timezone="UTC+1/UTC+2"),
           Airport(airport_code="HKG", airport_name="Hong Kong International Airport",
                   city="Hong Kong", based_airline="CPA", latitude=22.308046, longitude=113.918480, timezone="UTC+8"),
           Airport(airport_code="SVO", airport_name="Sheremetyevo International Airport",
                   city="Khimki", based_airline="AFL", latitude=55.973648, longitude=37.412503, timezone="UTC+3")])
s.commit()

print(f"{'~' * 50}\n{s.query(Airport).first().airport_name}\n{'~' * 50}\n")
for airport_name, city in s.query(Airport.airport_name, Airport.city).order_by(Airport.city):
    print(f"{'~' * 50}\n{airport_name} || {city}\n{'~' * 50}")
