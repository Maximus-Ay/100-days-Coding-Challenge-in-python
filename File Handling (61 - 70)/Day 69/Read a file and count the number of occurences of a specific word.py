'''
    This is a simple python program that reads a file and count the number of occurences of a specific word
'''

def count_number_of_occurences(filename, word):
    try:
        with open(filename, "r") as file:
            text = file.read().lower()
            occurences = text.count(word.lower())
        print(f"The word {word} occurs {occurences} times in the file.")
    except FileNotFoundError:
        print("The file in question is not found!")
    except Exception as e:
        print("Enable to count number of occurences: {e}")


filename = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\Copy_of_test_TextFile.txt"
word = input("Enter the word for the number of occurences: ")
count_number_of_occurences(filename, word)