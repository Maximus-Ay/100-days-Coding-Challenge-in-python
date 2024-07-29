'''
    This is a simple program that finds the frequency of each character in a string
    For this, the best suited structure to be used is the dictionary 

'''

string = input("Enter the string: ")

characters = {}

for char in string:
    if char in characters.keys():
        characters[char] += 1
    else:
        characters[char] = 1

for keys,values in characters.items():
    print(f"{keys} : {values} ")
    



