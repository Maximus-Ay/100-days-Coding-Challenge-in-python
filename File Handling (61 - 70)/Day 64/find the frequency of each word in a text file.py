'''
    This is a python program that finds the frequency of each word in a text file
'''

def frequency_of_words(fileName):
    try:
        with open(fileName, "r") as file:
            text = file.read()
            words = text.split()
            word_count = {}
            for word in words:
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            for word, count in word_count.items():
                print(f"{word}:{count}")
    except FileNotFoundError:
        print("The file in question doesn't exitst!")


fileName = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt"
frequency_of_words(fileName)