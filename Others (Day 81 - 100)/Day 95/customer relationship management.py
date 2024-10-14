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
