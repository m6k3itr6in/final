class user:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.__password = password
        self.tickets = []

    def register(self):
        print(f'User {self.name} is registered')

    def user_tickets(self):
        if not self.tickets:
            print('You have no purchased tickets')
        else:
            print(f'User {self.name} tickets:')
            for ticket in self.tickets:
                print(f'Ticket ID: {ticket.ticket_id}, Status: {ticket.status}')

class events:
    def __init__(self, name, description, date):
        self.name = name
        self.description = description
        self.date = date
        
    def show_event_details(self):
        print(f'Event: {self.name}')
        print(f'Description: {self.description}')
        print(f'Date: {self.date}') 
        print(f'Number of tickets: {len(self.tickets)}')
        
class ticket:
    def __init__(self, ticket_id):
        self.ticket_id = ticket_id
        self.status = 'available'

    def mark_sold(self):
        self.status = 'sold'

class system:
    def __init__(self):
        self.users = []
        self.events = []