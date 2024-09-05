'''
    This is a python program that combines each line of the first file and the 
    coresponding line of the second file
'''

def Combine_files(file1, file2, output_file):
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2, open(output_file, "w") as of:
            for line1, line2 in zip(f1, f2):
                of.write(line1.strip() + "" + line2.strip() + "\n")
            print("Files combined Successfully!")
    except FileNotFoundError:
        print("One of the input files were not found!")
    except Exception as e:
        print(f"Error combining files {e}")

file1 = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt"
file2 = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\Copy_of_test_TextFile.txt"
output_file = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\outputfile.txt"
Combine_files(file1, file2, output_file)