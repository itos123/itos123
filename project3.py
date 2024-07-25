def Caculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

marks = float(input("Enter your marks: "))
grade = Caculate_grade(marks)

print(f"Your grade is: {grade}")