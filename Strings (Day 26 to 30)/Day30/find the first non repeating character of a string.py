'''
    This is a simple program that finds and returns the first non repeating character of a string.

'''
def first_non_repeating_character_in_string(string):
    characters = {}
    for x in string:
        if x in characters.keys():
            characters[x] += 1
        else:
            characters[x] = 1
    for x in string:
        if characters[x] == 1:
            return x
    return None

string = input("Enter a string: ")

print(f"The first non repeating character in {string} is {first_non_repeating_character_in_string(string)}")

