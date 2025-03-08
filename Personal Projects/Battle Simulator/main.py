#Alex Anderson, Battle Simulator

import csv
import random

# Function to create a new character
def create_character(name, character_class):
    valid_classes = {"Warrior", "Mage", "Rogue"}
    while character_class not in valid_classes:
        character_class = input("Invalid class. Choose (Warrior, Mage, Rogue): ").capitalize()

    base_stats = {
        "Warrior": {"health": 120, "strength": 20, "defense": 15, "speed": 10},
        "Mage": {"health": 80, "strength": 10, "defense": 8, "speed": 12},
        "Rogue": {"health": 90, "strength": 15, "defense": 10, "speed": 18}
    }
    stats = base_stats[character_class]

    # Creating a character dictionary
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "experience": 0,
        "health": stats["health"],
        "strength": stats["strength"],
        "defense": stats["defense"],
        "speed": stats["speed"],
        "inventory": {"Health Potion": 1},
        "armor": {"helmet": None, "chestplate": None, "pants": None, "shoes": None},
        "status_effects": []
    }

    return character


# Function to save characters to a CSV file
def save_characters(characters, filename="characters.csv"):
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
                character["inventory"],
                character["armor"],
                character["status_effects"]
            ])


# Function to load characters from a CSV file
def load_characters(filename="characters.csv"):
    characters = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
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
                    "inventory": eval(row[8]),
                    "armor": eval(row[9]),
                    "status_effects": eval(row[10])
                }
                characters.append(character)
    except FileNotFoundError:
        pass  # If the file doesn't exist, return an empty list
    return characters


# Function to display a character's details
def display_character(character):
    armor = ', '.join([f"{key}: {val}" for key, val in character["armor"].items() if val]) or "None"
    print(f"Name: {character['name']}, Class: {character['class']}, Level: {character['level']}, Health: {character['health']}, Strength: {character['strength']}, Defense: {character['defense']}, Speed: {character['speed']}, Inventory: {character['inventory']}, Armor: {armor}, Status Effects: {character['status_effects']}")


# Function to battle two teams of characters
def battle(team_one, team_two):
    print("\nBattle Start: Team 1 vs Team 2")
    turn_order = sorted(team_one + team_two, key=lambda character: character["speed"], reverse=True)
    while True:
        for character in turn_order:
            if character["health"] <= 0:
                continue
            apply_status_effects(character)
            if character["health"] <= 0:
                continue
            enemies = team_two if character in team_one else team_one
            alive_enemies = [enemy for enemy in enemies if enemy["health"] > 0]
            if not alive_enemies:
                print("Team 1 wins!" if character in team_one else "Team 2 wins!")
                return
            target = random.choice(alive_enemies)
            damage = max(1, character["strength"] * random.uniform(0.8, 1.2) - target["defense"] * 0.5)
            target["health"] -= damage
            print(f"{character['name']} attacks {target['name']} for {damage:.1f} damage!")
            if target["health"] <= 0:
                print(f"{target['name']} has been defeated!")
                character["experience"] += 10
                if character["experience"] >= character["level"] * 20:
                    character["level"] += 1
                    character["strength"] += 2
                    character["defense"] += 2
                    character["speed"] += 1
                    character["health"] += 10
                    character["experience"] = 0
                    print(f"{character['name']} leveled up to {character['level']}!")
                reward_item = random.choice(["Helmet", "Chestplate", "Pants", "Shoes", "Health Potion"])
                print(f"{character['name']} found a {reward_item}!")
                if reward_item == "Health Potion":
                    character["inventory"][reward_item] = character["inventory"].get(reward_item, 0) + 1
                else:
                    equip_armor(character, reward_item.lower(), reward_item)


# Function to equip armor to a character
def equip_armor(character, armor_piece, armor_name):
    if armor_piece not in character["armor"]:
        print("Invalid armor slot.")
        return
    if character["armor"][armor_piece]:
        print(f"{character['name']} removed {character['armor'][armor_piece]} before equipping {armor_name}.")
    character["armor"][armor_piece] = armor_name
    print(f"{character['name']} equipped {armor_name} ({armor_piece})!")


# Function to apply status effects to a character
def apply_status_effects(character):
    for effect in character["status_effects"]:
        if effect == "poison":
            damage = random.randint(2, 5)
            character["health"] -= damage
            print(f"{character['name']} takes {damage} poison damage!")
        elif effect == "stun":
            print(f"{character['name']} is stunned and skips their turn!")
        elif effect == "frozen":
            print(f"{character['name']} is frozen and skips their turn!")
    character["status_effects"] = [effect for effect in character["status_effects"] if effect != "poison" and effect != "stun" and effect != "frozen"]


# Function to create the main menu and interact with the user
def main():
    characters = load_characters()

    while True:
        print("\n=== Character Management Game ===")
        action = input("What would you like to do? (create, view, battle, save, exit): ").strip().lower()

        if action == "create":
            name = input("Enter character name: ")
            class_choice = input("Choose a class (Warrior, Mage, Rogue): ").capitalize()
            character = create_character(name, class_choice)
            characters.append(character)
            print(f"{name} the {class_choice} has been created!")

        elif action == "view":
            if characters:
                for character in characters:
                    display_character(character)
            else:
                print("No characters available.")

        elif action == "battle":
            if len(characters) < 4:
                print("Not enough characters for a 2v2 battle. Please create more characters.")
            else:
                battle(characters[:2], characters[2:4])

        elif action == "save":
            save_characters(characters)
            print("Characters saved successfully!")

        elif action == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid input, please try again.")


# Running the main function
if __name__ == "__main__":
    main()
