'''
    This is a python program that reads the last n lines of a text file
'''

def read_last_n_lines(fileName, n):
    try:
        with open(fileName, "r") as file:
            lines = file.readlines()
            last_n_lines = lines[-n:]
            for line in last_n_lines:
                print(line.strip(), end="")
                print()
    except FileNotFoundError:
        print(f"File {fileName} not found!")

fileName = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt"
read_last_n_lines(fileName, 4)