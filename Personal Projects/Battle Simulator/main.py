import csv
import random
import os
import json

CHARACTER_FILE = "characters.csv"

def main():
    characters = load_characters()

    def create_character(name, character_class):
        classes = {
            "Warrior": {"health": 120, "strength": 20, "defense": 15, "speed": 10},
            "Mage": {"health": 80, "strength": 10, "defense": 8, "speed": 12},
            "Rogue": {"health": 90, "strength": 15, "defense": 10, "speed": 18}
        }

        if character_class not in classes:
            return None

        stats = classes[character_class]
        return {
            "name": name, "class": character_class, "level": 1, "experience": 0,
            "health": stats["health"], "strength": stats["strength"], "defense": stats["defense"], "speed": stats["speed"],
            "inventory": {"Health Potion": 3}, "armor": {"helmet": None, "chestplate": None, "pants": None, "shoes": None}, "status_effects": [],
            "special_ability": determine_special_ability(character_class)
        }

    def determine_special_ability(character_class):
        abilities = {
            "Warrior": "Berserk: Increases strength temporarily.",
            "Mage": "Fireball: Deals massive damage with a chance to burn.",
            "Rogue": "Shadow Strike: Deals extra damage and has a chance to stun."
        }
        return abilities.get(character_class, "None")

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

    def battle(team_one, team_two):
        print("\nBattle Start: Team 1 vs Team 2")
        turn_order = sorted(team_one + team_two, key=lambda character: character["speed"], reverse=True)

        while True:
            # Check for if the battle is over (i.e., all characters on a team are defeated)
            if all(character["health"] <= 0 for character in team_one):
                print("Team 2 wins!")
                return
            if all(character["health"] <= 0 for character in team_two):
                print("Team 1 wins!")
                return

            for character in turn_order:
                if character["health"] <= 0:
                    continue

                # Handle status effects
                apply_status_effects(character)

                if character["health"] <= 0:
                    continue

                # Player's turn actions
                print(f"\n{character['name']}'s turn!")
                action = input(f"What would you like to do? (attack, use potion, special ability): ").strip().lower()

                if action == "attack":
                    alive_enemies = [enemy for enemy in (team_two if character in team_one else team_one) if enemy["health"] > 0]
                    if alive_enemies:
                        print("Choose an enemy to attack:")
                        for i, enemy in enumerate(alive_enemies):
                            print(f"{i + 1}. {enemy['name']} (Health: {enemy['health']})")
                        enemy_choice = int(input("Enter the number of the enemy you want to attack: ")) - 1
                        target = alive_enemies[enemy_choice]
                        damage = max(1, character["strength"] - target["defense"])

                        # Apply armor damage reduction
                        for armor_piece in target["armor"].values():
                            if armor_piece:  # If there's armor
                                damage = max(damage - 3, 1)  # Example armor effect: reduce damage by 3

                        target["health"] -= damage
                        target["health"] = max(target["health"], 0)  # Prevent negative health
                        print(f"{character['name']} attacks {target['name']} for {damage} damage!")
                        if target["health"] <= 0:
                            print(f"{target['name']} has been defeated!")

                elif action == "use potion":
                    if "Health Potion" in character["inventory"] and character["inventory"]["Health Potion"] > 0:
                        print(f"{character['name']} uses a Health Potion!")
                        character["health"] += 20  # Heal by 20 HP (you can adjust this value)
                        character["inventory"]["Health Potion"] -= 1
                        print(f"{character['name']} now has {character['health']} health!")
                    else:
                        print(f"{character['name']} has no Health Potions left!")

                elif action == "special ability":
                    if character["special_ability"] == "Berserk: Increases strength temporarily.":
                        print(f"{character['name']} uses Berserk!")
                        character["strength"] += 5  # Increase strength temporarily
                        print(f"{character['name']}'s strength is now {character['strength']}!")
                    elif character["special_ability"] == "Fireball: Deals massive damage with a chance to burn.":
                        print(f"{character['name']} uses Fireball!")
                        damage = random.randint(15, 25)
                        target = random.choice([enemy for enemy in (team_two if character in team_one else team_one) if enemy["health"] > 0])
                        target["health"] -= damage
                        target["health"] = max(target["health"], 0)
                        print(f"{character['name']} casts Fireball and deals {damage} damage to {target['name']}!")
                        if target["health"] <= 0:
                            print(f"{target['name']} has been defeated!")
                    elif character["special_ability"] == "Shadow Strike: Deals extra damage and has a chance to stun.":
                        print(f"{character['name']} uses Shadow Strike!")
                        damage = random.randint(10, 20)
                        target = random.choice([enemy for enemy in (team_two if character in team_one else team_one) if enemy["health"] > 0])
                        target["health"] -= damage
                        target["health"] = max(target["health"], 0)
                        print(f"{character['name']} strikes and deals {damage} damage to {target['name']}!")
                        if random.random() < 0.3:  # 30% chance to stun
                            target["status_effects"].append("stun")
                            print(f"{target['name']} has been stunned!")

                else:
                    print("Invalid action. Please choose again.")

                # After each action, check if the character gained experience
                if character["health"] > 0:
                    gain_experience(character, 10)  # Gain experience per battle
                    if character["experience"] >= 100:
                        level_up(character)

    def apply_status_effects(character):
        for effect in character["status_effects"]:
            if effect == "poison":
                damage = random.randint(2, 5)
                character["health"] -= damage
                character["health"] = max(character["health"], 0)  # Prevent negative health
                print(f"{character['name']} takes {damage} poison damage!")
            elif effect == "burn":
                damage = random.randint(3, 6)
                character["health"] -= damage
                character["health"] = max(character["health"], 0)
                print(f"{character['name']} takes {damage} burn damage!")
            elif effect == "stun":
                print(f"{character['name']} is stunned and cannot act this turn!")

        character["status_effects"] = [effect for effect in character["status_effects"] if effect not in ["poison", "burn", "stun"]]

    def gain_experience(character, amount):
        character["experience"] += amount
        print(f"{character['name']} gains {amount} experience!")

    def level_up(character):
        character["level"] += 1
        character["health"] += 10  # Increase health upon level up
        character["strength"] += 2  # Increase strength upon level up
        character["defense"] += 2  # Increase defense upon level up
        print(f"{character['name']} has leveled up to level {character['level']}!")

    while True:
        action = input("\nWhat would you like to do? (create, view, battle, save, exit): ").strip().lower()

        if action == "create":
            name = input("Enter character name: ")
            # Check for duplicate names
            if any(char["name"].lower() == name.lower() for char in characters):
                print("A character with that name already exists.")
                continue

            char_class = input("Choose a class (Warrior, Mage, Rogue): ").capitalize()
            while char_class not in ["Warrior", "Mage", "Rogue"]:
                print("Invalid class. Please choose Warrior, Mage, or Rogue.")
                char_class = input("Choose a class (Warrior, Mage, Rogue): ").capitalize()

            character = create_character(name, char_class)
            if character:
                characters.append(character)
                print(f"{name} the {char_class} has been created!")
            else:
                print("Failed to create character.")

        elif action == "view":
            for char in characters:
                print(char)

        elif action == "battle":
            if len(characters) < 4:
                print("Not enough characters for a 2v2 battle. Please create more characters.")
            else:
                battle(characters[:2], characters[2:4])

        elif action == "save":
            save_characters(characters)
            print("Characters saved successfully!")

        elif action == "exit":
            break

        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
