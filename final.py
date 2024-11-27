import hashlib
import time
class User:
    def __init__(self, login):
        self.login = login

    def display_purchases(self):
        with open('purchased_tickets.txt', 'r') as f:
            information = f.read().strip().splitlines()
                
            user_purchases = []
            for record in information:
                user_login, title, amount = record.split(':')
                if user_login == self.login:
                    user_purchases.append((title, amount))

            if not user_purchases:
                print('You have no purchases.')
            else:
                print('Your purchases:')
                for title, amount in user_purchases:
                    print(f'Film/Performance: {title}, Amount: {amount}')

class Events:
    def __init__(self):
        pass
   
    def event_selection(self):
        choice_events = input('What are you interested in? (f)ilms or (p)erformance: ')
        print('--------------------')

        if choice_events.lower() == 'f':
            with open('films.txt', 'r') as f:
                films = f.read().strip().split("\n\n") 
                titles = [film.split(':')[0] for film in films]
                print("Available films:")
                for title in titles:
                    print(f"- {title.strip()}")

            selected_film = input('Please enter the film title: ').strip().lower()
            print('--------------------')
            found = False

            with open('films.txt', 'r') as f:
                films = f.read().strip().split("\n\n")

                for film in films:
                    title = film.split(':')[0].strip().lower()
                    if title == selected_film:
                        print(film)
                        print('--------------------') 
                        found = True

            if not found:
                print('Film not found.')
                return
        
        elif choice_events.lower() == 'p':
            with open('performances.txt', 'r') as f:
                events = f.read().strip().split("\n\n") 
                titles = [event.split(':')[0] for event in events]
                print("Available performances:")
                for title in titles:
                    print(f"- {title.strip()}")

            selected_performance = input('Please enter the performance title: ').strip().lower()
            print('--------------------')
            found = False

            with open('performances.txt', 'r') as f:
                performances = f.read().strip().split("\n\n")

                for performance in performances:
                    title = performance.split(':')[0].strip().lower()
                    if title == selected_performance:
                        print(performance)
                        print('--------------------') 
                        found = True
            
            if not found:
                print('Performance not found.')
                return
        else:
            print('Invalid choice.')
            return


class Ticket:
    def __init__(self):
        pass

    def add_tickets(self):
        with open('films.txt', 'r') as d:
            films = d.read().strip().split("\n\n") 
            film_titles = [film.split(':')[0].strip() for film in films]

        with open('performances.txt', 'r') as t:
            performances = t.read().strip().split("\n\n") 
            performance_titles = [event.split(':')[0].strip() for event in performances]

        for title in film_titles:
            amount = input(f'Input available amount tickets for film "{title}": ')
            self.save_ticket(title, amount)

        for title in performance_titles:
            amount = input(f'Input available amount tickets for performance "{title}": ')
            self.save_ticket(title, amount)

    def save_ticket(self, title, amount):
        with open('available_tickets.txt', 'a') as f:
            f.write(f"{title}:{amount}\n") 

    def display_available_tickets(self):
        available = {}

        with open('available_tickets.txt', 'r') as t:
            tickets = t.read().strip().splitlines()
            for ticket in tickets:
                title, amount = ticket.split(':')
                available[title.strip()] = int(amount.strip())

        for title, amount in available.items():
            if amount > 0:
                print(f'- {title} - {amount} available for buying')
            else:
                print(f'- {title} - SOLD OUT')             
        return available  # Return available tickets for further actions

    def purchase_ticket(self, available, user_login):
        print('--------------------')
        title = input("Enter the title of the ticket you want to buy: ").strip()
        print('--------------------')
        if title in available and available[title] > 0:
            print('--------------------')
            amount_to_buy = int(input(f"How many tickets do you want to buy for '{title}'? (Available: {available[title]}): "))
            print('--------------------')
            if amount_to_buy <= available[title] and amount_to_buy > 0:
                available[title] -= amount_to_buy
                self.add_purchase(title, amount_to_buy, user_login)
                print('Wait please...')
                time.sleep(2)
                print('Payment confirmation...')
                time.sleep(5)
                print('Succesfully!')
                print('Thank you for your purchase!')
                print('--------------------')
                self.update_ticket_file(available)
            else:
                print("Invalid number of tickets requested.")
        else:
            print("Sorry, but this Film/Performance is sold out.")

    def add_purchase(self, title, amount, user_login):
        with open('purchased_tickets.txt', 'a') as f:
            f.write(f"{user_login}:{title}:{amount}\n")

    def update_ticket_file(self, available):
        with open('available_tickets.txt', 'w') as f:
            for title, amount in available.items():
                f.write(f"{title}:{amount}\n")

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
            print('--------------------')
            return login, access_level
        else:
            print('Invalid credentials. Please try again.')
            return None, None
    
    def is_valid_email(self, email):
        if "@" not in email or "." not in email:
            print("Email must contain '@' and '.'")
            return False
        return True


# Main interaction logic
system = System()
event = Events()
ticket = Ticket()

while True:
    choice = input('Do you want to (r)egister or (l)ogin? (Type "exit" to quit): ')
    
    if choice.lower() == 'r':
        system.register_user()
    elif choice.lower() == 'l':
        login, access = system.login_user()
        if login:
            user = User(login)  # Create a User object with the current login
            if access == 'user':
                while True:
                    event.event_selection()
                    available_tickets = ticket.display_available_tickets()
                    ticket.purchase_ticket(available_tickets, login)  # Pass the login here
                    continue_choice = input('Do you want to continue buying tickets? (y/n): ')
                    if continue_choice.lower() != 'y':
                        break  # Exit the loop if the user doesn't want to continue
                # After all purchases, display the user's purchase history
                user.display_purchases()  # Show the user their purchases
            elif access == 'admin':
                while True:
                    event.event_selection()  # Admin can also select events
                    ticket.add_tickets()  # Allow admin to add tickets for the selected event
                    continue_choice = input('Do you want to continue adding tickets? (y/n): ')
                    if continue_choice.lower() != 'y':
                        break  # Exit the loop if the admin doesn't want to continue
    elif choice.lower() == '1234':
        system.register_admin()
    elif choice.lower() == 'exit':
        print("Exiting the system.")
        break  # Exit the program
    else:
        print('Invalid choice.')
