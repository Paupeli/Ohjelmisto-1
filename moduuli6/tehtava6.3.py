def gasoline(gallons):
    return gallons *3.785

def main ():
    amount_of_gallons = float(input("Enter the amount of gallons: "))

    while amount_of_gallons >= 0:
        litres = gasoline(amount_of_gallons)
        print(f"The amount of gasoline in litres is {litres}")

        amount_of_gallons = float(input("Enter the amount of gallons: "))

if __name__ == "__main__":
    main()