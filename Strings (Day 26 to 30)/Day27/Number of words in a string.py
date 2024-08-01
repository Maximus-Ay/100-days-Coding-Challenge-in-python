'''
    This is a simple program that finds the number of words in a string

'''
string = " "
while string == " ":
    string = input("Enter the string: ")
print(f"The number of words in the string is: {string.count(' ') + 1}")
 
