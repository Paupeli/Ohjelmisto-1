import random


def dice_roll(sides):
    return random.randint(1,sides)

def main ():
    sides = int(input("Enter the number of sides on the die:  "))
    number = int(input(f"Enter the maximum number on the die: "))

    result = 0
    while result != number:
        result = dice_roll(sides)
        print(f"Dice roll: {result}")


if __name__ == "__main__":
    main()