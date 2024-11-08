computer_science = True
age = True

if computer_science and age:
    print("He's a programmer")
else:
    print("An analyst")

# while statements in python
# i = 1
# while i<20:
#     print(i)
#     i+=1

# the break statement
j = 10
while j<=100:
    print(j)
    if j == 60:
        break
    j+=10
# the continue statement
a = 0
while a < 1000:
    a += 100
    if a == 600:
        continue
    print(a)

# the else statement
q = 0
while q <= 10:
    print(q)
    q += 1
else:
    print("q is no longer 10")

# the for loop
# it's used to iterate over a sequence(set, tuple, dictionary, list)
fruits = ["Apple", "Mangoes", "Oranges", "Avacado"]
for fruit in fruits:
    print(fruit)

sett = set[1, 2, 3, 4, 5]
for s in sett:
    print(s)

# break statement
clas = ["P1", "P2", "P3", "P4", "P5", "P6"]
for c in clas:
    if c == "P4":
        break
    print(c)

# the continue statement

animals = ["Lion", "Cow", "Dog", "Cat", "Leopard"]
for animal in animals:
    if animal == "Cat":
        continue
    print(animal)

# for range() loop
for x in range(6, 20, 3):
    print(x)
# else for loop
for x in range(10):
    if x == 6:
        break
    print(x)
else:
    print("finally finished")

# nested for loop
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["wonderful", "beautiful", "expensive"]
cars = ["Toyota", "Jeep", "Prado"]

for x in adj:
    for y in cars:
        print(x, y)

# In this example, the enumerate() function is used to generate a sequence of tuples containing the index
# and value of each item in the tuple cars.
# The for loop then iterates over this sequence of tuples and prints the index and value of each item.
for index, z in enumerate(cars):
    print(index, z)
# 0 Toyota
# 1 Jeep
# 2 Prado
