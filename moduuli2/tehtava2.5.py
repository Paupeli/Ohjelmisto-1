lot = 13.3
pound = 13.3*32
talent= 13.3*32*20

lot_str = float(input("Give lots: ")) * lot
pound_str = float(input("Give pounds: ")) * pound
talent_str = float(input("Give talents: ")) * talent

total_mass_in_grams = lot_str + pound_str + talent_str

kilograms = total_mass_in_grams // 1000
grams = total_mass_in_grams % 1000

print(f"The mass is {kilograms:2.2f} kilograms and {grams:2.2f} grams")