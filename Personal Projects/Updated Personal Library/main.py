#Alex Anderson Update Personal Library

import random
import json
import os

CHARACTER_FILE = "characters.csv"

# Function to create a character
def create_character(name, character_class):
    classes = {
        "Warrior": {"health": 120, "strength": 20, "defense": 15, "speed": 10},
        "Mage": {"health": 80, "strength": 10, "defense": 8, "speed": 12},
        "Rogue": {"health": 90, "strength": 15, "defense": 10, "speed": 18}
    }

    if character_class not in classes:
        return None

    stats = classes[character_class]
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "experience": 0,
        "health": stats["health"],
        "strength": stats["strength"],
        "defense": stats["defense"],
        "speed": stats["speed"],
        "inventory": {"Health Potion": 3},
        "armor": {"helmet": None, "chestplate": None, "pants": None, "shoes": None},
        "status_effects": [],
        "special_ability": determine_special_ability(character_class)
    }

    return character

# Function to determine the character's special ability
def determine_special_ability(character_class):
    abilities = {
        "Warrior": "Berserk: Increases strength temporarily.",
        "Mage": "Fireball: Deals massive damage with a chance to burn.",
        "Rogue": "Shadow Strike: Deals extra damage and has a chance to stun."
    }
    return abilities.get(character_class, "None")

# Function to save characters to a file
def save_characters(characters, filename=CHARACTER_FILE):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "class", "level", "experience", "health", "strength", "defense", "speed", "inventory", "armor", "status_effects"])
        for character in characters:
            writer.writerow([
                character["name"],
                character["class"],
                character["level"],
                character["experience"],
                character["health"],
                character["strength"],
                character["defense"],
                character["speed"],
                json.dumps(character["inventory"]),
                json.dumps(character["armor"]),
                json.dumps(character["status_effects"])
            ])

# Function to load characters from a file
def load_characters(filename=CHARACTER_FILE):
    characters = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                character = {
                    "name": row[0],
                    "class": row[1],
                    "level": int(row[2]),
                    "experience": int(row[3]),
                    "health": int(row[4]),
                    "strength": int(row[5]),
                    "defense": int(row[6]),
                    "speed": int(row[7]),
                    "inventory": json.loads(row[8]),
                    "armor": json.loads(row[9]),
                    "status_effects": json.loads(row[10])
                }
                characters.append(character)
    return characters

# Function to display all characters
def display_characters(characters):
    if not characters:
        print("No characters found!")
        return
    for char in characters:
        print(f"Name: {char['name']}, Class: {char['class']}, Health: {char['health']}, Strength: {char['strength']}, Defense: {char['defense']}, Speed: {char['speed']}")

# Function for a battle
def battle(team_one, team_two):
    print("\nBattle Start: Team 1 vs Team 2")
    turn_order = sorted(team_one + team_two, key=lambda character: character["speed"], reverse=True)

    while True:
        if all(character["health"] <= 0 for character in team_one):
            print("Team 2 wins!")
            return
        if all(character["health"] <= 0 for character in team_two):
            print("Team 1 wins!")
            return

        for character in turn_order:
            if character["health"] <= 0:
                continue

            print(f"\n{character['name']}'s turn!")
            action = input(f"What would you like to do? (attack, use potion, special ability): ").strip().lower()

            if action == "attack":
                target_team = team_two if character in team_one else team_one
                alive_enemies = [enemy for enemy in target_team if enemy["health"] > 0]
                if alive_enemies:
                    print("Choose an enemy to attack:")
                    for i, enemy in enumerate(alive_enemies):
                        print(f"{i + 1}. {enemy['name']} (Health: {enemy['health']})")
                    enemy_choice = int(input("Enter the number of the enemy you want to attack: ")) - 1
                    target = alive_enemies[enemy_choice]
                    damage = max(1, character["strength"] - target["defense"])
                    target["health"] -= damage
                    target["health"] = max(target["health"], 0)
                    print(f"{character['name']} attacks {target['name']} for {damage} damage!")
                    if target["health"] <= 0:
                        print(f"{target['name']} has been defeated!")
                else:
                    print("No enemies left to attack!")

            elif action == "use potion":
                if "Health Potion" in character["inventory"] and character["inventory"]["Health Potion"] > 0:
                    character["health"] += 20
                    character["inventory"]["Health Potion"] -= 1
                    print(f"{character['name']} uses a Health Potion and heals for 20 HP!")
                else:
                    print(f"{character['name']} has no Health Potions left!")

            elif action == "special ability":
                if character["special_ability"] == "Berserk: Increases strength temporarily.":
                    character["strength"] += 5
                    print(f"{character['name']} uses Berserk! Strength increased!")
                elif character["special_ability"] == "Fireball: Deals massive damage with a chance to burn.":
                    damage = random.randint(15, 25)
                    target = random.choice([enemy for enemy in (team_two if character in team_one else team_one) if enemy["health"] > 0])
                    target["health"] -= damage
                    print(f"{character['name']} uses Fireball! {damage} damage dealt!")
                elif character["special_ability"] == "Shadow Strike: Deals extra damage and has a chance to stun.":
                    damage = random.randint(10, 20)
                    target = random.choice([enemy for enemy in (team_two if character in team_one else team_one) if enemy["health"] > 0])
                    target["health"] -= damage
                    print(f"{character['name']} uses Shadow Strike! {damage} damage dealt!")
                else:
                    print("No special ability available!")

            else:
                print("Invalid action. Please choose again.")

            if character["health"] <= 0:
                print(f"{character['name']} has been defeated!")

# Main function
def main():
    characters = load_characters()

    while True:
        action = input("\nWould you like to add, view, battle, save, or exit?: ").strip().lower()

        if action == "add":
            name = input("Enter character name: ")
            char_class = input("Choose a class (Warrior, Mage, Rogue): ").capitalize()
            character = create_character(name, char_class)
            if character:
                characters.append(character)
                print(f"Character {name} created successfully!")
            else:
                print("Invalid class. Please try again.")

        elif action == "view":
            display_characters(characters)

        elif action == "battle":
            if len(characters) < 4:
                print("Not enough characters for a 2v2 battle. Please create more characters.")
            else:
                battle(characters[:2], characters[2:4])

        elif action == "save":
            save_characters(characters)
            print("Characters saved successfully!")

        elif action == "exit":
            print("Exiting game. Goodbye!")
            break

        else:
            print("Invalid input. Please try again.")

main()