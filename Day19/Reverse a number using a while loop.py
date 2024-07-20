'''
    This is a simple program that reverses a number using the a while loop
'''

number = int(input("Enter the number: "))
temp = number
reverse = 0
while number > 0:
    last_digit = number % 10
    reverse = reverse * 10 + last_digit 
    number //= 10

print(f"The reverse of {temp} is {reverse}")
