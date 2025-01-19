centimetres = float(input("How many centimetres is your fish? "))


if centimetres<37:
    missing_cm = 37 - centimetres
    print(f"You need to let the fish back to the lake, you're missing {missing_cm: .2f} cm ")


else:
    print("Well done! You can keep your fish")