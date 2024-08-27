'''
    This is a simple python function that checks if a string is a paindrome
'''

def Check_if_Palindrome(my_String):
    if my_String == my_String[::-1]:
        return True
    else:
        return False
    
myString = input("Enter the string to check if palindrome: ")
print(f"Answer: {Check_if_Palindrome(myString)}")