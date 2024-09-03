'''
    A program that writes a list to a text file
'''

def Write_To_Text_File(fileName, list):
    try:
        with open(fileName, "w") as file:
            for item in list:
                file.write(str(item) + "\n")
    except FileNotFoundError:
        print("The file in question doesn't exist!")

fileName = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt"
myList = ["Hello my name ", "is additional content", "I am some random", "additional content added",  "into the test Text file"]
Write_To_Text_File(fileName, myList)