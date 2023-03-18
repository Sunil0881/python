n = int(input("Enter the number of courses: "))
grades = []
credit_hours = []
total_credit_hours = 0
total_grade_points = 0

# Loop to input grades and credit hours for each course
for i in range(n):
    grade = input(f"Enter grade for course {i+1}: ")
    credit_hour = int(input(f"Enter credit hours for course {i+1}: "))
    grades.append(grade)
    credit_hours.append(credit_hour)
    total_credit_hours += credit_hour

# Loop to calculate grade points and total grade points
for i in range(n):
    if grades[i] == "A":
        grade_point = 4.0
    elif grades[i] == "A-":
        grade_point = 3.7
    elif grades[i] == "B+":
        grade_point = 3.3
    elif grades[i] == "B":
        grade_point = 3.0
    elif grades[i] == "B-":
        grade_point = 2.7
    elif grades[i] == "C+":
        grade_point = 2.3
    elif grades[i] == "C":
        grade_point = 2.0
    elif grades[i] == "C-":
        grade_point = 1.7
    elif grades[i] == "D+":
        grade_point = 1.3
    elif grades[i] == "D":
        grade_point = 1.0
    else:
        grade_point = 0.0
    total_grade_points += grade_point * credit_hours[i]

# Calculate the CGPA
cgpa = total_grade_points / total_credit_hours

# Print the CGPA
print(f"Your CGPA is: {cgpa:.2f}")
