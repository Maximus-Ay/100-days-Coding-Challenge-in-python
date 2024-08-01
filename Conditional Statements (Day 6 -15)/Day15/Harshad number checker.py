'''
    This is a simple program to check if a number is a Harshad number.
    A Harshad number is a number that is divisible by the sum of its digits

'''
def isHarshad(number):
    total = 0
    temp = number
    while number > 0:
        x = number % 10
        total += x
        number //= 10
    # Checking the divisibility
    if temp % total == 0:
        return True
    else:
        return False


number = int(input("Enter a number: "))
if isHarshad(number):
    print(f"{number} is a Harshad number")
else:
    print(f"{number} is not a Harshad number")
