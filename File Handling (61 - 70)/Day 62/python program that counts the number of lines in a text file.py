'''
    This is a python program that counts the number of lines in a text file
'''

def count_number_of_lines(fileName):
    try:
        with open(fileName, "r") as file:
            n = file.readlines()
            return len(n)
    except FileNotFoundError:
        print("The file doesn't exist!")

fileName = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt"
print(count_number_of_lines(fileName))