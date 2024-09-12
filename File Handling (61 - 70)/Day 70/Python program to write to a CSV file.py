'''
    This is a simple python program that writes to a CSV file
'''
import csv

def write_to_csv(filename, data):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Data written to {filename}.")
    except Exception as e:
        print("Error writing to CSV : {e}")

data = [
    ["Name", "Age", "City"],
    ["John", 13, "Yaounde"],
    ["Alice", 30, "New York"],
    ["Pogba", 31, "Paris"],
    ["Dos Santos", 19, "Rio De Janeiro"]
]
filename = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\File Handling (61 - 70)\\Test.csv"
write_to_csv(filename, data)