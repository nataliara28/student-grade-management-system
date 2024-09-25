# student-grade-management-system

## Description:
Imagine you are the teacher of a coding class, and you need a quick way to manage and analyze the grades of your students. Using Python, you'll develop a Student Grade Management System that automates this process! The system will randomly generate grades for students, calculate their average, identify the top performers, and determine who passed and who failed. This simple but powerful tool will use core programming concepts like loops, functions, and data structures such as lists and dictionaries. Let’s build this system and help you automate the tedious task of managing student performance!

### 1. Student Grade Generation:
In this section, we'll create a function that generates random grades for each student. We'll use the random module to assign random scores between 50 and 100 for a specified number of students. The result will be stored in a dictionary where student names are the keys, and their grades (as lists) are the values.

### 2. Calculating Average Grades:
Once we have the student grades, we need to calculate the average for each student. This section defines a function that iterates through the dictionary and computes the average score for each student by summing their grades and dividing by the number of grades.

### 3. Identifying the Top Student:
Here, we’ll write a function that identifies the student with the highest average score. We’ll loop through the dictionary of averages to find the student who tops the class.

### 4. Classifying Students (Passed or Failed):
This section defines a while loop that classifies students based on their average grade. If their average is 60 or higher, they pass; otherwise, they fail. This helps simulate a real-world grading scenario.
