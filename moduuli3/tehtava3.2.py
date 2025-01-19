cabin = str(input("Enter your cabin type: "))

LUX = "LUX"
A = "A"
B = "B"
C = "C"

if cabin == LUX:
    print ("LUX is a cabin with a balcony on the upper deck")
elif cabin == A:
    print("A is a cabin with a window above the car deck")
elif cabin == B:
    print("B is a cabin without a window above the car deck")
elif cabin == C:
    print("C is a cabin without a window below the car deck")
else:
    print("This type of cabin cannot be found")