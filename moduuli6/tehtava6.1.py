import random

def dice_roll():
    return random.randint(1,6)

def main ():
    result = 0
    while result != 6:
        result = dice_roll()
        print(f"Dice roll: {result}")

if __name__ == "__main__":
    main()