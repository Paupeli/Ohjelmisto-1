import mysql.connector

def get_airport_name_and_location(icao_code):
    sql = f"SELECT airport.name, municipality FROM airport WHERE ident = '{icao_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The name of the airport is {row[0]} and the location is {row[1]}")
    else:
        print("The airport cannot be found")

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'pauliina',
    password = 'tikru123!',
    autocommit = True,
    collation = 'utf8mb4_unicode_ci'
    )

icao_code = input ("Enter the ICAO code: ")
get_airport_name_and_location(icao_code)