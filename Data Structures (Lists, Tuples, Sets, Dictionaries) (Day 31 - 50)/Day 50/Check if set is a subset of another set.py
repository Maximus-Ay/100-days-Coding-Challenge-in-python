'''
    This is a simple python program that checks to find if a set is a subset of another set
'''

set1 = {1,2,3,4,5,6,7}
set2 = {1,4,7}
print(f"Set1: {set1} and Set2: {set2}")
print(f"Is Set 2 a sub set of Set1: {set2.issubset(set1)}")