'''
    - Write a program to create a class that simulates a simple online shopping system 
      with methods to add, remove, and purchase items.
'''

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}\nName: {self.name}\nPrice: ${self.price}\nQuantity: {self.quantity}"

class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.total = 0

    def add_item(self, product):
        if product.product_id in self.items:
            self.items[product.product_id]["quantity"] += product.quantity
        else:
            self.items[product.product_id] = {"product": product, "quantity": product.quantity}
        print(f"Added {product.name} to cart")

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
            print(f"Removed product {product_id} from cart")
        else:
            print(f"Product {product_id} not found in cart")

    def view_cart(self):
        print("\nShopping Cart:")
        for item in self.items.values():
            print(item["product"])
            print(f"Quantity: {item['quantity']}")
            print("--------------------")

    def calculate_total(self):
        self.total = sum(item["product"].price * item["quantity"] for item in self.items.values())
        return self.total

class OnlineShoppingSystem:
    def __init__(self):
        self.products = {}
        self.shopping_cart = ShoppingCart()

    def add_product(self, product_id, name, price, quantity):
        product = Product(product_id, name, price, quantity)
        self.products[product_id] = product
        print(f"Added product {name}")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Removed product {product_id}")
        else:
            print(f"Product {product_id} not found")

    def display_products(self):
        print("\nAvailable Products:")
        for product in self.products.values():
            print(product)
            print("--------------------")

    def purchase_items(self):
        self.shopping_cart.view_cart()
        total = self.shopping_cart.calculate_total()
        print(f"\nTotal: ${total}")
        self.shopping_cart.items.clear()
        self.shopping_cart.total = 0
        print("Purchase successful")
