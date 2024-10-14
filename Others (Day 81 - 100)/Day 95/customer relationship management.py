'''
    - Write a Python program to create a class that models a basic customer relationship management (CRM) system 
      with methods to add, remove, and display customer information.
'''

class Customer:
    def __init__(self, customer_id, name, email, phone, address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"Customer ID: {self.customer_id}\nName: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {self.address}"

class CRMSystem:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer_id, name, email, phone, address):
        customer = Customer(customer_id, name, email, phone, address)
        self.customers[customer_id] = customer
        print(f"Customer added: {name}")

    def remove_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print(f"Customer {customer_id} removed")
        else:
            print(f"Customer {customer_id} not found")

    def display_customers(self):
        print("\nRegistered Customers:")
        for customer in self.customers.values():
            print(customer)
            print("--------------------")

    def search_customer(self, customer_id):
        if customer_id in self.customers:
            print(self.customers[customer_id])
        else:
            print(f"Customer {customer_id} not found")

    def update_customer(self, customer_id, name=None, email=None, phone=None, address=None):
        if customer_id in self.customers:
            if name:
                self.customers[customer_id].name = name
            if email:
                self.customers[customer_id].email = email
            if phone:
                self.customers[customer_id].phone = phone
            if address:
                self.customers[customer_id].address = address
            print(f"Customer {customer_id} updated")
        else:
            print(f"Customer {customer_id} not found")
            
# Example usage
crm_system = CRMSystem()

while True:
    print("\nCustomer Relationship Management System")
    print("1. Add customer")
    print("2. Remove customer")
    print("3. Display customers")
    print("4. Search customer")
    print("5. Update customer")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        customer_id = input("Enter customer ID: ")
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        phone = input("Enter customer phone: ")
        address = input("Enter customer address: ")
        crm_system.add_customer(customer_id, name, email, phone, address)
    elif choice == "2":
        customer_id = input("Enter customer ID: ")
        crm_system.remove_customer(customer_id)
    elif choice == "3":
        crm_system.display_customers()
    elif choice == "4":
        customer_id = input("Enter customer ID: ")
        crm_system.search_customer(customer_id)
    elif choice == "5":
        customer_id = input("Enter customer ID: ")
        name = input("Enter new name (or leave blank): ")
        email = input("Enter new email (or leave blank): ")
        phone = input("Enter new phone (or leave blank): ")
        address = input("Enter new address (or leave blank): ")
        name = name if name else None
        email = email if email else None
        phone = phone if phone else None
        address = address if address else None
        crm_system.update_customer(customer_id, name, email, phone, address)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")