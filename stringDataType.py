# operations performed on the string
# 1. Concatenation: Combine two or more strings using the '+' operator
str1 = "Hello"
str2 = "World"
name = "Daniel"
Greetings = str1 + "Kidi " + name
print(Greetings)
# 2. Repetition: A string can be repeated a specified number of times using '*' operator
repeated = "hello"*3
print(repeated)
# 3. String length: len() is used to get the length of the string
Length = len("python")
print(Length)
study_level = "University"
print(len(study_level))
# 4. Replacing substrings: replace() is used to replace the occurrences of a substring with another string.
text = "she likes apples"
new_text = text.replace("apples", "bananas")
print(new_text)

status = "I live in Lira"
new_status = status.replace("Lira", "Angwetangwet")
print(new_status)
fruit = "banana"
new_fruit = fruit.replace('a', 'e')
print(new_fruit)

# 5. Counting occurrences: count() is used to count the number of times a substring appears in a string
comment = "I love apples, apples are my favourite fruit"
new_comment = comment.count("apples")
print("apples appears", new_comment)

city = "kampala"
new_city = city.count('a')
print(new_city)

# 6. Splitting Strings: split() is used to split a string into a list of substring
#    By default, it splits at a whitespace
jungle = "welcome to the jungle"
new_jungle = jungle.split()
print(new_jungle)  # output ['welcome', 'to', 'the', 'jungle']
# Split at a specific character
jungle2 = "welcome, to the jungle"
new_jungle2 = jungle2.split(',')
print(new_jungle2)
clas = "I am in this class, because i have passion for ICT"
new_clas = clas.split("because")
print(new_clas)

# 7. Converting cases:
# upper(): Converts the string to uppercase
text1 = "HEllo word"
upper_text1 = text1.upper()
print(upper_text1)
# lower(): Converts the string to lowercase
lower_text1 = text1.lower()
print(lower_text1)
# title(): Converts the first character of each word to uppercase
title_text1 = text1.title()
print(title_text1)
# capitalize(): Converts only the first character of the string to uppercase
capitalized_text1 = text1.capitalize()
print(capitalized_text1)
# swapcase(): Converts uppercase character to lowercase and vice vasa
swapcase_text1 = text1.swapcase()
print(swapcase_text1)
# 8. Checking the string contents
test = "university"
# startswith(): checks if the string starts with a particular substring
print(test.startswith("un"))
# endswith(): checks if the string ends with a particular substring
print(test.endswith("ty"))
# isalnum(): checks if the string consist of alphanumeric characters(letters and numbers)
print(test.isalnum())
# isalpha(): checks if the string consist of only the alphabetic characters
print(test.isalpha())
# isdigit(): checks if the string consists of only the digits.
print(test.isdigit())
# isspace(): checks if the string consists of only whitespace.
print(test.isspace())

# Indexing a string
# positive indexing
campus = "LIRA UNIVERSITY"
# printing university only
print(campus[5:])
print(campus[-10:])
print(campus[: -10])
print(campus[5:])
