import hashlib
class User:
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

class Events:
    def __init__(self, name, description, date):
        self.name = name
        self.description = description
        self.date = date
        self.tickets = []
        
    def show_event_details(self):
        print(f'Event: {self.name}')
        print(f'Description: {self.description}')
        print(f'Date: {self.date}') 
        print(f'Number of tickets: {len(self.tickets)}')
        
class Ticket:
    def __init__(self, ticket_id):
        self.ticket_id = ticket_id
        self.status = 'available'

    def mark_sold(self):
        self.status = 'sold'

class System:
    def __init__(self):
        pass

    def add_user(self, email, login: str, password: str) -> bool:
        with open('users.txt', 'r') as f:
            users = f.read().splitlines()

        for user in users:
            args = user.split(':')
            if login == args[0]:
                return False
        
        with open('users.txt', 'a') as f:
            f.write(f'{login}:{password}:{email}\n')
        return True
    
    def get_user(self, login: str, hash_password: str) -> bool:
        with open('users.txt', 'r') as f:
            users = f.read().splitlines()

        for user in users:
            args = user.split(':')
            if login == args[0] and hash_password == args[1]:
                return True
        return False  

    def get_admin(self, login: str, hash_password: str) -> bool:
        with open('users.txt', 'r') as f:
            users = f.read().splitlines()

        for user in users:
            args = user.split(':')
            if login == args[0] == hash_password == args[1]:
                return True
        return False
    
    def hash_password(self, text):
        return hashlib.sha256(text.encode()).hexdigest()
    
    def register_user(self):
        email = input('Enter your email: ')
        is_valid = self.is_valid_email(email)
    
        if not is_valid:
            print("Please enter a valid email address.")
            return  

        login = input('Choose a username: ')
        password = input('Choose a password: ')
        
        hash_password = self.hash_password(password)

        if login != password:
            if self.add_user(email, login, hash_password):
                print('Registration successful.')
            else:
                print('User already exists. Please try logging in.')
        else:
            print('Login must not be the same as password')

    def login_user(self):
        login = input('Enter your username: ')
        password = input('Enter your password: ')

        hash_password = self.hash_password(password)
        role = self.get_user(login, hash_password)
        is_admin = self.get_admin(login, hash_password) 

        if role == is_admin:
            print(f'Welcome back, {login}!' 
                '\nYou have admin access.')
        elif role != is_admin:
            print(f'Welcome back, {login}!'
                '\nYou have user access.')
        else:
            print('Invalid credentials. Please try again.')
    
    def is_valid_email(self, email):
        with open('users.txt', 'r') as f:
            users = f.read().splitlines()

        for user in users:
            if "@" not in email or "." not in email:
                print("Email must contain '@' and '.'")
                return False
            else:
                return True

system = System()
choice = input('Do you want to (r)egister or (l)ogin? ')

if choice.lower() == 'r':
    system.register_user()
elif choice.lower() == 'l':
    system.login_user()
else:
    print('Invalid choice.')
