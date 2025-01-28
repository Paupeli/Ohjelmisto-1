numbers = []

while True:
    number_str = input("Enter a number: ")

    if number_str == "":
      break

    try:
        number = float(number_str)
        numbers.append(number)
    except ValueError:
        print("Program stopped")

numbers.sort(reverse = True)
print("Program stopped. The 5 greatest numbers in descending order:", numbers[:5])