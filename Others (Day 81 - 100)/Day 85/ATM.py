'''
    - Write a program to create a class that simulates a simple ATM machine 
      with methods to check balance, deposit, and withdraw money.
'''

class ATM:
    def __init__(self, card_number, pin, balance = 0):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
        self.logged_in = False

    def login(self):
        card_number = input("Enter card number: ")
        pin = input("Enter PIN: ")

        if card_number == self.card_number and pin == self.pin:
            self.logged_in = True
            print("Login Successful!")
        else:
            print("Invalid card number or PIN.")

    def deposit(self):
        if self.logged_in:
            amount = float(input("Enter deposit amount: $"))
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("Please login first")

    def check_balance(self):
        if self.logged_in:
            print(f"Current balance: ${self.balance:.2f}")
        else:
            print("Please login first")

    def withdraw(self):
        if self.logged_in:
            amount = float(input("Enter withdrawal amount: $"))
            if amount > 0 and amount <= self.balance:
              self.balance -= amount
              print(f"Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")
            elif amount <= 0:
                print("Invalid withdrawal amount!")
            else:
                print("Insufficient funds!")
        else:
            print("Please login first")
      
    def logout(self):
        self.logged_in = False
        print("Logged Out")


def main():
    card_number = "1234567890"
    pin = "1234"
    balance = 1000

    atm = ATM(card_number, pin, balance)

    while True:
        if not atm.logged_in:
            print("\nATM Machine")
            print("1. Login")
            print("2. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                atm.login()
            elif choice == "2":
                break
            else:
                print("Invalid choice. Please try again!")
        else:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Logout")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                atm.check_balance()
            elif choice == "2":
                atm.deposit()
            elif choice == "3":
                atm.withdraw()
            elif choice == "4":
                atm.logout()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please Try again")

if __name__ == "__main__":
    main()