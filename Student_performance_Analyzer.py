"""
STUDENT MARKS & GRADE CALCULATOR
Beginner-friendly Python mini project

How to run:
1. Open this file in Python IDLE or VS Code.
2. Run the file.
3. Enter the student's name and marks when asked.
"""

def get_marks(subject):
    """Ask for marks until the user enters a valid number from 0 to 100."""
    while True:
        try:
            marks = float(input(f"Enter {subject} marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def calculate_grade(percentage):
    """Return a grade based on the percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def main():
    print("=" * 48)
    print("       STUDENT MARKS & GRADE CALCULATOR")
    print("=" * 48)

    student_name = input("Enter student name: ").strip()
    while not student_name:
        print("Name cannot be empty.")
        student_name = input("Enter student name: ").strip()

    subjects = ["English", "Computer", "Mathematics", "Science", "Hindi"]
    results = {}

    for subject in subjects:
        results[subject] = get_marks(subject)

    total = sum(results.values())
    maximum_marks = len(subjects) * 100
    percentage = total / len(subjects)
    grade = calculate_grade(percentage)
    status = "PASS" if all(mark >= 33 for mark in results.values()) else "NEEDS IMPROVEMENT"

    print("\n" + "=" * 48)
    print("                 STUDENT RESULT")
    print("=" * 48)
    print(f"Student Name : {student_name}")
    print("-" * 48)

    for subject, marks in results.items():
        print(f"{subject:<20}: {marks:>6.1f}/100")

    print("-" * 48)
    print(f"Total Marks  : {total:.1f}/{maximum_marks}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")
    print(f"Result       : {status}")
    print("=" * 48)

    # Save a copy of the result in a text file.
    with open("student_result.txt", "w", encoding="utf-8") as file:
        file.write("STUDENT MARKS & GRADE CALCULATOR\n")
        file.write(f"Student Name: {student_name}\n")
        for subject, marks in results.items():
            file.write(f"{subject}: {marks:.1f}/100\n")
        file.write(f"Total: {total:.1f}/{maximum_marks}\n")
        file.write(f"Percentage: {percentage:.2f}%\n")
        file.write(f"Grade: {grade}\n")
        file.write(f"Result: {status}\n")

    print("\nYour result has also been saved in student_result.txt")


if __name__ == "__main__":
    main()
