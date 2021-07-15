import psycopg2

conn = psycopg2.connect(dbname='air_fleet', user='postgres', password='*****')
cursor = conn.cursor()
cursor.execute('SELECT * FROM air_fleet.public.planes')
print(cursor.fetchall())
cursor.close()
conn.close()

# [(319, 'Airbus A319-100', 6850), (320, 'Airbus A320-200', 6150), 
# (321, 'Airbus A321-200', 5950), (333, 'Airbus A330-300', 11750), 
# (388, 'Airbus A380-800', 15400), (738, 'Boeing 737-800', 5765), 
# (763, 'Boeing 767-300', 12200), (773, 'Boeing 777-300', 11121)]
