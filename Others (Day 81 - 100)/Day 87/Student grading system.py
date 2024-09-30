'''
    - Write a Python program to create a class that models a student grading system.
'''

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, course, grade):
        self.grades[course] = grade
        print(f"Added grade for {course}:{grade}")

    def remove_grade(self, course):
        if course in self.grades:
            del self.grades[course]
            print(f"Removed grade for {course}")
        else:
            print(f"No grade found for {course}")

    def calculate_gpa(self):
        total_credits = len(self.grades)
        if total_credits == 0:
            return 0
        total_grade_points = sum(self.convert_grade_to_points(grade) for grade in self.grades.values())

    @staticmethod
    def convert_grade_to_points(grade):
        grade_points = {
            'A': 4,
            'A-': 3.7,
            'B+': 3.3,
            'B': 3,
            'B-': 2.7,
            'C+':2.3,
            'C':2,
            'C-':1.7,
            'D+': 1.3,
            'D':1,
            'F':0
        }
        return grade_points.get(grade.upper(), 0)

    def display_grades(self):
        print("\nStudent Grades")
        for course, grade in self.grades.items():
            print(f"{course}:{grade}")
        print(f"GPA: {self.calculate_gpa():.2f}")

class GradeSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, student_id):
        self.students[student_id] = Student(name, student_id)
        print(f"Added student {name} with ID {student_id}")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Removed student with ID {student_id}")
        else:
            print(f"No student found with ID {student_id}")

    def display_student_grades(self, student_id):
        if student_id in self.students:
            self.students[student_id].display_grades()
        else:
            print(f"No Student found with ID {student_id}")

def main():
    grade_system = GradeSystem()
    
    while True:
      print("\nGrade System Menu")
      print("1. Add Student")
      print("2. Remove Student")
      print("3. Add grade")
      print("4. Remove grade")
      print("5. Display Student Grades")
      print("6. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
        name = input("Enter student name: ")
        student_id = input("Enter Student ID: ")
        grade_system.add_student(name, student_id)
      elif choice == "2":
        student_id = input("Enter Student ID to remove: ")
        grade_system.remove_student(student_id)
      elif choice == "3":
        student_id = input("Enter student ID: ")
        course = input("Enter course: ")
        grade = int(input("Enter grade: "))
        if student_id in grade_system.students:
            grade_system.students[student_id].add_grade(course, grade)
        else:
            print(f"No student found with ID {student_id}")
      elif choice == "4":
        student_id = input("Enter student ID: ")
        course = input("Enter course to remove: ")
        if student_id in grade_system.students:
            grade_system.students[student_id].remove_grade(course)
        else:
            print(f"No student found with ID {student_id}")
      elif choice == "5":
        student_id = input("Enter student ID: ")
        grade_system.display_student_grades(student_id)
      elif choice == "6":
          break
      else:
            print("Invalid choice. Please Try again")

if __name__ == "__main__":
    main()
    