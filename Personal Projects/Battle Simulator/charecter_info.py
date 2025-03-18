#Alex Anderson, Battle Simulator, functions that deal with the charecter directly

import json
import os
import csv
CHARACTER_FILE = "Personal Projects/Battle Simulator/characters.csv"

# Function to determine the character's special ability
def ability_determiner(character_class):
    def determine_special_ability(character_class):
        abilities = {
            "Warrior": "Berserk", # Increases strength temporarily for one turn
            "Mage": "Fireball", # Deals massive damage with a chance to burn for one turn
            "Rogue": "Shadow Strike" # Deals extra damage and has a 50 percent chance to stun for one turn
        }
        return abilities.get(character_class, "None")
    return determine_special_ability(character_class)


def charecter_creation(name, character_class):

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
            "special_ability": ability_determiner(character_class)
        }
    
        return character
    
    return create_character(name, character_class)


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