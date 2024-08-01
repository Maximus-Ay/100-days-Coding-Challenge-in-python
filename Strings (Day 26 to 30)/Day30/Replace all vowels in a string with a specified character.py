'''
    This is a simple program that replaces all the vowels in a string with a specified character
    I will use the - symbol instead of vowels. Let's see what it gives

'''

string = input("Enter the string: ")
for char in string:
    if char == "a" or char == "A" or char == "e" or char == "E" or char == "i" or char == "I" or char == "o" or char == "O" or char == "u" or char =="U":
        string = string.replace(char, "-")        
print(string)

