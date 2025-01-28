cities = []

for _ in range(5) :
    city = input("Enter the name of the city: ")
    cities.append(city)

print("\nThe cities you entered are:")
for city in cities:
    print(city)