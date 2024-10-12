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

# Example usage
employee_system = EmployeeManagementSystem()

while True:
    print("\nEmployee Management System")
    print("1. Add employee")
    print("2. Remove employee")
    print("3. Display employees")
    print("4. Search employee")
    print("5. Update employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        employee_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        department = input("Enter department: ")
        position = input("Enter position: ")
        salary = float(input("Enter salary: "))
        employee_system.add_employee(employee_id, name, age, department, position, salary)
    elif choice == "2":
        employee_id = input("Enter employee ID: ")
        employee_system.remove_employee(employee_id)
    elif choice == "3":
        employee_system.display_employees()
    elif choice == "4":
        employee_id = input("Enter employee ID: ")
        employee_system.search_employee(employee_id)
    elif choice == "5":
        employee_id = input("Enter employee ID: ")
        name = input("Enter new name (or leave blank): ")
        age = input("Enter new age (or leave blank): ")
        department = input("Enter new department (or leave blank): ")
        position = input("Enter new position (or leave blank): ")
        salary = input("Enter new salary (or leave blank): ")
        name = name if name else None
        age = int(age) if age else None
        salary = float(salary) if salary else None
        employee_system.update_employee(employee_id, name, age, department, position, salary)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
