'''
    - Write a program to create a class that models a simple bank account and 
      includes methods for deposit, withdrawal, and balance inquiry.
'''
class BankAccount:
    def __init__(self, account_number, account_name, initial_balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}.New Balance: ${self.balance:.2f}")
        else:
            print("invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}.New Balance: ${self.balance:.2f}")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient funds!")
    
    def check_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
def main():
    account_number = input("Enter account number: ")
    account_name = input("Enter account name: ")
    initial_balance = float(input("Enter your initial balance: (default = 0) " or 0))

    account = BankAccount(account_number, account_name, initial_balance)

    while True:
        print("\nBank Account Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the deposit amount: $"))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: $"))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please Try again.")

if __name__ == "__main__":
    main()
  
