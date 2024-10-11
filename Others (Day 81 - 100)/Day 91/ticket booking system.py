'''
    - Write a program to create a class that simulates a basic ticket booking system 
      with methods to add, remove, and book tickets.
'''
class Ticket:
    def __init__(self, ticket_id, event_name, price, availability=True):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"Ticket {self.ticket_id} ({self.event_name}, ${self.price}) - Available: {self.availability}"

class TicketBookingSystem:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket_id, event_name, price):
        ticket = Ticket(ticket_id, event_name, price)
        self.tickets.append(ticket)
        print(f"Ticket added: {ticket}")

    def remove_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                self.tickets.remove(ticket)
                print(f"Ticket {ticket_id} removed")
                return
        print(f"Ticket {ticket_id} not found")

    def book_ticket(self, ticket_id, customer_name):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                if ticket.availability:
                    ticket.availability = False
                    print(f"Ticket {ticket_id} booked by {customer_name}")
                    print(f"Total cost: ${ticket.price}")
                else:
                    print(f"Ticket {ticket_id} is already booked")
                return
        print(f"Ticket {ticket_id} not found")

    def cancel_booking(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                if not ticket.availability:
                    ticket.availability = True
                    print(f"Ticket {ticket_id} booking cancelled")
                else:
                    print(f"Ticket {ticket_id} is already available")
                return
        print(f"Ticket {ticket_id} not found")

    def display_tickets(self):
        print("\nAvailable Tickets:")
        for ticket in self.tickets:
            if ticket.availability:
                print(ticket)
        print("\nBooked Tickets:")
        for ticket in self.tickets:
            if not ticket.availability:
                print(ticket)

# Example usage
ticket_system = TicketBookingSystem()

while True:
    print("\nTicket Booking System")
    print("1. Add ticket")
    print("2. Remove ticket")
    print("3. Book ticket")
    print("4. Cancel booking")
    print("5. Display tickets")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        ticket_id = input("Enter ticket ID: ")
        event_name = input("Enter event name: ")
        price = float(input("Enter ticket price: "))
        ticket_system.add_ticket(ticket_id, event_name, price)
    elif choice == "2":
        ticket_id = input("Enter ticket ID: ")
        ticket_system.remove_ticket(ticket_id)
    elif choice == "3":
        ticket_id = input("Enter ticket ID: ")
        customer_name = input("Enter customer name: ")
        ticket_system.book_ticket(ticket_id, customer_name)
    elif choice == "4":
        ticket_id = input("Enter ticket ID: ")
        ticket_system.cancel_booking(ticket_id)
    elif choice == "5":
        ticket_system.display_tickets()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
