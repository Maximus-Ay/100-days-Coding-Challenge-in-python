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
