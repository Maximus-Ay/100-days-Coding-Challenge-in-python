'''
    This python program defines a class called Student and displays the different details of a student
'''

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_student_details(self):
        return f"Student Details:\nName: {self.name}\nAge: {self.age}\nGrade: {self.grade}"
    

student1 = Student("Maximus", 20, 3.9)
student2 = Student("John", 19, 3.5)
print(student1.display_student_details())
print(student2.display_student_details())
