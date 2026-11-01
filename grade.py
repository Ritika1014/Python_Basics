# Student Grade Program

marks = float(input("Enter the student's marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("Grade A")
elif marks > 75 and marks < 90:
    print("Grade B")
elif marks > 50 and marks <= 75:
    print("Grade C")
else:
    print("Grade F")
