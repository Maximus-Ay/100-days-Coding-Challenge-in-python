'''
    This is a simple program to check if a given number is a perfect number or not
    A perfect number is a number in which the sum of its proper divisors equalts that 
    number e.g 6 = 1 + 2 + 3 (which are the divisors of 6)

'''
# Function to check is a number is perfect
def isPerfectNum(number):
    temp = number
    Sum = 0
    for num in range(1, number):
        if number % num == 0:
            Sum += num
        
    if Sum == number:
        return True
    else:
        return False

number = int(input("Enter a number: "))
if isPerfectNum(number):
    print(f"{number} is a perfect number!")
else:
    print(f"{number} is not a perfect number!")
