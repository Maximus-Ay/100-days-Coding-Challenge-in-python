'''
    This is a simple program that finds the length of a string without using the len() function
'''
string = input("Enter the string: ")
count = 0
for x in string:
    count+=1
print(f"The length of {string} is {count}")
