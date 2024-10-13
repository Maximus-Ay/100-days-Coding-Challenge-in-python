'''
    - Write a Python program to create a class that simulates a simple library management system with methods to issue, return, and display books.
'''

class Book:
    def __init__(self, title, author, publication_date, status="Available"):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author}, Published: {self.publication_date}, Status: {self.status}"
    
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, publication_date):
        self.books[title] = Book(title, author, publication_date)
        print(f"Added {title} to library")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Removed {title} from library")
    
    def lend_book(self, title, borrower):
        if title in self.books and self.books[title].status == "Available":
            self.books[title].status = f"Lent to {borrower}"
            print(f"Lent {title} to {borrower}")
        elif title in self.books and self.books[title].status != "Available":
            print(f"{title} is currently lent to {self.books[title].status.split(' ')[-1]}.")
        else:
            print(f"{title} not found in library!")

    def return_book(self, title):
        if title in self.books and self.books[title].status != "Available":
            self.books[title].status = "Available"
            print(f"Returned {title} to library")
        elif title in self.books and self.books[title].status == "Available":
            print(f"{title} is already available in library.")
        else:
            print(f"{title} not found in library!")

    def display_catalog(self):
        print("\nLibrary Catalog.")
        for book in self.books.values():
            print(book)

def main():
    
    library = Library()

    while True:
      print("\nLibrary Management System")
      print("1. Add Book")
      print("2. Remove Book")
      print("3. Lend Book")
      print("4. Return Book")
      print("5. Display Catalog")
      print("6. Exit")
      
      choice = input("Enter your choice: ")

      if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        publication_date = input("Enter book publication date: ")
        library.add_book(title, author,publication_date)
      elif choice == "2":
        title = input("Enter book title to remove: ")
        library.remove_book(title)
      elif choice == "3":
        title = input("Enter book title to lend: ")
        borrower = input("Enter borrowers name: ")
        library.lend_book(title, borrower)
      elif choice == "4":
        title = input("Enter book title to return: ")
        library.return_book(title)
      elif choice == "5":
        library.display_catalog()
      elif choice == "6":
        break
      else:
        print("Invalid choice. Please Try again")

if __name__ == "__main__":
    main()