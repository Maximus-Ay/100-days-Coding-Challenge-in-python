'''
    - Write a Python program to create a simple to-do list using a class and file handling.
'''

import os

class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return [line.strip() for line in file.readlines()]
        else:
            return []
    
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(task + "\n")

    def add_task(self):
        task = input("Enter task: ")
        self.tasks.append(task)
        self.save_tasks()
        print("Task Added!")

    def remove_tasks(self):
        task_number = int(input("Enter task number to remove: ")) - 1
        if task_number < len(self.tasks):
            del self.tasks[task_number]
            self.save_tasks()
            print("Task removed!")
        else:
            print("Invalid task number!")
    
    def view_tasks(self):
        if self.tasks:
            print("\nTo-Do-List")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}.{task}")
        else:
            print("No task")
    
def main():
    filename = "C:\\Users\\Max The Developer\\Documents\\GitHub\\100-days-Coding-Challenge-with-python\\Others (Day 81 - 100)\\Day 83\\todo.txt"
    todo = ToDoList(filename)

    while True:
        print("\nShopping Cart Menu: ")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo.add_task()
        elif choice == "2":
            todo.view_tasks()
            todo.remove_tasks()
        elif choice == "3":
            todo.view_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

