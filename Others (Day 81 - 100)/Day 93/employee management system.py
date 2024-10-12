'''
    - Write a Python program to create a class that simulates a basic employee management system 
      with methods to add, remove, and display employees.
'''
class Employee:
    def __init__(self, employee_id, name, age, department, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.department = department
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.employee_id}\nName: {self.name}\nAge: {self.age}\nDepartment: {self.department}\nPosition: {self.position}\nSalary: ${self.salary}"

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, name, age, department, position, salary):
        employee = Employee(employee_id, name, age, department, position, salary)
        self.employees[employee_id] = employee
        print(f"Employee added: {name}")

    def remove_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            print(f"Employee {employee_id} removed")
        else:
            print(f"Employee {employee_id} not found")

    def display_employees(self):
        print("\nRegistered Employees:")
        for employee in self.employees.values():
            print(employee)
            print("--------------------")

    def search_employee(self, employee_id):
        if employee_id in self.employees:
            print(self.employees[employee_id])
        else:
            print(f"Employee {employee_id} not found")

    def update_employee(self, employee_id, name=None, age=None, department=None, position=None, salary=None):
        if employee_id in self.employees:
            if name:
                self.employees[employee_id].name = name
            if age:
                self.employees[employee_id].age = age
            if department:
                self.employees[employee_id].department = department
            if position:
                self.employees[employee_id].position = position
            if salary:
                self.employees[employee_id].salary = salary
            print(f"Employee {employee_id} updated")
        else:
            print(f"Employee {employee_id} not found")
