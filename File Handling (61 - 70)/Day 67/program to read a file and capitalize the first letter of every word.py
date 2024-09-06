'''
    Python program to read a file and capitalise every first letter of every word
'''

def capitalise_first_letter(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
        words = text.split()
        capitalized_words = [word.capitalize() for word in words]
        capitalized_text = ''.join(capitalized_words)

        # Writing to the file
        with open(filename, "w") as file:
            file.write(capitalized_text)
        print(f"First letters capitalized in {filename}.")
    except FileNotFoundError:
        print("The file in question was not found among")
    except Exception as e:
        print(f"Error capitalising letters {e}")

filename = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt"
capitalise_first_letter(filename)