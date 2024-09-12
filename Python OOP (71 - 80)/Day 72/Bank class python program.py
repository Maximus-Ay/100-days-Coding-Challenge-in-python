'''
    This is a simple python program that defines a bank class and methods to deposit withdraw and check balance
'''

class Bank:
    def __init__(self, amount):
        self.amount = amount

    def deposit(self, deposit_amount):
        self.amount = self.amount + deposit_amount
        print(f"{deposit_amount}FCFA succesfully deposited in your account! New Balance: {self.amount}FCFA")

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount > self.amount:
            print(f"Insufficient funds, cannot withdraw {withdrawal_amount}FCFA!")
        else:
            self.amount = self.amount - withdrawal_amount
            print(f"{withdrawal_amount}FCFA has been withdrawn from your account! New Balance: {self.amount}FCFA")

    def check_balance(self):
        print(f"Your balance is: {self.amount}FCFA")

mybank = Bank(20000)
mybank.deposit(5000)
mybank.deposit(10000)
mybank.withdraw(50000)

