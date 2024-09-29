'''
    - Write a program to create a class that represents a restaurant menu with methods 
      to add, remove, and display items.
'''

class MenuItem:
  def __init__(self, name, description, price):
    self.name = name
    self.description = description
    self.price = price

  def __str__(self):
    return f"{self.name}:{self.description}, $ {self.price}"
  
class RestaurantMenu:
  def __init__(self):
    self.menu = {}

  def add_item(self, name, description, price):
    self.menu[name] = MenuItem(name, description, price)
    print(f"Added {name} to menu")

  def remove_item(self, name):
    if name in self.menu:
      del self.menu[name]
      print(f"Removed {name} from menu")
    else:
      print(f"{name} not found in menu")
  
  def display_menu(self):
    print("\nRestaurant Menu")
    for item in self.menu.values():
      print(item)

def main():
   menu = RestaurantMenu()

   while True:
      print("\nMenu Management System")
      print("1. Add Item")
      print("2. Remove Item")
      print("3. Display Menu")
      print("4. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
        name = input("Enter item name: ")
        description = input("Enter item description: ")
        price = float(input("ENter item price: $"))
        menu.add_item(name, description, price)
      elif choice == "2":
        name = input("Enter item  to remove: ")
        menu.remove_item(name)
      elif choice == "3":
        menu.display_menu()
      elif choice == "4":
        break
      else:
        print("Invalid choice. Please Try again")

if __name__ == "__main__":
    main()