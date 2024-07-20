'''
    This is a simple program that finds the factorial of a number using a loop
'''

number = int(input("Enter a number: "))
fact = 1
for x in range(1, number+1):
    fact = fact * x

print(f"{number}! = {fact}")
