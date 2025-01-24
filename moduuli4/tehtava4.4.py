import random

drawn_number = (random.randint(1,10))

guess = int(input("Guess the number: "))

while guess != drawn_number:
    if guess > drawn_number:
        print("Too high")
    elif guess < drawn_number:
        print("Too low")
    guess = int(input("Guess the number: "))
print("Correct!")