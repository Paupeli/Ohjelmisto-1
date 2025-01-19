sex = str(input("What is your biological sex? M/F: "))
hemoglobin_level = int(input("What is your hemoglobin level? " ))

male = "M"
female = "F"

if sex == "F":
    if hemoglobin_level < 117:
        print("Your hemoglobin level is too low")
    elif hemoglobin_level > 175:
        print("Your hemoglobin level is too high")
    else:
        print("Your hemoglobin level is normal")

if sex == "M":
    if hemoglobin_level < 134:
        print("Your hemoglobin level is too low")
    elif hemoglobin_level >195:
        print("Your hemoglobin level is too high")
    else:
        print("Your hemoglobin level is normal")

