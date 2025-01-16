length_str = input("What is the length of the rectangle?")
width_str = input("What is the width of the rectangle?")

length = float(length_str)
width = float(width_str)

perimeter = (length*2 + width*2)
area = (length * width)

print("The perimeter of the rectangle is " + str(perimeter) + " and the area of the rectangle is " + str(area))