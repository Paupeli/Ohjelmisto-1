import mysql.connector

def get_airports_from_country(area_code):

    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='pauliina',
        password='tikru123!',
        autocommit=True,
        collation='utf8mb4_unicode_ci'
    )

    sql = (f"SELECT airport.type as 'airport types', COUNT(*) as 'amount of airports' "
           f"FROM airport,country "
           f"WHERE airport.iso_country = country.iso_country "
           f"AND airport.iso_country = %s "
           f"GROUP BY airport.type")


    cursor = connection.cursor()
    cursor.execute(sql, (area_code,))
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        print(f"Airports in {area_code}: ")
        for row in result:
            print(f"{row[1]} {row[0]}s")
    else:
        print("The airport cannot be found")

area_code = input("Enter the area code: ")
get_airports_from_country(area_code)
