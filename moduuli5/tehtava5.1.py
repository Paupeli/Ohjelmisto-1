import random

dice = []
n = 0

dice_roll = int(input("How many dice to roll?: "))

for _ in range(dice_roll):
    roll = random.randint(1,6)
    dice.append(roll)

n = sum(dice)

print(f"The sum of the numbers is: {n} ")