'''
    - Write a Python program to create a class that simulates a basic inventory management system.
'''

class Product:
    def __init__(self,id,name,price,quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.id}, Name: {self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}"
    
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, id, name, price, quantity):
        self.products[id] = Product(id, name, price, quantity)
        print(f"Added {name} to inventory")

    def remove_product(self, id):
        if id in self.products:
            del self.products[id]
            print(f"Removed Product ID {id} from inventory")
        else:
            print(f"Product ID {id} not found in inventory")

    def update_product(self, id, name = None, price=None, quantity=None):
        if id in self.products:
            if name:
                self.products[id].name = name
            if price:
                self.products[id].price = price
            if quantity:
                self.products[id].quantity = quantity
            print(f"Updated Product ID {id} in inventory")
        else:
            print(f"Product ID {id} not found in inventory")
    
    def display_inventory(self):
        print("Current Inventory")
        for product in self.products.values():
            print(product)

    def search_product(self, id):
        if id in self.products:
            print(self.products[id])
        else:
            print(f"Product ID {id} not found in inventory")

def main():
    inventory = Inventory()

    while True:
      print("\nInventory Management System")
      print("1. Add Product")
      print("2. Remove Product")
      print("3. Update Product")
      print("4. Display Product")
      print("5. Search Product")
      print("6. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
        id = int(input("Enter prodcut ID: "))
        name = input("Enter product name: ")
        price = float(input("Enter product price: $"))
        quantity = int(input("Enter product quantity: "))
        inventory.add_product(id, name, price, quantity)
      elif choice == "2":
        id = int(input("Enter product ID to remove: "))
        inventory.remove_product(id)
      elif choice == "3":
        id = int(input("Enter prodcut ID to update: "))
        name = input("Enter product name(Optional): ")
        price = float(input("Enter product price(Optional): $"))
        quantity = int(input("Enter product quantity(Optional): "))
        inventory.update_product(id, name, price, quantity)
      elif choice == "4":
        inventory.display_inventory()
      elif choice == "5":
        id = int(input("Enter product ID to search: "))
        inventory.search_product(id)
      elif choice == "6":
        break
      else:
        print("Invalid choice. Please Try again")

if __name__ == "__main__":
    main()

