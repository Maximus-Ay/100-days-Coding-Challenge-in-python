'''
    This is a simple python address book program using Classes and dictionaries and other concepts in python
'''

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {
            "phone_number": phone_number,
            "email": email,
            "address": address
        }
        print(f"Contact {name} added successfully!")
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} doesn't exist!")
        
    def update_contact(self, name, phone_number = None, email=None, address=None):
        if name in self.contacts:
            if phone_number:
                self.contacts[name]["phone_number"] = phone_number
            if email:
                self.contacts[name]["email"] = email
            if address:
                self.contacts[name]["address"] = address
            print(f"Contact {name} successfully updated!")
        else:
            print(f"Contact {name} not found!")
    
    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact {name} found!")
            print(f"Phone Number: {self.contacts[name]['phone_number']}")
            print(f"Email: {self.contacts[name]['email']}")
            print(f"Address: {self.contacts[name]['address']}")
        else:
            print(f"Contact {name} not found!")

    def display_contacts(self):
        if self.contacts:
            print("Contains:")
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone Number: {details['phone_number']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}")
        else:
            print("No contacts found!")

def main():
    address_book = AddressBook()

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. Display Contacts")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter address: ")
            address_book.add_contact(name, phone_number, email, address)

        elif choice == "2":
            name = input("Enter the name: ")
            address_book.delete_contact(name)
        elif choice == "3":
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter address: ")
            address_book.update_contact(name, phone_number or None, email or None, address or None)
        elif choice == "4":
            name = input("Enter name: ")
            address_book.search_contact(name)
        elif choice == "5":
            address_book.display_contacts()
        elif choice == "6":
            break
        else:
            print("invalid choice. Please Try again!")

if __name__ == "__main__":
    main()
 