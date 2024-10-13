'''
    - Write a program to create a class that represents a simple chat system 
      with methods to send, receive, and display messages.
'''
class ChatSystem:
    def __init__(self):
        self.messages = []
        self.users = {}

    def register_user(self, username):
        if username not in self.users:
            self.users[username] = []
            print(f"User '{username}' registered successfully.")
        else:
            print(f"User '{username}' already exists.")

    def send_message(self, username, message):
        if username in self.users:
            self.messages.append((username, message))
            print(f"Message sent by '{username}' successfully.")
        else:
            print(f"User '{username}' not found.")

    def receive_messages(self, username):
        if username in self.users:
            user_messages = [(user, msg) for user, msg in self.messages if user != username]
            return user_messages
        else:
            print(f"User '{username}' not found.")
            return []

    def display_messages(self, username):
        if username in self.users:
            print(f"\nMessages for '{username}':")
            for user, message in self.receive_messages(username):
                print(f"{user}: {message}")
        else:
            print(f"User '{username}' not found.")

