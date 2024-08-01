'''
    This is a simple program that finds the multiplication table of a given number in python
'''

number = int(input("Enter a number: "))
print(f"The multiplication table of {number} up to 12 is: ")
for x in range(1, 13):
    print(f"{number} x {x} = {number * x}")

