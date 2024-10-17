'''
    - Write a program to create a class that models a basic email system 
      with methods to send, receive, and display emails.
'''

class Email:
    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def __str__(self):
        return f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\n\n{self.body}"

class EmailSystem:
    def __init__(self):
        self.emails = {}
        self.users = set()

    def register_user(self, username):
        if username not in self.users:
            self.users.add(username)
            self.emails[username] = []
            print(f"User '{username}' registered successfully.")
        else:
            print(f"User '{username}' already exists.")

    def send_email(self, sender, recipient, subject, body):
        if sender in self.users and recipient in self.users:
            email = Email(sender, recipient, subject, body)
            self.emails[recipient].append(email)
            print(f"Email sent from '{sender}' to '{recipient}' successfully.")
        else:
            print("Sender or recipient not found.")

    def receive_emails(self, username):
        if username in self.users:
            return self.emails[username]
        else:
            print(f"User '{username}' not found.")
            return []

    def display_emails(self, username):
        if username in self.users:
            print(f"\nEmails for '{username}':")
            for i, email in enumerate(self.emails[username], start=1):
                print(f"\nEmail {i}:")
                print(email)
        else:
            print(f"User '{username}' not found.")

# Example usage
email_system = EmailSystem()

while True:
    print("\nEmail System")
    print("1. Register user")
    print("2. Send email")
    print("3. Receive emails")
    print("4. Display emails")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        email_system.register_user(username)
    elif choice == "2":
        sender = input("Enter sender's username: ")
        recipient = input("Enter recipient's username: ")
        subject = input("Enter email subject: ")
        body = input("Enter email body: ")
        email_system.send_email(sender, recipient, subject, body)
    elif choice == "3":
        username = input("Enter username: ")
        emails = email_system.receive_emails(username)
        for email in emails:
            print(email)
    elif choice == "4":
        username = input("Enter username: ")
        email_system.display_emails(username)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
