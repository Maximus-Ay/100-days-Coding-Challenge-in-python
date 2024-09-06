'''
    This is a python program that reads a file and replaces a specific word within it by another word from the user
'''

def replace_word_by_another_word(filename, initial_word, replacement_word):
    try:
        with open(filename, "r") as file:
            text = file.read()
            text = text.replace(initial_word, replacement_word)
        with open(filename, "w") as file:
            file.write(text)
        print(f"Word{initial_word} replaced with {replacement_word} in {filename}")
            
    except FileNotFoundError:
        print("The file in question was not found!")
    except Exception as e:
        print(f"Error replacing file {e}")

filename = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt"
replace_word_by_another_word(filename, "additional", "extra")