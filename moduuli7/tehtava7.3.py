airport_data = {}

while True:
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        icao_code = input("Enter ICAO code: ").strip().upper()
        airport_name = input("Enter airport name: ").strip()
        airport_data[icao_code] = airport_name
    elif choice == "2":
        icao_code = input("Enter ICAO code: ").strip().upper()
        if icao_code in airport_data:
            print(f"Airport: {airport_data[icao_code]}")
        else:
            print("Airport not found.")

    elif choice == "3":
        break
    else:
     print("Invalid code, please try again.")
