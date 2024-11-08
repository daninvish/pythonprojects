import math

print("Area of a shape Calculator")
print("Select the shape now: ")
print("Option:")
print("\t\t1: Square\n"
      "\t\t2: Triangle\n"
      "\t\t3: Rectangle\n")
opt = int(input("Select option 1 to 3: "))
if opt == 1:
    l = int(input("Enter the length of the square: "))
    print(f"The area of the square with length {l} is {pow(l, 2)} ")
elif opt == 2:
    l2 = int(input("Enter the length of the triangle: "))
    w = int(input("Enter the height of the triangle"))
    print(f"The area of the triangle is {math.prod(0.2, l2, w)} ")
else:
    print("range 1 to 3")