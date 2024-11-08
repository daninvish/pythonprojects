# A program to calculate the area of a circle
# Declaring the variables
PI = 22 / 7
radius = float(input("Enter the radius of the circle: "))
# Calculating the area
area = PI * radius ** 2
rounded_area = round(area, 4)

print("The area of the circle is: ", rounded_area,"cm\u00B2")
print(f"{area:.2f} cm\u00B3")
# The '\u00B2' is the Unicode escape sequence for the superscript 2 character.
