'''
    This is a simple program that checks if a given year is a leap year.
    A year is a leap year if it is divisible by 4 and if every century year is divisible by 400.
'''

year = int(input("Enter the year: "))

if year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year!")
elif year % 4:
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")

