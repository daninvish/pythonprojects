# Complex numbers
x =2 + 3j
y = 4 - 1j
print(x, "and", y)
print(x+y)

# String
name = "Dr.Rukidi"
print(name)
# Accessing the 5th character on the string
print(name[4])
# String functions
# Capitalize() function
sample = "i love the game, kill the runner game"
print(sample.capitalize())
# Startwith() function and will return true if true and false if false
print(sample.startswith('i'))
# count() function. returns the number of time a specific value appear in a string
print("game appears in the string", sample.count('game'), "times")
# find() function searches the string for a specified value and returns the position of where it is found
print(sample.find('kill'), 'is the position of the \'kill\' in the string')
# upper() function converts a string into uppercase
print(sample.upper())
# lower() function converts a string into the lower case
sample2 = "I LOVE THE GAME, KILL THE RUNNER GAME"
print(sample2.lower())
# strip() function returns a trimmed version of the string
st = "            i love the game,kill the runner game       "
print(st.strip())
