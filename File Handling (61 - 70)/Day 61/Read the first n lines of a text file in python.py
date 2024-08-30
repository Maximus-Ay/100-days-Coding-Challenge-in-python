'''
    This is a python program that reads the first n lines of a text file in python
'''

def Read_first_n_lines_of_a_file(fileName, n):
    try:
        with open(fileName, "r") as file:
            for i in range(n):
                line = file.readline()
                if line:
                    print(line.strip())
                else:
                    break
    except FileNotFoundError:
        print("The file doesn't exist or is not found!")

fileName = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt"
Read_first_n_lines_of_a_file(fileName, 2)