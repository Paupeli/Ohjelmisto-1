import math

def calculate_unit_price(diameter, price):
    radius = diameter/2
    area_cm2 = math.pi * (radius ** 2)

    area_m2 = area_cm2 / 10000

    unit_price = price / area_m2
    return unit_price

def main():
    diameter1 = float(input("Enter the diameter of the first pizza: "))
    price1 = float(input("Enter the price of the first pizza: "))

    diameter2 = float(input("Enter the diameter of the second pizza: "))
    price2 = float(input("Enter the price of the second pizza: "))

    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2,price2)

    print(f"Unit price of the first pizza: {unit_price1:.2f} euros per m2")
    print(f"Unit price of the second pizza: {unit_price2:.2f} euros per m2")

    if unit_price1 < unit_price2:
        print("The first pizza has a lower unit price")
    elif unit_price2 < unit_price1:
        print("The second pizza has a lower unit price")

if __name__ == "__main__":
    main()
