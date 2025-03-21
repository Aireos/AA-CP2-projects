#Alex Anderson, Battle Simulator, functions that deal with the charecter directly

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
        classes = ["Warrior","Mage","Rogue"]
    
        if character_class not in classes:
            return None

        if character_class == "Warrior":
            character_class = {"health": 4, "strength": 3, "defense": 3, "speed": 2}
            
        elif character_class == "Mage":
            character_class = {"health": 1, "strength": 7, "defense": 1, "speed": 3}
        
        elif character_class == "Rogue":
            character_class = {"health": 2, "strength": 4, "defense": 2, "speed": 4}

        character = {
            "name": name,
            "class": character_class,
            "stats": character_class,
            "level": 1,
            "experience": 0,
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
        writer.writerow(["name", "class", "stats", "level", "experience", "inventory", "armor", "status_effects"])
        for character in characters:
            writer.writerow([
                character["name"],
                character["class"],
                character["stats"],
                character["level"],
                character["experience"],
                character["inventory"],
                character["armor"],
                character["status_effects"],
                character["special_ability"]
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
                    "stats": row[2],
                    "level": int(row[3]),
                    "experience": int(row[4]),
                    "inventory": row[5],
                    "armor": row[6],
                    "status_effects": row[7],
                    "special_ability": row[8]
                }
                characters.append(character)
    return characters

def xp_giver(character):
    xp_requirment = 0
    character['experience'] += 10
    for number in range(character['level']):
        xp_requirment += 10*number
    if character['experience'] >= xp_requirment:
        print(character['name'], "levaled up!")
        character['level'] += 1
        character['experience'] = 0
    return character

def stat_updater(characters):
    for character in characters:
        character["stats"]["health"] = character["class"]["health"] * character["level"]
        character["stats"]["strength"] = character["class"]["strength"] * character["level"]
        character["stats"]["defense"] = character["class"]["defense"] * character["level"]
        character["stats"]["speed"] = character["class"]["speed"] * character["level"]
    return characters

# Function to display all characters
def display_characters(characters):
    if not characters:
        print("No characters found!")
        return
    
    for char in characters:
        print(f"Name: {char['name']}, Class: {char['class']}, Health: {char['health']}, Strength: {char['strength']}, Defense: {char['defense']}, Speed: {char['speed']}")
        import matplotlib.pyplot as plt
        import numpy as np

        plt.style.use('_mpl-gallery-nogrid')

        # make data
        x = [char['health'],char['strength'],char['defense'],char['speed']]
        colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

        # plot
        fig, ax = plt.subplots()
        ax.pie(x, colors=colors, radius=3, center=(4, 4),
            wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

        ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
            ylim=(0, 8), yticks=np.arange(1, 8))

        plt.show()
        
