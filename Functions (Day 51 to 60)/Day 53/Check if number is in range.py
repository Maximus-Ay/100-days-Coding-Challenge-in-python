'''
    This is a simple python program that checks if a number is within a range
'''

def CheckRange(number, max_number, min_number):
    if number in range(min_number, max_number+1):
        return True
    else:
        return False
    
min_number = int(input("Enter the minimum number in the range: "))
max_number = int(input("Enter the maximum number in the range: "))
number = int(input("Enter the number you want to check: "))

print(CheckRange(number, max_number, min_number))


