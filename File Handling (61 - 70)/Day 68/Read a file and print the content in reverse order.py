'''
    This is a python program that reads a file and prints its content in reverse order
'''

def print_file_in_reverse(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in reversed(lines):
                print(line.strip()[::-1])
    except FileNotFoundError:
        print("The file in question is not found!")
    except Exception as e:
        print(f"Erro reading file: {e}")
    
filename = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt"
print_file_in_reverse(filename)