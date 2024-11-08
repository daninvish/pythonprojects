# Python program to calculate the grade of the mark scored
print("============================")
print("============================")
print("Grade Calculator for Campus Students")
score_input = input("Enter the marks scored: ")
# Check the score entered
try:
    score = float(score_input)
except ValueError:
    print("Invalid Score: Range is 0 to 100")
else:
    # Test the score
    if score < 0 or score > 100:
        print("Invalid Marks, Range 0 to 100")
    elif score == 0:
        print("You are almost becoming a fool")
    if score < 50:
        print('Grade is F')
    elif score < 55:
        print("Grade is D")
    elif score < 60:
        print("Grade is D+")
    elif score < 65:
        print("Grade is C")
    elif score < 70:
        print("Grade is C+")
    elif score < 75:
        print("Grade is B")
    elif score < 80:
        print("Grade is B+")
    elif score <= 100:
        print("Grade is A")
    else:
        print("Bye")

    print("========================")
