# Write a python program to find grade of a student in diploma Curriculum.
def find_grade_letter(marks):
    try:
        marks = float(marks)
        if marks < 0 or marks > 100:
            return "Marks should be between 0 and 100."
        if marks >= 80:
            return 'A+'
        elif marks >= 75:
            return 'A'
        elif marks >= 70:
            return 'A-'
        elif marks >= 65:
            return 'B+'
        elif marks >= 60:
            return 'B'
        elif marks >= 55:
            return 'B-'
        elif marks >= 50:
            return 'C+'
        elif marks >= 45:
            return 'C'
        elif marks >= 40:
            return 'D'
        else:
            return 'F'
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Example usage
mark = input("Mark = ")
print(find_grade_letter(mark))
