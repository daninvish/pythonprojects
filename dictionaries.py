# Dictionaries in Python
car = {"Brand": "Toyota",
       "Model": "MvT",
       "Manufacture": "Toyota Co.",
       "Year": "2005"}
print(car.get('Model'))
x = car.keys()
y = car.values()
# print(x, y)

# Update the dictionary
car.update({"Year": "2022"})
print(car)

