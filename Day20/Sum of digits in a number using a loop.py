'''
    This is a program that makes use of the notion of loops in order to accomplish the task of finding the 
    sum of the digits in a number.
'''

number = int(input("Enter the number: "))
total = 0
temp = number
while number>0:
    last_digit = number % 10
    total += last_digit
    number //=10
print(f"The sum of the digits of the number {temp} = {total}")
