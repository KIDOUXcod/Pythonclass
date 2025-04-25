def calculate_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# Input
student_name = input("Enter the student name: ")
grade1 = float(input("Enter a grade: "))
grade2 = float(input("Enter a grade: "))
grade3 = float(input("Enter a grade: "))
grade4 = float(input("Enter a grade: "))
grade5 = float(input("Enter a grade: "))

# Calculate average
average = (grade1 + grade2 + grade3 + grade4 + grade5) / 5

# Determine letter grade
letter_grade = calculate_letter_grade(average)

# Output
print(f"\n{student_name}\n")
print(f"Average: {average:.1f}\n")
print(f"Letter Grade: {letter_grade}")

print("Gradebook by Kidmar Desir")