'''
    This is a python program to read a file, and print all its numbers or numeric values
'''

def Read_File_Return_Values(fileName):
    try:
        with open(fileName, "r") as file:
            text = file.read()
            numbers = [float(num) for num in text.split() if num.replace('.','', 1).isdigit()]
            return numbers
    except FileNotFoundError:
        print(f"File {fileName} not found!")
        return []
    except Exception as e:
        print(f"Error reading numbers {e}")
        return []
                

file1 = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt"
print(Read_File_Return_Values(file1))