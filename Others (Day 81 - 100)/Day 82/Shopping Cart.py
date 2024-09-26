'''
- Write a program to create a simple shopping cart using lists and functions.
'''

cart = []

def display_menu():
    print("\nShopping Cart Menu: ")
    print("1. Add item")
    print("2. Remove item")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: $"))
    quantity = int(input("Enter the item quantity: "))
    cart.append({"name":name, "price":price, "quantity":quantity})
    print(f"Added {quantity} {name}(s) to cart")

def remove_item():
    name = int(input("Enter item name to remove: "))
    for item in cart:
        if item["name"] == name:
            cart.remove(item)
            print(f"Removed {name} from cart.")
            return
    print(f"{name} not found in cart.")

def view_cart():
    if cart:
        print("\nShopping Crat")
        total = 0
        for i, item in enumerate(cart, 1):
            print(f"{i}.{item["name"]}:{item["quantity"]} x ${item["price"]} = ${item["quantity"] * item["price"]:.2f}")
            total += item["quantity"] * item["price"]
        print(f"Total: ${total:.2f}")
    else:
        print("Cart is empty.")

def checkout():
    if cart:
        print("\nCheckout Summary.")
        total = 0
        for item in cart:
            print(f"{item["name"]}:{item["quantity"]} x ${item["price"]} = ${item["quantity"] * item["price"]:.2f}")
            total += item["quantity"] * item["price"]
            print(f"Total: ${total:.2f}")
            cart.clear()
        print("Checkout successful. Cart cleared")
    else:
        print("Cart is empty.")

# Main program
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        checkout()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")