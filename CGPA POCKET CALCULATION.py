# COS202 Assignment
# Personal Pocket CGPA Calculator

print("===== PERSONAL POCKET CGPA CALCULATOR =====")

courses = int(input("Enter number of courses: "))

total_points = 0
total_units = 0

for i in range(courses):
    print("\nCourse", i + 1)

    unit = int(input("Course Unit: "))
    score = int(input("Course Score: "))

    if score >= 70:
        gp = 5
        grade = "A"

    elif score >= 60:
        gp = 4
        grade = "B"

    elif score >= 50:
        gp = 3
        grade = "C"

    elif score >= 45:
        gp = 2
        grade = "D"

    elif score >= 40:
        gp = 1
        grade = "E"

    else:
        gp = 0
        grade = "F"

    print("Grade:", grade)
    print("Grade Point:", gp)

    total_points += gp * unit
    total_units += unit

cgpa = total_points / total_units

print("\n===== RESULT =====")
print("Total Units:", total_units)
print("Total Grade Points:", total_points)
print("CGPA =", round(cgpa, 2))

if cgpa >= 4.50:
    print("Class: First Class")

elif cgpa >= 3.50:
    print("Class: Second Class Upper")

elif cgpa >= 2.40:
    print("Class: Second Class Lower")

elif cgpa >= 1.50:
    print("Class: Third Class")

else:
    print("Class: Pass")