'''
    This is a simple program that uses the notion of functions to find the number of letters in a 
    string that are upper case and lower case letters.
'''

def Count_lower_and_upper(myString):
    count_upper = 0
    count_lower = 0
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for x in myString:
        if x in lower:
            count_lower += 1
        if x in upper:
            count_upper += 1

    return f"The number of lower case letters are: {count_lower} and upper case letters are: {count_upper}"

print(Count_lower_and_upper("Maximusthemodel12ApashTHKIJI"))
