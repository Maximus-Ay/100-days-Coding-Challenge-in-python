'''
    - Write a program to create a class that models a basic school management system with 
      methods to add, remove, and display students and teachers.
'''

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}"

class Student(Person):
    def __init__(self, student_id, name, age, address, grade):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grade = grade

    def __str__(self):
        return f"Student ID: {self.student_id}\n" + super().__str__() + f"\nGrade: {self.grade}"

class Teacher(Person):
    def __init__(self, teacher_id, name, age, address, subject):
        super().__init__(name, age, address)
        self.teacher_id = teacher_id
        self.subject = subject

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}\n" + super().__str__() + f"\nSubject: {self.subject}"

class SchoolManagementSystem:
    def __init__(self):
        self.students = {}
        self.teachers = {}

    def add_student(self, student_id, name, age, address, grade):
        student = Student(student_id, name, age, address, grade)
        self.students[student_id] = student
        print(f"Student added: {name}")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student {student_id} removed")
        else:
            print(f"Student {student_id} not found")

    def display_students(self):
        print("\nRegistered Students:")
        for student in self.students.values():
            print(student)
            print("--------------------")

    def add_teacher(self, teacher_id, name, age, address, subject):
        teacher = Teacher(teacher_id, name, age, address, subject)
        self.teachers[teacher_id] = teacher
        print(f"Teacher added: {name}")

    def remove_teacher(self, teacher_id):
        if teacher_id in self.teachers:
            del self.teachers[teacher_id]
            print(f"Teacher {teacher_id} removed")
        else:
            print(f"Teacher {teacher_id} not found")

    def display_teachers(self):
        print("\nRegistered Teachers:")
        for teacher in self.teachers.values():
            print(teacher)
            print("--------------------")

# Example usage
school_system = SchoolManagementSystem()

while True:
    print("\nSchool Management System")
    print("1. Add student")
    print("2. Remove student")
    print("3. Display students")
    print("4. Add teacher")
    print("5. Remove teacher")
    print("6. Display teachers")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        address = input("Enter student address: ")
        grade = input("Enter student grade: ")
        school_system.add_student(student_id, name, age, address, grade)
    elif choice == "2":
        student_id = input("Enter student ID: ")
        school_system.remove_student(student_id)
    elif choice == "3":
        school_system.display_students()
    elif choice == "4":
        teacher_id = input("Enter teacher ID: ")
        name = input("Enter teacher name: ")
        age = int(input("Enter teacher age: "))
        address = input("Enter teacher address: ")
        subject = input("Enter teacher subject: ")
        school_system.add_teacher(teacher_id, name, age, address, subject)
    elif choice == "5":
        teacher_id = input("Enter teacher ID: ")
        school_system.remove_teacher(teacher_id)
    elif choice == "6":
        school_system.display_teachers()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")
