# Ask the user their name and favourite color
import datetime

# name = input("What is your name?\t")
# favourite_color = input("What is your favourite color? \t")
#
# print(f"Hey! {name} likes {favourite_color} color")
#
#
# # Calculate the age
import datetime

birth_date = int(input("Enter your year of birth: \t"))

current = datetime.date.today().year
age = int(current) - birth_date
if age > 1:
    print("You are ", age, "years old")
else:
    print("You are ", age, " year old")

