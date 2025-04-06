#Alex Anderson, Battle Simulator, functions that deal with the charecter directly

import os
import csv
import ast
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from faker import Faker
fake = Faker()
CHARACTER_FILE = "Personal Projects/Personal Portfolio/charecters.csv"

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

#Function to make character backstorys
def backstory_maker():
    part_one = fake.job()
    part_two = fake.company()
    background = f"They were a {part_one} working for {part_two} before becoming a adventurer."
    return background

#Fucntion to make character characteristics
def characteristics_maker():

    # generater of random characteristics
    hair_color = fake.color_name()  # Random hair color
    eye_color = fake.random_element(['Blue', 'Green', 'Brown', 'Hazel', 'Gray'])
    height = fake.random_int(min=150, max=200)  # Random height in cm
    weight = fake.random_int(min=40, max=100)  # Random weight in kg

    characteristics = {
        "Hair": hair_color,
        "Eye": eye_color,
        "Height": height,
        "Weight": weight
    }

    return characteristics


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
            "special_ability": ability_determiner(character_class["name"]),
            "backstory": backstory_maker(),
            "characteristics": characteristics_maker()
        }
    
        return character
    
    return create_character(name, character_class)


# Function to save characters to a file
def save_characters(characters, filename=CHARACTER_FILE):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "class", "stats", "level", "experience", "inventory", "armor", "status_effects", "backstory", "characteristics"])
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
                character["special_ability"],
                character["backstory"],
                character["characteristics"]
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
                        "special_ability": row[8],
                        "backstory": row[9],
                        "characteristics": row[10]
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
        stats_df = pd.json_normalize(df["stats"])  # Flattens nested stats dictionary

        print("Character Statistics:")
        print(stats_df.describe())  # Shows statistical summary for all characters

        # Finds and prints the character's name with the highest strength and their strength stat
        max_strength_idx = stats_df["strength"].idxmax()
        print(f"\nHighest Strength Character: {df.loc[max_strength_idx, 'name']} - Strength: {stats_df.loc[max_strength_idx, 'strength']}")

        # Finds and prints the character name with the highest health and their health stat
        max_health_idx = stats_df["health"].idxmax()
        print(f"\nHighest Health Character: {df.loc[max_health_idx, 'name']} - Health: {stats_df.loc[max_health_idx, 'health']}")

        # Finds and prints the character's name that has the highest defense and their defense stat
        max_speed_idx = stats_df["defense"].idxmax()
        print(f"\nToughest Character: {df.loc[max_speed_idx, 'name']} - Defense: {stats_df.loc[max_speed_idx, 'defense']}")

        # Finds and prints the fastest character's name and their speed stat
        max_speed_idx = stats_df["speed"].idxmax()
        print(f"\nFastest Character: {df.loc[max_speed_idx, 'name']} - Speed: {stats_df.loc[max_speed_idx, 'speed']}")

# Function to display all characters
def display_character(characters):
    if not characters:
        print("No characters found!")
        return

    which_character = input("Which charecters info do you want to view?(type all to see generalized statistics)(type leveling to see leveling chart): ").strip()

    if which_character == "all":
        character_statistics(characters)
    
    if which_character == "leveling":
        try:
            level_amount = int(input("What level do you want the chart to go to?: "))
        except:
            print("that was not a number, will default to 10")
            level_amount = 10
        leveling_chart(level_amount)

    else:
        character_found = False
        for character in characters:
            if which_character == character['name']:
                character_found = True

                print("Name:", character['name'], "| Health:", int(character['stats']['health']), "| Strength:", int(character['stats']['strength']), "| Defense:", int(character['stats']['defense']), "| Speed:", int(character['stats']['speed']))
                print("Backstory:", character['backstory'])

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
                ax.set(xlim=(0, 20), xticks=np.arange(0, 0),
                    ylim=(0, 20), yticks=np.arange(0, 0))

                # Show the plot
                plt.show()

        if character_found == False:
            print("That is not a characters name.")
            
def leveling_chart(level_amount):
    plt.style.use('_mpl-gallery')
    
    # make data:
    x = np.arange(level_amount)

    xp_requirments = []
    for number in range(level_amount):
        xp_requirments.append(10*number)

    y = xp_requirments
    
    # plot
    fig, ax = plt.subplots()
    
    ax.bar(x, y, width=0.5, edgecolor="white", linewidth=0.1)
    
    ax.set(xlim=(0, level_amount), xticks=np.arange(1, level_amount),
           ylim=(0, level_amount*10), yticks=np.arange(1, level_amount*10))
    
    plt.show()
