inch_to_cm = 2.54

while True:
    inch_str = float(input("Enter inches: "))

    cm = inch_str * inch_to_cm

    if inch_str >0:
     print(f"{inch_str} inches is {cm:2.2f} cm")
    else:
     print("Negative number entered")
    break