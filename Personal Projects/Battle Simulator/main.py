#Alex Anderson, Battle Simulator

import csv

# Function to load user profiles from CSV
def load_user_profiles():
    users = {}
    try:
        with open("users.csv", "r", newline="") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                try:
                    if row:
                        username, password = row[0], row[1]
                        leaderboards = row[2:] if row[2:] else ["", "", ""]
                        users[username] = {
                            "password": password,
                            "items": leaderboards[0].split() if leaderboards[0] else [],
                            "leaderboard_two": leaderboards[1].split() if leaderboards[1] else [],
                            "leaderboard_three": leaderboards[2].split() if leaderboards[2] else []
                        }
                except:
                    continue
    except:
        pass
    return users

# Function to turn user leaderboard into a list
def leaderboard_fixer(users):
    try:
        for username, data in users.items():
            data["leaderboard_one"] = " ".join(data["leaderboard_one"]) if data["leaderboard_one"] else ""
            data["leaderboard_two"] = " ".join(data["leaderboard_two"]) if data["leaderboard_two"] else ""
            data["leaderboard_three"] = " ".join(data["leaderboard_three"]) if data["leaderboard_three"] else ""
    except:
        pass

# Function to save user profiles to CSV
def save_user_profiles(users):
    try:
        with open("users.csv", "w", newline="") as file:
            csv_writer = csv.writer(file)
            for username, data in users.items():
                try:
                    csv_writer.writerow([
                        username,
                        data["password"],
                        data["leaderboard_one"],
                        data["leaderboard_two"],
                        data["leaderboard_three"]
                    ])
                except:
                    continue
    except:
        pass

# Function to access an account
def access_account(users):
    while True:
        try:
            username = input("What is your username?(Type leave to make a new account): ").strip()
            if username == "SillyBilly":
                print('Error: SillyBilly too powerful')
                continue
            
            if username.lower() == "leave":
                return False

            if username not in users:
                print("That username does not exist.")
                continue

            password = input("Enter your password: ").strip()
            if password == users[username]["password"]:
                print("Login successful!")
                return username
            else:
                print("Incorrect password. Try again.")
        except:
            print("An error occurred. Please try again.")

# Function to create a new account
def new_account(users):
    while True:
        try:
            username = input("Enter your desired username: ").strip()
            if username in users:
                print("That username is already taken. Try again.")
                continue

            password = input("Enter your password: ").strip()
            users[username] = {
                "password": password,
                "leaderboard_one": "",
                "leaderboard_two": "",
                "leaderboard_three": ""
            }
            print("Account created successfully!")
            return username
        except:
            print("An error occurred. Please try again.")

# Main function to handle user login or account creation
def user_login():
    while True:
        try:
            users = load_user_profiles()
            leaderboard_fixer(users)
            print("\033cWelcome to Game Central!")

            while True:
                choice = input("Do you want to make a new account (1), access an account (2), or exit program (3)?: ").strip()
                if choice == "1":
                    user_key = new_account(users)
                    break
                elif choice == "2":
                    user_key = access_account(users)
                    if user_key is False:
                        user_key = new_account(users)
                    break
                elif choice == "3":
                    print("Thank you for using our program!")
                    return None
                else:
                    print("Invalid choice. Please enter 1, 2 or 3.")
                    continue
            
            save_user_profiles(users)
            print(f"Welcome, {user_key}!")
            return user_key
        except:
            print("An error occurred during login.")
            continue