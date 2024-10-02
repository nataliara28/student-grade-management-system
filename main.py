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


# 2. Function to calculate the average grade of each student
def calculate_average(students):
    averages = {}
    for student, grades in students.items():
        averages[student] = sum(grades) / len(grades)
    
    return averages


# 3. Function to find the top student based on average grades
def find_top_student(averages):
    top_student = None
    top_avg = 0
    
    for student, avg in averages.items():
        if avg > top_avg:
            top_avg = avg
            top_student = student
    
    return top_student, top_avg

# 4. Function to classify students as passed or failed / if average is 60 

def classify_students(averages, passing_mark):
    passed_students = []
    failed_students = []
    
    for student, avg in averages.items():
        if avg >= passing_mark:
            passed_students.append(student)
        else:
            failed_students.append(student)
    
    return passed_students, failed_students
    
    
def main():
    num_students = 5
    num_grades = 3
    
    #1. Generate students and grades
    students = generate_grades(num_students, num_grades)
    
    print("Student Grades:")
    for student, grades in students.items():
        print(f"{student}: {grades}")
        
    # 2. Calculate average grades
    averages = calculate_average(students)
    
    print("\nStudents Averages:")
    for student, avg in averages.items():
        print(f'{student}: {avg:.2f}')
    
    # 3. Find the top student
    top_student, top_avg = find_top_student(averages)
    print(f"\nTop Student is: {top_student} with an average of {top_avg:.2f}")
    
    # 4. Classify students who passed or failed
    passed_students, failed_students = classify_students(averages, 60)
    
    if passed_students:
        print('\nPassed Students:')
        for student in passed_students:
            print(student)
    
    if failed_students:
        print('\nFailed Students:')
        for student in failed_students:
            print(student)

if __name__ == "__main__":
    main()