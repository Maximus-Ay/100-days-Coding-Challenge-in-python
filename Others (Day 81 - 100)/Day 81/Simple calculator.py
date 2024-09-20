'''
    This is a simple calculator that makes use of functions to carry out basic mathematic operations
'''

def Addition(number1, number2):
    return number1 + number2

def Subtraction(number1, number2):
    return number1 - number2

def Multiplication(number1, number2):
    return number1 * number2

def Division(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        print("Cannot divide a number by 0!")

def display_menu():
    print("WELCOME TO MY CALCULATOR!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        print(Addition(number1, number2))
    elif choice == 2:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        print(Subtraction(number1, number2))
    elif choice == 3:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        print(Multiplication(number1, number2))
    elif choice == 4:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        print(Division(number1, number2))
    elif choice == 5:
        print("Thanks for using My Calculator!")
    else:
        print("Invalid Response: ")

display_menu()
