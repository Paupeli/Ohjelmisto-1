import mysql.connector
from geopy.distance import geodesic

def get_coordinates (icao_code):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='pauliina',
        password='tikru123!',
        autocommit=True,
        collation='utf8mb4_unicode_ci'
    )

    sql = (f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s")

    cursor = connection.cursor()
    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()

    if result:
        return (result[0], result[1])
    else:
        return None

def calculate_distance(icao_code_first, icao_code_second):
    coordinates_first = get_coordinates(icao_code_first)
    coordinates_second = get_coordinates(icao_code_second)

    if coordinates_first and coordinates_second:
        distance = geodesic(coordinates_first,coordinates_second).kilometers
        print(f"The distance between {icao_code_first} and {icao_code_second} is {distance:.2f} kilometers.")
    else:
        print("The ICAO codes cannot be found.")

icao_code_first = input("Enter an ICAO code: ")
icao_code_second = input("Enter another ICAO code: ")

calculate_distance(icao_code_first, icao_code_second)




