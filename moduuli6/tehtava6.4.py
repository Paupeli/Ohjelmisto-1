def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
numbers = [8,10,15,46,19]

sum_result = sum_of_numbers(numbers)
print("The sum is " +str(sum_result))

