import sys
# [cite: 201, 202, 203, 205]
from .managers import UsersManager, QuestionsManager
from .models import User
from .utils import show_menu, input_int
import getpass 

def main():
    # [cite: 207]
    users_mgr = UsersManager()
    questions_mgr = QuestionsManager()

    print("Welcome to AskMe App")

    while True:
        print("\n--- Main Menu ---")
        choice = show_menu(["Login", "Sign Up", "Exit"])

        if choice == 1: # Login
            username = input("Username: ")
            # [cite: 291] 
            try:
                password = getpass.getpass("Password: ")
            except:
                password = input("Password: ")
            
            user = users_mgr.get_user(username, password)
            if user:
                print(f"\nWelcome back, {user.name}!")
                user_home(user, questions_mgr, users_mgr)
            else:
                print("Error: Invalid username or password.")

        elif choice == 2: # Sign Up
            print("\n--- Create New Account ---")
            username = input("Username: ")
            if users_mgr.is_username_exist(username):
                print("Error: Username already exists.")
                continue
            
            password = input("Password: ")
            name = input("Name: ")
            email = input("Email: ")
            allow_anon = input_int("Allow anonymous questions? (0: No, 1: Yes): ", 0, 1)
            
            new_user = User(username=username, password=password, name=name, email=email, allow_anonymous=(allow_anon==1))
            users_mgr.save_user(new_user)
            print("Account created successfully. Please login.")

        elif choice == 3:
            print("Goodbye!")
            break

def user_home(user, q_mgr, u_mgr):
    while True:
        print(f"\n--- User Menu ({user.name}) ---")
        choices = [
            "Print Questions To Me",
            "Print Questions From Me",
            "Answer Question",
            "Delete Question",
            "Ask Question",
            "List Feed",
            "Logout"
        ]
        choice = show_menu(choices)

        if choice == 1:
            q_mgr.print_to_questions(user)
        elif choice == 2:
            q_mgr.print_from_questions(user)
        elif choice == 3:
            q_mgr.answer_question(user)
        elif choice == 4:
            q_mgr.delete_question(user)
        elif choice == 5:
            q_mgr.ask_question(user, u_mgr)
        elif choice == 6:
            q_mgr.list_feed()
        elif choice == 7:
            break

if __name__ == "__main__":
    main()