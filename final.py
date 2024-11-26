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
        self.films = {
    "Leon": {
        "Genre": "action, thriller",
        "Year of production": "1994",
        "Description": "An orphan girl becomes the partner of an assassin. A cult thriller starring Jean Reno and Natalie Portman."
    },

    "The disgusting eight": {
        "Genre": "western, crime, thriller, drama, detective",
        "Year of production": "2015",
        "Description": '''USA after the Civil War. 
        Legendary bounty hunter John Root (The Executioner) accompanies the prisoner. 
        On the way, they are joined by other travelers. A snowstorm forces them to seek refuge in a remote store, 
        where an eccentric company has already gathered: a Confederate general, a Mexican, a cowboy... 
        One of them is not who he claims to be'''
    },

    "Seven": {
        "Genre": "thriller, detective, crime, drama",
        "Year of production": "1995",
        "Description":'''Detective William Somerset is a veteran criminal investigator who dreams of retiring and leaving the city. 
        Seven days before retiring, he will face two troubles: a young partner, Mills, and a particularly brutal murder. 
        An experienced investigator understands that this crime is likely to be followed by others.'''
    },

     "Shutter Island": {
        "Genre": "thriller, detective, drama",
        "Year of production": "2005",
        "Description":'''Two American bailiffs are sent to one of the islands in Massachusetts 
        to investigate the disappearance of a patient at a clinic for insane criminals. 
        During the investigation, they will have to face a web of lies, a hurricane and a deadly riot of the clinic's inhabitants.'''
    },
            }
        self.performances = {
    "Tolstoy and Co": {
        "Author's work": "A.G. Dolbilova",
        "Description": '''The first part of the trilogy about the classics of Russian literature L.N.Tolstoy, N.V.Gogol and A.P.Chekhov, 
        which presents the life and work of famous authors in an unusual perspective, 
        where the viewer will discover new personal traits of writers, little-known, 
        but fascinating and important moments of their biography.'''
    },

    "Once upon a time in the kingdom": {
        "Author's work": "I.S. Sukhanova",
        "Description": '''For the third time, boys and girls with Vasya Gromov 
        will go on a fun trip together with Bremen Town musicians and other heroes of well-known fairy tales. 
        We will meet the real king! And where there is a king, of course there is a princess.
        And where the princess is, there will definitely be love!..'''
    },

    "Once upon a time in the kingdom": {
        "Author's work": "I.S. Sukhanova",
        "Description": '''For the third time, boys and girls with Vasya Gromov 
        will go on a fun trip together with Bremen Town musicians and other heroes of well-known fairy tales. 
        We will meet the real king! And where there is a king, of course there is a princess.
        And where the princess is, there will definitely be love!..'''
    },

    

    "Moping in Russian": {
        "Author's work": "I.S. Sukhanova",
        "Description": '''A simple, at first glance, story about the everyday course of life of a provincial nobleman 
        trying to dispel himself in the rural wilderness, chasing peasants. 
        A lot of unexpected things are revealed in the house of the main character Lasukov in one evening.
        And the reason for this is the "illness" of the master.
        ++And the diagnosis of the disease is not difficult to determine – Russian melancholy.'''
    },
        } 
    
    def event_selection(self):
        choice_events = input('What are you interested in? (f)ilms or (p)erformance: ')

        if choice_events.lower() == 'f':
            print("Available films:")
            for title in self.films.keys():
                print(f"- {title}")

            selected_film = input('Please enter the film title from above: ')
            films_lowercase = {film.lower(): info for film, info in self.films.items()}
            if selected_film.lower() in films_lowercase:
                info = films_lowercase[selected_film]
                print(f"\nTitle: {selected_film.capitalize()}")
                print(f"Genre: {info['Genre']}")
                print(f"Year of production: {info['Year of production']}")
                print(f"Description: {info['Description']}\n")
            else:
                print("Invalid film title.")
        
        elif choice_events.lower() == 'p':
            print("Available performances:")  
            for title in self.performances.keys():
                print(f"- {title}")

            selected_performance = input('Please enter the performance title from above: ')
            performances_lowercase = {performance.lower(): info for performance, info in self.performances.items()}
            if selected_performance.lower() in performances_lowercase:
                info = performances_lowercase[selected_performance]
                print(f"\nTitle: {selected_performance.capitalize()}")
                print(f"Author's work: {info["Author's work"]}")
                print(f"Description: {info['Description']}\n")
            else:
                print("Invalid performance title.")

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
        else:
            print('Invalid credentials. Please try again.')
    
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
    event.event_selection()
elif choice.lower() == 'l':
    system.login_user()
    event.event_selection()
elif choice == '1234':
    system.register_admin()
else:
    print('Invalid choice.')
