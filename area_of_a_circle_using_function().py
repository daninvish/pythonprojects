# A program to calculate the area of a circle using function
from Hello.data import area_of_the_circle

pi = 3.14
r = int(input("Enter the radius of the circle:  "))

# defining the function
def area(r):
    area = pi*r ** 2
    return area
print("The area of the circle is", area(r))