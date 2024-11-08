from datetime import datetime

import pandas as pd
# import datetime
# datestamp = str(datetime.datetime.now())
# print(datestamp)

# Initialize an empty list to store student data
student_data = []
student_number = int(input("Enter the nuber of students:  "))
for i in range(student_number):
    name = input(f"Enter the name of student {i + 1}:\t")
    while True:
        try:
            score = int(input(f"Enter marks scored for student {i + 1} (0-100):\t"))
            if score < 0 or score > 100:
                print("Invalid mark, range 0 to 100")
            else:
                # Determine the grade based on the score
                if score >= 80:
                    grade = "A"
                elif score >= 70:
                    grade = "B"
                elif score >= 60:
                    grade = "C"
                elif score >= 50:
                    grade = "D"
                else:
                    grade = "F"

                # Append the name, score, and grade to the list
                student_data.append({"Name": name, "Score": score, "Grade": grade})
                break  # Exit the loop when a valid score is entered
        except ValueError:
            print("Please enter a valid integer.")

# Create a DataFrame from the list of student data
df = pd.DataFrame(student_data)
# Save the DataFrame to an Excel file
df.to_excel(f"student_scores4.xlsx", index=False)

print("Scores and grades saved to student_scores.xlsx")