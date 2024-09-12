'''
    Python program to read a file and append text to it
'''

def Read_and_Append(filename, text):
    try:
        with open(filename, "a") as file:
            file.write(text + "\n")
        print("Text appended to the file succesful")
    except FileNotFoundError:
        print("The file in question is not found!")
    except Exception as e:
        print("Unable to append to file: {e}")

filename = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt"
text = input("Enter the text to append: ")
Read_and_Append(filename, text)