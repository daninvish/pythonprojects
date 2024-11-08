# Creating the function using the def keyword
def greet():
    print("Hello my friend")

#  function call
greet()

def wish(name, msg):
    print("Hello", name + ' ' + msg)

# A program to find the sum of two numbers using function
a = int(input('Enter the first number'))
b = int(input('Enter the second number'))
def sum_of_two_numbers(a, b):
    sum1 = a + b
    return sum1
print("Their sum is", sum_of_two_numbers(a,b))
