'''
    This is a simple program that counts the number of vowels in a String
    In English Language we have 5 vowels, which are a,e,i,o,u
    and so while moving through the string we will check to see if we
    have any one of these vowels within and add it to a variable we are going to create to store
    the number of vowels.

'''

string = input("Enter the string: ")
count_vowels = 0
for i in string:
    if i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U':
        count_vowels+=1
print(f"The number of vowels in {string} is {count_vowels}")