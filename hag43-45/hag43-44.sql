CREATE DATABASE air_fleet
ENCODING 'UTF8';

CREATE TABLE planes
( aircraft_code integer NOT NULL,
  model text NOT NULL,
  range integer NOT NULL,
  PRIMARY KEY ( aircraft_code ) );
CREATE TABLE airlines
( airline_id char( 3 ) NOT NULL,
  airline text NOT NULL,
  country text NOT NULL,
  PRIMARY KEY ( airline_id ) );
CREATE TABLE aviation
( airline_id char( 3 ) NOT NULL,
  aircraft_code integer NOT NULL );

INSERT INTO planes ( aircraft_code, model, range )
VALUES  ( 319, 'Airbus A319-100', 6850 ),
        ( 320, 'Airbus A320-200', 6150 ),
        ( 321, 'Airbus A321-200', 5950 ),
        ( 333, 'Airbus A330-300', 11750 ),
        ( 388, 'Airbus A380-800', 15400 ),
        ( 738, 'Boeing 737-800', 5765 ),
        ( 763, 'Boeing 767-300', 12200 ),
        ( 773, 'Boeing 777-300', 11121 );

INSERT INTO airlines ( airline_id, airline, country )
VALUES ( 'AFL', 'Aeroflot', 'Russia'),
       ( 'CPA', 'Cathay Pacific', 'Hong Kong' ),
       ( 'DLH', 'Deutsche Lufthansa AG', 'Germany' ),
       ( 'GIA', 'Garuda Indonesia', 'Indonesia' );

INSERT INTO aviation ( airline_id, aircraft_code )
VALUES ( 'AFL', 320 ),
       ( 'AFL', 321 ),
       ( 'AFL', 333 ),
       ( 'AFL', 738 ),
       ( 'CPA', 388 ),
       ( 'CPA', 777 ),
       ( 'DLH', 319 ),
       ( 'DLH', 321 ),
       ( 'DLH', 333 ),
       ( 'DLH', 763 ),
       ( 'GIA', 319 ),
       ( 'GIA', 321 ),
       ( 'GIA', 773 );

SELECT * FROM planes;
SELECT * FROM airlines;
SELECT * FROM aviation;

SELECT max( range ) FROM planes;
SELECT min ( range ) FROM planes;

-- №44

SELECT airline_id, count( * ) FROM aviation
GROUP BY airline_id
HAVING count( * ) > 2;

SELECT aircraft_code FROM planes
WHERE range > 10000
UNION
SELECT aircraft_code FROM planes
WHERE range < 6000
ORDER BY aircraft_code;

SELECT av.airline_id, av.aircraft_code, a.country
FROM aviation av
JOIN airlines AS a
ON av.airline_id = a.airline_id;

SELECT airline_id
FROM aviation
WHERE aircraft_code IN
( SELECT planes.aircraft_code
FROM planes
WHERE range < 6000 );
