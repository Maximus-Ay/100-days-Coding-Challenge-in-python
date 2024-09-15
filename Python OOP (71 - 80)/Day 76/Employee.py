'''
    Employee class with attributes name, ID, Salary and methods to calculate the annual salary
'''

class Employee:
    def __init__(self,name,ID, salary):
        self.name = name
        self.ID = ID
        self.salary = salary

    def annual_salary(self):
        return f"$ {12 * self.salary}"
    

myEmployee = Employee("Maximus", 1245612, 70000)
print(myEmployee.annual_salary())
