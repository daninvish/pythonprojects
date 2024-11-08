# Multiplication table of a number using the for loop
number = int(input("Enter a number to see its multiplication table: "))
for x in range(1, 13):
    print(f"{number} x {x} = {number * x}")

# Filtering a list based on certain condition
# 1. Even number
listt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for l in listt:
    if l % 2==0:
       even_numbers.append(l)
print("List of even numbers from the list")
print(even_numbers)

# 2. Calculating the sum of the items in the list
#  from the list above
sum = 0
for li in listt:
    sum += li
print(f"The sum is {sum}")
print("\t&***************************************************************************************&")
print("\t&******************************** MULTIPLICATION TABLE *********************************&")
print("\t&***************************************************************************************&")
for w in range(1,13):
    for e in range(1,13):
        print("  ", w * e, end="\t")
    print()