'''
    This is a python program to count the number of words in a text file
'''

def Count_words(fileName):
    try:
        with open(fileName, "r") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print("The file you are searching for doesn't exist!")


fileName = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt"
print(Count_words(fileName))