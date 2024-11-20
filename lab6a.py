#!/usr/bin/env python3
# Author ID: ppayal1

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Ensure student number is stored as a string
        self.courses = {}

    def displayStudent(self):
        return f"Student Name: {self.name}\nStudent Number: {self.number}"

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        if not self.courses:  # Check if the courses dictionary is empty
            return f"GPA of student {self.name} is 0.0"
        total_grades = sum(self.courses.values())
        gpa = total_grades / len(self.courses)
        return f"GPA of student {self.name} is {gpa:.1f}"  # Format to one decimal place

    def displayCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed_courses

if __name__ == "__main__":
    # Create first student object and add grades for each class
    student1 = Student("Alice", "987654321")
    student1.addGrade("math101", 3.0)
    student1.addGrade("eng202", 4.0)
    student1.addGrade("sci303", 2.5)

    # Create second student object and add grades for each class
    student2 = Student("Bob", 123456)  # Testing with an integer student number
    student2.addGrade("comp101", 4.0)
    student2.addGrade("data202", 3.5)
    student2.addGrade("math101", 0.0)

    # Display information for student1
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())

