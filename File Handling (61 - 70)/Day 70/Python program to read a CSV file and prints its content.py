'''
    This is a simple python program to read a CSV file and print its content
'''

import csv

def read_a_csv(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            data = list(reader)
        print(f"Data read from {filename}")
        for row in data:
            print(row)
    except FileNotFoundError:
        print("File is not found!")

filename = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\Test.csv"
read_a_csv(filename)