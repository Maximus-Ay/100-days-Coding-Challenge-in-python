'''
    This is a python program that copies the content of one text file to another one
'''

def Copy_contents_of_text_file(fileName, CopyFileName):
    try:
        with open(fileName, "r") as source_file:
            with open(CopyFileName, "w") as destination_file:
                destination_file.write(source_file.read())
        print("Contents copied succesfully")

    except FileNotFoundError:
        print("Source file not found!")
    except Exception as e:
        print(f"Error copying file contents: {e}")

filename = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\TestTextFile.txt"
copyfileName = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\Copy_of_test_TextFile.txt"
Copy_contents_of_text_file(filename, copyfileName)