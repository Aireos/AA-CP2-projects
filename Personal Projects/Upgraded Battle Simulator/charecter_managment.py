#Alex Anderson, Battle Simulator, functions that deal with the charecter directly

import os
import csv
import ast
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
CHARACTER_FILE = "Personal Projects/Upgraded Battle Simulator/charecters.csv"

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
            character_class = {"name": "Warrior", "health": 4, "strength": 3, "defense": 3, "speed": 2}
            
        elif character_class == "Mage":
            character_class = {"name": "Mage", "health": 1, "strength": 7, "defense": 1, "speed": 3}
        
        elif character_class == "Rogue":
            character_class = {"name": "Rogue", "health": 2, "strength": 4, "defense": 2, "speed": 4}

        character = {
            "name": name,
            "class": character_class,
            "stats": character_class,
            "level": 1,
            "experience": 0,
            "inventory": {"Health Potion": 3},
            "armor": {"helmet": None, "chestplate": None, "pants": None, "shoes": None},
            "status_effects": [],
            "special_ability": ability_determiner(character_class["name"])
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
            try:
                for row in reader:
                    character = {
                        "name": row[0],
                        "class": ast.literal_eval(row[1]),
                        "stats": ast.literal_eval(row[2]),
                        "level": int(row[3]),
                        "experience": int(row[4]),
                        "inventory": ast.literal_eval(row[5]),
                        "armor": row[6],
                        "status_effects": row[7],
                        "special_ability": row[8]
                    }
                    characters.append(character)
            except:
                return []
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
        character["stats"]["health"] = int(character["class"]["health"] * character["level"])
        character["stats"]["strength"] = int(character["class"]["strength"] * character["level"])
        character["stats"]["defense"] = int(character["class"]["defense"] * character["level"])
        character["stats"]["speed"] = int(character["class"]["speed"] * character["level"])
    return characters

def character_statistics(characters):
    df = pd.DataFrame(characters)

    if "stats" in df.columns:
        stats_df = pd.json_normalize(df["stats"])  # Flatten nested stats dictionary

        print("Character Statistics:")
        print(stats_df.describe())  # Show statistical summary

        # Find and print the character with the highest strength
        max_strength_idx = stats_df["strength"].idxmax()
        print(f"\nHighest Strength Character: {df.loc[max_strength_idx, 'name']} - Strength: {stats_df.loc[max_strength_idx, 'strength']}")

        # Find and print the character with the highest health
        max_health_idx = stats_df["health"].idxmax()
        print(f"\nHighest Health Character: {df.loc[max_health_idx, 'name']} - Health: {stats_df.loc[max_health_idx, 'health']}")

        # Find and print the fastest character
        max_speed_idx = stats_df["speed"].idxmax()
        print(f"\nFastest Character: {df.loc[max_speed_idx, 'name']} - Speed: {stats_df.loc[max_speed_idx, 'speed']}")

# Function to display all characters
def display_character(characters):
    if not characters:
        print("No characters found!")
        return

    which_character = input("Which charecters info do you want to view?(type all to see generalized statistics): ").strip().capitalize()

    if which_character == "All":
        character_statistics(characters)
    
    else:
        for character in characters:
            if which_character == character['name']:

                print("Name:", character['name'], "| Health:", int(character['stats']['health']), "| Strength:", int(character['stats']['strength']), "| Defense:", int(character['stats']['defense']), "| Speed:", int(character['stats']['speed']))

                plt.style.use('_mpl-gallery-nogrid')

                # Define data
                labels = ["Health", "Strength", "Defense", "Speed"]
                x = [int(character['stats']["health"]),
                    int(character['stats']["strength"]),
                    int(character['stats']["defense"]),
                    int(character['stats']["speed"])]

                colors = plt.get_cmap('coolwarm')(np.linspace(0.2, 0.7, len(x)))

                # Create the plot
                fig, ax = plt.subplots()
                wedges, texts = ax.pie(x, colors=colors, radius=3, center=(4, 4),
                                        wedgeprops={"linewidth": 1, "edgecolor": "white"}, 
                                        frame=True)

                # Add legend (key)
                ax.legend(wedges, labels, title=character['name'], loc="upper right", bbox_to_anchor=(1, 1))

                # Set limits
                ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                    ylim=(0, 8), yticks=np.arange(1, 8))

                # Show the plot
                plt.show()
