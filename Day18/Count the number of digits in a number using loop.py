'''
    This is a simple program that finds the number digits in a number entered by the user.
'''

number = int(input("Enter the number: "))
temp = number
count = 0
while number > 0:
    x = number % 10
    count += 1
    number //= 10
print(f"The number of digits in {temp} is {count}")
