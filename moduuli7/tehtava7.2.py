names = set()

while True:
    name = input("Enter a name: ")

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        names.add(name)
        print("New name")
print("\nList of entered names: ")
for name in names:
    print(name)