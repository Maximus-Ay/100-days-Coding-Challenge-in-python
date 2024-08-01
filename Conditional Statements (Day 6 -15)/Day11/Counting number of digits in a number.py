'''
    This is a program that counts the number of digits in a number


'''
def countDigits(number):
    count = 0
    while number > 0:
        count = count + 1
        number = int(number/10)
    
    return count


number = int(input("Enter a number: "))
print(f"The number of digits in {number} is {countDigits(number)}")

