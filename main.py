import random

# 1. Function to generate random grades for students
def generate_grades(num_students, num_grades):
    students = {}
    # Generating name of students
    for i in range(1, num_students + 1):
        student_name = f"Student_{i}"
        # Generate random grades for the students
        grades = [random.randint(50, 100) for _ in range(num_grades)]
        students[student_name] = grades
    
    return students


def main():
    num_students = 5
    num_grades = 3
    
    #1. Generate students and grades
    students = generate_grades(num_students, num_grades)
    
    print("Student Grades:")
    for student, grades in students.items():
        print(f"{student}: {grades}")
        

if __name__ == "__main__":
    main()