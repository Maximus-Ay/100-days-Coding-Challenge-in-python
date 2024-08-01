'''
    This is a simple python program to swap two numbers.
    To swap these two numbers I will make use of a third variable that will be used as a place holder.

'''

# Getting user input
firstNumber = int(input("Enter the first number: "))
secondNumber = int(input('Enter the secind number: '))
# Before Swapping
print(f"Before: first number = {firstNumber} and second number = {secondNumber}")
# Swapping Process
temp = firstNumber
firstNumber = secondNumber
secondNumber = temp
# After Swapping
print(f"After: first number = {firstNumber} and second number = {secondNumber}")