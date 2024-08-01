'''
    This is a simple python program that finds the multiplication table for a given number.
    I will limit to that number multiplied by 12

'''
number = int(input("Enter a number: "))

print("The multiplication table for the number is: ")
for x in range(1,11):
    print(f"{number} x {x} = {number*x}")

