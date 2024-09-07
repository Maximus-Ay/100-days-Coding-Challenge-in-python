'''
    Python program that reads a file and removes all the blank spaces in a file
'''

def remove_spaces_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        text_without_spaces = text.replace(" ", "")
        with open(filename, "w") as file:
            file.write(text_without_spaces)
        print(f"Spaces removed from {filename}")
    except FileNotFoundError:
        print("The file in question is not found!")
    except Exception as e:
        print(f"Error removing spaces {e}")

filename = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\outputfile.txt"
remove_spaces_in_file(filename)
