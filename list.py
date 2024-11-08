my_list = [1,2,3, "apple", "banana"]
print(my_list)

# list slicing
# slicing allows you to extract a part of the list by specifying a start and end index
numbers = [10, 20, 30, 40, 50, 60]
# extracting from index 1 to 3
print(numbers[1:4])
# extracting from the start to index 2
print(numbers[:3])
# extracting from index 2 bto the end
print(numbers[2:])

# Addition of elements in the list
# Creating an empty list
empty_list = []
# adding 10 to the list
empty_list.append(10)
empty_list.append(20)
empty_list.append(30)
empty_list.append(40)
empty_list.append(50)
empty_list.append(60)
print(empty_list)

# adding using the insert()
numbers.insert(2, 90)
print(numbers)
numbers.insert(0, "daniel")
print(numbers)
number1 = [10, 20, 30, 40, 50, 60]
number1.extend([1,2,3,4])
print(number1)
number1.append("daniel")
print(number1)
number1.extend("daniel")
print(number1)

# removing the first occurances of 50
number1.remove(50)
print(number1)
# # removing an element not in the list
# number1.remove(6)
# print(number1) # list.remove(x): x not in list

# removing the last element from the list
number2 = [10, 20, 30, 40, 50, 60, 70, 80]
number2.pop()
print(number2)
# removing an element at index 2 ie. 30
number2.pop(2)
print(number2)

# Substituting the element in the list
# syntax: list[index] = new substitute
number3 = [10, 20, 30, 40, 50, 60, 70, 80]
# substitute element at index 2 with 90
number3[2] = 90
print(number3)
# substituting the last index with my name
number3[7] = "daniel"
print(number3)

age = True
