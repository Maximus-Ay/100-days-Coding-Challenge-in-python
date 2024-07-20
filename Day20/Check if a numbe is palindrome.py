'''
    This is a simple program that makes use of loops to be able to determine if a number is palindrome or not
'''

def reverse(number):
    reverse = 0
    while number>0:
        last_digit = number % 10
        reverse = reverse * 10 + last_digit
        number //= 10
    
    return reverse

def isPalindrome(number, reverse):
    if number == reverse:
        return True
    else:
        return False
    
number = int(input("Enter the number: "))
print(f"is {number} a palindrome? Answer: {isPalindrome(number, reverse(number))}")


