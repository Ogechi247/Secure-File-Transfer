import json
import getpass
import bcrypt
from user_registration import register_user

USERS_FILE = 'users.json'

def load_users():
    """Load user data from the JSON file."""
    try:
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    """Save user data to the JSON file."""
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def main():
    print("No users are registered with this client.")
    users = load_users()

    if not users:
        register = input("Do you want to register a new user (y/n)? ").lower()

        if register == 'y':
            full_name = input("Enter Full Name: ")
            email = input("Enter Email Address: ")
            password = getpass.getpass("Enter Password: ")
            re_password = getpass.getpass("Re-enter Password: ")

            if password != re_password:
                print("Passwords do not match. Please try again.")
                return

            if email in users:
                print("User already registered.")
                return

            # Hash the password before saving
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            users[email] = {
                'full_name': full_name,
                'password': hashed_password  # Store the hashed password
            }

            save_users(users)
            print("User Registered.")
            print("Exiting SecureDrop.")
        else:
            print("No user registered. Exiting.")
    else:
        print("Users already registered with the client.")

if __name__ == "__main__":
    main()
