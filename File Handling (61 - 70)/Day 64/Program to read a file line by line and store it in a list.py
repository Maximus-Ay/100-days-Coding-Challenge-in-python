'''
    This is a simple python program that reads a file line by line and stores it in a list
'''

def Read_file_line_by_line(fileName):
    try:
        with open(fileName, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("The file doesn't exist or is not found!")

fileName = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt"
Read_file_line_by_line(fileName)