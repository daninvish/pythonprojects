fruit = ("oranges", 5, "apple", "pinnaple", "passion", 1, 2, 7, "pawpaw")
print(fruit)
print(fruit[2])
print("The first element in the fruit tuple is :", fruit[0])
print("The last element in the tuple is:", fruit[-1])
print("TRhe first three elements in fruit tuple is : ", fruit[0:3])
game = (1, 2, 3, "yes", 9)
w = game.index(9)
print(w)
print(game[3])

# Concatenation of a tupple
a = ('a', 'b', 'c')
b = ('e', 'f', 'g', 'a')
c = a + b
print(c)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
results = tuple1 + tuple2
print(results)
my_tuple = (1, 6, 7, 8, 6, 8, 9)
print(my_tuple.count(6))
my_tuple2 = (30, 70, 80, 90)
print(my_tuple2.index(30))

# Tuple unpacking
my_info = ("Okidi", "Dan", 80)
x, y, z = my_info
print(x)
print(y)
print(z)
