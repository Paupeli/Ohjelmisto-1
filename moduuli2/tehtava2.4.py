number1_str = input("Give a number: ")
number2_str = input("Give another number: ")
number3_str = input("Give one more number: ")

number1 = float(number1_str)
number2 = float(number2_str)
number3 = float(number3_str)

sum_of_numbers = (number1 + number2 + number3)
product = (number1 * number2 * number3)
average = ((number1 + number2 + number3) //3)

print("The sum of the numbers is " + str(sum_of_numbers) + ", the product of the numbers is " + str(product) + " and the average of the numbers is " + str(average))