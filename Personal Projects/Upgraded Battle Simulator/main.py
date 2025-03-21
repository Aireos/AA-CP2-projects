#Alex Anderson, Battle Simulator

from charecter_managment import *
from battle import *

# Main user interface
def main():

    characters = load_characters()

    while True:
        action = input("\nWould you like to add, view, battle, or exit?: ").strip().lower()

        if action == "add":
            name = input("Enter character name: ")
            character_class = input("Choose a class (Warrior, Mage, Rogue): ").capitalize()
            character = charecter_creation(name, character_class)
            if character:
                characters.append(character)
                save_characters(characters)
                print(f"{name} created successfully!")
                
            else:
                print("Invalid class. Please try again.")

        elif action == "view":
            display_character(characters)

        elif action == "battle":
            if len(characters) < 4:
                print("Not enough characters for a 2v2 battle. Please create more characters.")

            else:
                placement = 0
                for item in characters:
                    print(f"{placement}. {item['name']}")
                    placement += 1
                
                team_one = input("What is the placements for the two characters on team one? (example: 1,2): ").split(',')
                team_two = input("What is the placements for the two characters on team two? (example: 2,4): ").split(',')

                duplicate_found = False

                for item in team_one:
                    found = False

                    for i in team_two:
                        if item == i:
                            print("You can not use charecters multiple times. Please try again.")
                            duplicate_found = True
                            continue
                
                    for i in team_one:
                        if item == i:
                            if found == True:
                                print("You can not use charecters multiple times. Please try again.")
                                duplicate_found = True
                            found = True
                
                for item in team_two:
                    found = False

                    for i in team_two:
                        if item == i:
                            if found == True:
                                print("You can not use charecters multiple times. Please try again.")
                                duplicate_found = True
                                continue
                            found = True

                if duplicate_found == True:
                    continue

                try:
                    wining_team = battle([characters[int(team_one[0])],characters[int(team_one[1])]],[characters[int(team_two[0])],characters[int(team_two[1])]])
                    for character in wining_team:
                        character = xp_giver(character)
                        characters = stat_updater(characters)
                        save_characters(characters)
                except:
                    print("Those placements do not work. Please try again.")

        elif action == "exit":
            print("Exiting game. Goodbye!")
            break

        else:
            print("Invalid input. Please try again.")


main()