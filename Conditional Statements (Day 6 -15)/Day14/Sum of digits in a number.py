'''
    This is a program that makes use of conditional statements to find the sum of all the digits of a number

'''
number = int(input("Enter the number: "))
total = 0
temp = number
while number>0:
    x = number % 10
    total += x
    number //= 10

print(f"The sum of all the digits in {temp} is: {total}")
