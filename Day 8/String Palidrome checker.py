'''
    STRING PALINDROME CHECKER
    This is a program to check if a string entered by the user is a palindrome.
    A palindrome is a string whose reverse equals the original string itself.


'''
string = input("Enter the string: ")
if string == string[::-1]:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")