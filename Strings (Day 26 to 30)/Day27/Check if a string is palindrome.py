'''
    This is a simple program that checks if a string is a palindrome
'''

string = input("Enter the string: ")
if string == string[::-1]:
    print(f"{string} is palindrome")
else:
    print(f"{string} is not palindrome")
    