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

    # def buy_ticket(self, event):
    #     if self.tickets:  
    #         ticket = self.tickets.pop()  
    #         ticket.mark_sold()  
    #         self.tickets.append(ticket)  
    #         print(f'{self.name} bought ticket ID: {ticket.ticket_id} for the event: {event.name}')
    #     else:
    #         print(f'Sorry, there are no available tickets for the event: {event.name}')

class Events:
    def __init__(self):
        pass
    
        # with open ('films.txt', 'w') as f:
        #     for title, details in self.films.items():
        #         f.write(f"{title}:\n")
        #         for key, value in details.items():
        #             f.write(f"{key}: {value}\n")
        #         f.write("\n")
    
        # with open('performances.txt', 'w') as f:
        #     for title, details in self.performances.items():
        #         f.write(f"{title}:\n")
        #         for key, value in details.items():
        #             f.write(f"{key}: {value}\n")
        #         f.write("\n")
    
    def event_selection(self):
        choice_events = input('What are you interested in? (f)ilms or (p)erformance: ')

        if choice_events.lower() == 'f':
            with open('films.txt', 'r') as f:
                films = f.read().strip().split("\n\n") 
                titles = [film.split(':')[0] for film in films]
                print("Available films:")
                for title in titles:
                    print(f"- {title.strip()}")

            selected_film = input('Please enter the film title: ').strip().lower()
            found = False

            with open('films.txt', 'r', encoding='utf-8') as f:
                films = f.read().strip().split("\n\n")

                for film in films:
                    title = film.split(':')[0].strip().lower()
                    if title == selected_film:
                        print(film) 
                        found = True
                        break

            if not found:
                print("Film not found.")
        
        elif choice_events.lower() == 'p':
            with open('performances.txt', 'r') as f:
                events = f.read().strip().split("\n\n") 
                titles = [event.split(':')[0] for event in events]
                print("Available performances:")
                for title in titles:
                    print(f"- {title.strip()}")

            selected_performance = input('Please enter the performance title: ').strip().lower()
            found = False

            with open('performances.txt', 'r') as f:
                performances = f.read().strip().split("\n\n")

                for performance in performances:
                    title = performance.split(':')[0].strip().lower()
                    if title == selected_performance:
                        print(performance) 
                        found = True
                        break

            if not found:
                print("Performance not found.")

        else:
            print('Invalid choice.')
        
class Ticket:
    def __init__(self, ticket_id):
        self.ticket_id = ticket_id
        self.status = 'available'

    def mark_sold(self):
        self.status = 'sold'

class System:
    def __init__(self):
        pass

    def add_user(self, email, login: str, password: str, access: str) -> bool:

        with open('users.txt', 'r') as f:
            users = f.read().splitlines()


        for user in users:
            args = user.split(':')
            if login == args[0]:
                print('This login is currently used.')
                return False
            elif email == args[2]:
                print('This email is already registered.')
                return False

        with open('users.txt', 'a') as f:
            f.write(f'{login}:{password}:{email}:{access}\n')
        return True

    def get_user(self, login: str, hash_password: str):

        with open('users.txt', 'r') as f:
            users = f.read().splitlines()

        for user in users:
            args = user.split(':')
            if login == args[0] and hash_password == args[1]:
                return args[3]
        return None
    
    def hash_password(self, text):
        return hashlib.sha256(text.encode()).hexdigest()
    
    def register_admin(self):
        email = input('Enter your email: ')
        is_valid = self.is_valid_email(email)
    
        if not is_valid:
            print("Please enter a valid email address.")
            return  

        login = input('Choose a username: ')
        password = input('Choose a password: ')
        
        hash_password = self.hash_password(password)

        if self.add_user(email, login, hash_password, 'admin'):
            print('Admin registration successful.')
        else:
            print('User already exists. Please try logging in.')
    
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
            if self.add_user(email, login, hash_password, 'user'):
                print('User registration successful.')
            else:
                print('User already exists. Please try logging in.')
        else:
            print('Login must not be the same as password')

    def login_user(self):
        login = input('Enter your username: ')
        password = input('Enter your password: ')

        hash_password = self.hash_password(password)
        access_level = self.get_user(login, hash_password)
        
        if access_level is not None:
            print(f'Welcome back, {login}! Your access level is: {access_level}')
            return True
        else:
            print('Invalid credentials. Please try again.')
            return False
    
    def is_valid_email(self, email):
        if "@" not in email or "." not in email:
            print("Email must contain '@' and '.'")
            return False
        return True

system = System()
event = Events()
choice = input('Do you want to (r)egister or (l)ogin? ')

if choice.lower() == 'r':
    system.register_user()
elif choice.lower() == 'l':
    if system.login_user() == True:
        event.event_selection()
elif choice == '1234':
    system.register_admin()
else:
    print('Invalid choice.')
