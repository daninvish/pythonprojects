# Write a program that will accept marks from the user and grades it the following order
# Marks           Grade
# 80 and above      A
# 70 - 79           B
# 60 - 69           C
# 50 - 59           D
#  below 50           Failure

score = int(input("Enter your marks scored:\t"))

if score < 0 or score > 100:
    print(f"Invalid mark, range 0 to 100")
elif score >= 80:
    print("Grade is A")
elif score >= 70:
    print("Grade is B")
elif score >= 60:
    print("Grade is C")
elif score >= 50:
    print("Grade is D")
else:
    print("Grade is F")
    