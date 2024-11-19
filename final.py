import hashlib
import os
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

    def add_user(self, email, login:str, password:str) -> bool:
        with open('users.txt', 'r') as f:
            users = f.read().splitlines()

        for user in users:
            args = user.split(':')
            if login ==args[0]:
                return False
            
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        with open('users.txt', 'a') as f:
            f.write(f'{login}:{password}:{email}\n')
        return True
    
    def get_user(self, login: str, password: str) -> bool:
        with open('users.txt', 'r') as f:
            users = f.read().splitlines()  # Считываем всех пользователей из файла

        for user in users:
            args = user.split(':')
            if login == args[0]:
                if hashlib.sha256(password.encode()).hexdigest():  # Если пользователь с таким логином и паролем существует
                    return True
        return False
    
    def register_user(self):
        email = input('Enter your email: ')
        login = input('Choose a username: ')
        password = input('Choose a password: ')

        if self.add_user(email, login, password):
            print('Registration successful.')
        else:
            print('User already exists. Please try logging in.')

    def login_user(self):
        login = input('Enter your username: ')
        password = input('Enter your password: ')

        if self.get_user(login, password):
            print(f'Welcome back, {login}!')
            # Здесь можно добавить доступ к мероприятиям и билетам
        else:
            print('Invalid credentials. Please try again.')

# Пример использования
system = System()
choice = input('Do you want to (r)egister or (l)ogin? ')

if choice.lower() == 'r':
    system.register_user()
elif choice.lower() == 'l':
    system.login_user()
else:
    print('Invalid choice.')