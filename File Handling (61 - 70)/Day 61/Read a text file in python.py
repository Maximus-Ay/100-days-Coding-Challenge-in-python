'''
    This is a simple python program to read the content of text file in python
'''
try:
    with open("C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("This file does not exist!")

