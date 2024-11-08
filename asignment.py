# A program to calculate the product of two numbers

print("***** Multiplication Calculator *****")
fnum = int(input('Enter the first number:  '))
snum = int(input('Enter the last number:  '))

def product(num,  snum):
    product = fnum * snum
    return product
print(f"The product of {fnum} and {snum} is", product(fnum, snum))

# -----------------------------------------
# ----------------------------------------

# A program to calculate the modulus of two
# numbers

print("Modulus Calculator")
num1 = int(input('Enter the first number:  '))
num2 = int(input('Enter the last number:  '))
print("Modulus Calculator")
def modulus(num1, num2):
    modulus = num1 % num2
    return modulus
print(f"The modulus of {num1} divided by {num2} is: ", modulus(num1, num2))

# -----------------------------------------
# ----------------------------------------

# A program to calculate the area of a triangle using function

print("Triangle Area Calculator")
l = int(input("Enter the length of the triangle:  "))
h = int(input("Enter the height of the triangle:  "))

def area_o_triangle(l, h):
    area_o_triangle = l*h/2
    return area_o_triangle
print(f"The area of the triangle is: ", area_o_triangle(l, h))