list1 = [1,2,3,2,1,4]
print(list1)
# set with duplicate values using set()
my_set = set([1, 2, 3, 2, 1, 4])
print(my_set)

x = {'a', 'b', 'c', 'd'}
x.add('g')
print(x)
x.update(list1)
print(x)
# Update()
wild_animals = {"Lion", "Bear", "Fox"}
domestic_animals = ["Dog", "Cow", "Sheep"]
wild_animals.update(domestic_animals)
print(wild_animals)

# remove() to remove a specific element, but raises error if not found
set1 = {1,2,3}
set1.remove(3)
print(set1)

# discard() to remove an element without raising an error if the element is not present
set3 = {1,2,3,4,5,6}
set3.discard(5)
print(set3)

# clear() method empties the set
set4 = {1,2,3,4,5,6,7,9}
set4.clear()
print(set4)

# del is used to delete a set
set5 = {"apple", "oranges", 2, 5}
del set5
print(set5)