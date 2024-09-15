'''
    This is a class called Manager that inherits from Employee and includes an additional attribute called department
'''

from Employee import Employee

class Manager(Employee):
    def __init__(self, name, ID, salary, department):
        super().__init__(name, ID, salary)
        self.department = department

myManager = Manager("Maximus", 564, 70000, "Engineering")
print(myManager.department)