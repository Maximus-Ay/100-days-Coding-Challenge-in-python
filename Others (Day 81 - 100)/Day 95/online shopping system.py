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


# Example usage
shopping_system = OnlineShoppingSystem()

while True:
    print("\nOnline Shopping System")
    print("1. Add product")
    print("2. Remove product")
    print("3. Display products")
    print("4. Add item to cart")
    print("5. Remove item from cart")
    print("6. View cart")
    print("7. Purchase items")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        shopping_system.add_product(product_id, name, price, quantity)
    elif choice == "2":
        product_id = input("Enter product ID: ")
        shopping_system.remove_product(product_id)
    elif choice == "3":
        shopping_system.display_products()
    elif choice == "4":
        product_id = input("Enter product ID: ")
        quantity = int(input("Enter quantity: "))
        if product_id in shopping_system.products:
            product = shopping_system.products[product_id]
            product.quantity = quantity
            shopping_system.shopping_cart.add_item(product)
        else:
            print(f"Product {product_id} not found")
    elif choice == "5":
        product_id = input("Enter product ID: ")
        shopping_system.shopping_cart.remove_item(product_id)
    elif choice == "6":
        shopping_system.shopping_cart.view_cart()
    elif choice == "7":
        shopping_system.purchase_items()
    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")