'''
- Write a Python program to create a class that simulates a basic bank transaction system 
  with methods to transfer money between accounts.
'''

class Account:
    def __init__(self, account_number, account_name, balance=0.0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into account {self.account_number}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount} from account {self.account_number}. New balance: ${self.balance}")

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Name: {self.account_name}\nBalance: ${self.balance}"

class BankTransactionSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_name, initial_balance=0.0):
        if account_number not in self.accounts:
            account = Account(account_number, account_name, initial_balance)
            self.accounts[account_number] = account
            print(f"Account {account_number} created successfully.")
        else:
            print(f"Account {account_number} already exists.")

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} deleted successfully.")
        else:
            print(f"Account {account_number} not found.")

    def transfer_funds(self, sender_account_number, recipient_account_number, amount):
        if sender_account_number in self.accounts and recipient_account_number in self.accounts:
            sender_account = self.accounts[sender_account_number]
            recipient_account = self.accounts[recipient_account_number]
            sender_account.withdraw(amount)
            recipient_account.deposit(amount)
        else:
            print("Sender or recipient account not found.")

    def display_account(self, account_number):
        if account_number in self.accounts:
            print(self.accounts[account_number])
        else:
            print(f"Account {account_number} not found.")

# Example usage
bank_system = BankTransactionSystem()

while True:
    print("\nBank Transaction System")
    print("1. Create account")
    print("2. Delete account")
    print("3. Deposit funds")
    print("4. Withdraw funds")
    print("5. Transfer funds")
    print("6. Display account")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account_number = input("Enter account number: ")
        account_name = input("Enter account name: ")
        initial_balance = float(input("Enter initial balance (default=0): ") or 0)
        bank_system.create_account(account_number, account_name, initial_balance)
    elif choice == "2":
        account_number = input("Enter account number: ")
        bank_system.delete_account(account_number)
    elif choice == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        if account_number in bank_system.accounts:
            bank_system.accounts[account_number].deposit(amount)
    elif choice == "4":
        account_number = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        if account_number in bank_system.accounts:
            bank_system.accounts[account_number].withdraw(amount)
    elif choice == "5":
        sender_account_number = input("Enter sender's account number: ")
        recipient_account_number = input("Enter recipient's account number: ")
        amount = float(input("Enter transfer amount: "))
        bank_system.transfer_funds(sender_account_number, recipient_account_number, amount)
    elif choice == "6":
        account_number = input("Enter account number: ")
        bank_system.display_account(account_number)
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")
