"""
    Author: Santiago Mendivil
    
    Date: 2025-02-09
    
    Description: 
        Immutable data types are a python's data structure
        that cannot be changed after it has been created. Usage
        of namedtuple in Python provides a convenient way to
        create immutable data types. This is useful when you
        want to identify the fields of a record without
        having to manually look a the index of the value. 
"""
from collections import namedtuple
import datetime

Student = namedtuple("Student", ["Name", "Batch", "Entry"])

def enroll_student(name: str, batch_number: int, entry_date: datetime.date) -> Student:
    """Method that enrolls a new student

    Args:
        name (str): Name of the student
        batch_number (int): Batch number of the student
        entry_date (datetime.date): Entry date of the student

    Returns:
        Student: Student object with the name, batch number and entry date
    """
    return Student(name, batch_number, entry_date)

def display_student_info(student: Student) -> None:
    """Method that displays the information of a student

    Args:
        student (Student): Student object with the name, batch number and entry date
    """
    print(f"Name: {student.Name}")
    print(f"Batch number: {student.Batch}")
    print(f"Entry date: {student.Entry}")

students = []

while True:
    print("\nStudent Management System")
    print("1. Enroll a new student")
    print("2. Display student information")
    print("3. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice")
        continue
    if choice == 1:
        student_name = input("Enter student's name: ")
        student_batch_number = int(input("Enter batch number: "))
        student_entry_date = datetime.datetime.strptime(
            input("Enter entry date (YYYY-MM-DD): "), "%Y-%m-%d").date()
        result = enroll_student(student_name, student_batch_number, student_entry_date)
        students.append(result)
    elif choice == 2:
        if students:
            for student_i in enumerate(students):
                print(f"{student_i[0] + 1}. {student_i[1].Name}")
        else:
            print("No students enrolled yet")
            continue
        try:
            student_name = int(input("Enter student's number: "))
            display_student_info(students[student_name - 1])
        except KeyError:
            print("Student not found")
    else:
        break
