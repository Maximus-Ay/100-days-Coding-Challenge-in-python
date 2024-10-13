'''
    - Write a program to create a class that represents a basic payroll system 
      with methods to calculate and display salaries.
'''

class Employee:
    def __init__(self, employee_id, name, position, salary, hours_worked):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.salary * self.hours_worked

class PayrollSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, name, position, salary, hours_worked):
        employee = Employee(employee_id, name, position, salary, hours_worked)
        self.employees[employee_id] = employee
        print(f"Employee added: {name}")

    def remove_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            print(f"Employee {employee_id} removed")
        else:
            print(f"Employee {employee_id} not found")

    def display_salaries(self):
        print("\nEmployee Salaries:")
        for employee in self.employees.values():
            salary = employee.calculate_salary()
            print(f"Employee ID: {employee.employee_id}")
            print(f"Name: {employee.name}")
            print(f"Position: {employee.position}")
            print(f"Salary: ${salary}")
            print("--------------------")

    def search_employee(self, employee_id):
        if employee_id in self.employees:
            employee = self.employees[employee_id]
            salary = employee.calculate_salary()
            print(f"Employee ID: {employee.employee_id}")
            print(f"Name: {employee.name}")
            print(f"Position: {employee.position}")
            print(f"Salary: ${salary}")
        else:
            print(f"Employee {employee_id} not found")

# Example usage
payroll_system = PayrollSystem()

while True:
    print("\nPayroll System")
    print("1. Add employee")
    print("2. Remove employee")
    print("3. Display salaries")
    print("4. Search employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        employee_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        position = input("Enter position: ")
        salary = float(input("Enter hourly salary: "))
        hours_worked = float(input("Enter hours worked: "))
        payroll_system.add_employee(employee_id, name, position, salary, hours_worked)
    elif choice == "2":
        employee_id = input("Enter employee ID: ")
        payroll_system.remove_employee(employee_id)
    elif choice == "3":
        payroll_system.display_salaries()
    elif choice == "4":
        employee_id = input("Enter employee ID: ")
        payroll_system.search_employee(employee_id)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
