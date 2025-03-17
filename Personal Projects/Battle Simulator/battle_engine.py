#Alex Anderson, Battle Simulator, function to run battles

import random

# Function for a battle
def battle(team_one, team_two):
    print("\nBattle Start:")
    turn_order = sorted(team_one + team_two, key=lambda character: character["speed"], reverse=True)
    
    # Resets special ability usage and status effects for all characters at the start of battle
    for character in turn_order:
        character["special_used"] = False
        character["status_effects"] = []

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

            # Applys status effects at the start of each turn
            if "stunned" in character["status_effects"]:
                print(f"{character['name']} is stunned and skips their turn!")
                character["status_effects"].remove("stunned")
                continue

            if "burned" in character["status_effects"]:
                burn_damage = 5
                character["health"] -= burn_damage
                print(f"{character['name']} takes {burn_damage} burn damage!")
                if character["health"] <= 0:
                    print(f"{character['name']} has been defeated!")
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
                if character["special_used"]:
                    print(f"{character['name']} has already used their special ability this battle!")

                else:
                    character["special_used"] = True  # Marks the special ability as used
                    target_team = team_two if character in team_one else team_one
                    alive_enemies = [enemy for enemy in target_team if enemy["health"] > 0]
                    if alive_enemies:
                        print("Choose an enemy to use your special ability on:")
                        for i, enemy in enumerate(alive_enemies):
                            print(f"{i + 1}. {enemy['name']} (Health: {enemy['health']})")

                        enemy_choice = int(input("Enter the number of the enemy you want to target: ")) - 1
                        target = alive_enemies[enemy_choice]

                        if character["special_ability"] == "Berserk":
                            character["strength"] += 5
                            print(f"{character['name']} uses Berserk! Strength increased!")

                        elif character["special_ability"] == "Fireball":
                            damage = random.randint(15, 25)
                            target["health"] -= damage
                            target["status_effects"].append("burned")
                            print(f"{character['name']} uses Fireball on {target['name']}! {damage} damage dealt! {target['name']} is burned!")

                        elif character["special_ability"] == "Shadow Strike":
                            damage = random.randint(10, 20)
                            target["health"] -= damage
                            if random.random() < 0.5:  # Has a 50 percent chance to stun
                                target["status_effects"].append("stunned")
                                print(f"{character['name']} uses Shadow Strike on {target['name']}! {damage} damage dealt! {target['name']} is stunned!")

                            else:
                                print(f"{character['name']} uses Shadow Strike on {target['name']}! {damage} damage dealt!")

                    else:
                        print("No enemies left to target!")

            else:
                print("Invalid action. Please choose again.")

            if character["health"] <= 0:
                print(f"{character['name']} has been defeated!")