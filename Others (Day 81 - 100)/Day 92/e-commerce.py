'''
    - Write a Python program to create a class that represents a simple e-commerce system 
      with methods to add, remove, and display products.
'''
class Product:
    def __init__(self, product_id, name, price, description):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"Product ID: {self.product_id}\nName: {self.name}\nPrice: ${self.price}\nDescription: {self.description}"

class ECommerceSystem:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price, description):
        product = Product(product_id, name, price, description)
        self.products[product_id] = product
        print(f"Product added: {name}")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product {product_id} removed")
        else:
            print(f"Product {product_id} not found")

    def display_products(self):
        print("\nAvailable Products:")
        for product in self.products.values():
            print(product)
            print("--------------------")

    def search_product(self, product_id):
        if product_id in self.products:
            print(self.products[product_id])
        else:
            print(f"Product {product_id} not found")

    def update_product(self, product_id, name=None, price=None, description=None):
        if product_id in self.products:
            if name:
                self.products[product_id].name = name
            if price:
                self.products[product_id].price = price
            if description:
                self.products[product_id].description = description
            print(f"Product {product_id} updated")
        else:
            print(f"Product {product_id} not found")

# Example usage
ecommerce_system = ECommerceSystem()

while True:
    print("\nE-Commerce System")
    print("1. Add product")
    print("2. Remove product")
    print("3. Display products")
    print("4. Search product")
    print("5. Update product")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        description = input("Enter product description: ")
        ecommerce_system.add_product(product_id, name, price, description)
    elif choice == "2":
        product_id = input("Enter product ID: ")
        ecommerce_system.remove_product(product_id)
    elif choice == "3":
        ecommerce_system.display_products()
    elif choice == "4":
        product_id = input("Enter product ID: ")
        ecommerce_system.search_product(product_id)
    elif choice == "5":
        product_id = input("Enter product ID: ")
        name = input("Enter new product name (or leave blank): ")
        price = input("Enter new product price (or leave blank): ")
        description = input("Enter new product description (or leave blank): ")
        name = name if name else None
        price = float(price) if price else None
        ecommerce_system.update_product(product_id, name, price, description)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
