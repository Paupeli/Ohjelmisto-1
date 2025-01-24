numbers = []

while True:
  number_str = input("Enter a number: ")

  try:
      number = float(number_str)
      numbers.append(number)
  except ValueError:
      print("Programme stopped.")


  if number_str == "":
      if numbers:
       print(f"The highest value is {max(numbers):2.2f} and  the lowest value is {min(numbers):2.2f}")
      else:
       print("No numbers entered")
      break