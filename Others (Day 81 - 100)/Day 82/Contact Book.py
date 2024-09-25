'''
- Write a Python program to create a contact book using a class.
'''

class Contact:
    def __init__(self,name,phone_number,email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def display(self):
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email: {self.email}")

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        contact = Contact(name,phone_number,email)
        self.contacts.append(contact)
        print(f"Contact added Successfully!")

    def delete_contact(self):
        name = input("Enter name of contact to delete: ")
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return 
        print("Contact not found!")

    def search_contact(self):
        name = input("Enter name of contact to search: ")
        for contact in self.contacts:
            if contact.name == name:
                contact.display()
                return
        print("Contact not found!")
    
    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for i,contact in enumerate(self.contacts, 1):
                print(f"Contact {i}:")
                contact.display()
                print()
            else:
                print("No Contacts found.")

def main():
    contact_book = ContactBook()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.delete_contact()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.display_contacts()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again")
if __name__ == "__main__":
    main()
