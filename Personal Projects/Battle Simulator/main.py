#Alex Anderson, Battle Simulator

import csv

# Function to load user profiles
def load_user_profiles():
    users = {}
    try:
        with open("Personal Projects/Battle Simulator/charecters.csv", "r", newline="") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                try:
                    if row:
                        username, password = row[0], row[1]
                        items = row[2].split() if row[2] else []
                        health = int(row[3]) if row[3].isdigit() else 100
                        strength = int(row[4]) if row[4].isdigit() else 10
                        defense = int(row[5]) if row[5].isdigit() else 10
                        speed = int(row[6]) if row[6].isdigit() else 10
                        user_class = row[7] if len(row) > 7 else "Warrior"
                        abilities = row[8].split(';') if len(row) > 8 else ["Power Strike"]
                        equipment = {
                            "head": row[9] if len(row) > 9 else "None",
                            "body": row[10] if len(row) > 10 else "None",
                            "legs": row[11] if len(row) > 11 else "None",
                            "feet": row[12] if len(row) > 12 else "None"
                        }
                        users[username] = {
                            "password": password,
                            "items": items,
                            "health": health,
                            "strength": strength,
                            "defense": defense,
                            "speed": speed,
                            "class": user_class,
                            "abilities": abilities,
                            "equipment": equipment
                        }
                except:
                    continue
    except:
        pass
    return users

# Function to save user profiles
def save_user_profiles(users):
    try:
        with open("Personal Projects/Battle Simulator/charecters.csv", "w", newline="") as file:
            csv_writer = csv.writer(file)
            for username, data in users.items():
                try:
                    csv_writer.writerow([
                        username,
                        data["password"],
                        " ".join(data["items"]),
                        data["health"],
                        data["strength"],
                        data["defense"],
                        data["speed"],
                        data["class"],
                        ";".join(data["abilities"]),
                        data["equipment"]["head"],
                        data["equipment"]["body"],
                        data["equipment"]["legs"],
                        data["equipment"]["feet"]
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
            
            if username.lower() == "leave":
                return False

            if username not in users:
                print("That username does not exist")
                continue

            password = input("Enter your password: ").strip()
            if password == users[username]["password"]:
                print("Login successful")
                return username
            else:
                print("Incorrect password")
        except:
            print("An error occurred, please try again")

# Function to create a new account
def new_account(users):
    while True:
        try:
            username = input("Enter your desired username: ").strip()
            if username in users:
                print("That username is already taken")
                continue

            password = input("Enter your password: ").strip()
            
            while True:
                user_class = input("Choose a class (Warrior, Mage, Rogue, Berserker): ").strip().capitalize()
                if user_class in ["Warrior", "Mage", "Rogue", "Berserker"]:
                    break
                else:
                    print("Invalid class, please choose from Warrior, Mage, Rogue, or Berserker")
            
            # Apply class-based stat modifications and abilities
            class_stats = {
                "Warrior": {"health": 120, "strength": 15, "defense": 15, "speed": 8, "abilities": ["Power Strike", "Shield Block"]},
                "Mage": {"health": 80, "strength": 20, "defense": 5, "speed": 12, "abilities": ["Fireball", "Magic Shield"]},
                "Rogue": {"health": 90, "strength": 12, "defense": 10, "speed": 18, "abilities": ["Backstab", "Shadow Step"]},
                "Berserker": {"health": 110, "strength": 18, "defense": 8, "speed": 10, "abilities": ["Rage", "Berserk Smash"]}
            }

            users[username] = {
                "password": password,
                "items": [],
                "health": class_stats[user_class]["health"],
                "strength": class_stats[user_class]["strength"],
                "defense": class_stats[user_class]["defense"],
                "speed": class_stats[user_class]["speed"],
                "class": user_class,
                "abilities": class_stats[user_class]["abilities"],
                "equipment": {"head": "None", "body": "None", "legs": "None", "feet": "None"}
            }
            print("Account created successfully!")
            return username
        except:
            print("An error occurred, please try again")

# Main function to handle user login or making a new acount
def user_login():
    while True:
        try:
            users = load_user_profiles()
            print("Welcome to the Battle Simulator!")

            while True:
                choice = input("Do you want to make a new account (1), access an account (2)?: ").strip()
                if choice == "1":
                    user_key = new_account(users)
                    break
                elif choice == "2":
                    user_key = access_account(users)
                    if user_key is False:
                        user_key = new_account(users)
                    break
                else:
                    print("Invalid choice, please enter 1 or 2")
                    continue
            
            save_user_profiles(users)
            print(f"Welcome {user_key}")
            return user_key, users
        except:
            print("An error occurred during login")
            continue

def equip_items(user_key, users):
    print()
    
user_key, users = user_login()
