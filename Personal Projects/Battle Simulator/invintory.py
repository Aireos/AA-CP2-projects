#Alex Anderson, Battle Simulator

def equip_items(user_key, users):
    print(f"You have a {users[user_key]["equipment"]["head"]} on your head, {users[user_key]["equipment"]["body"]} on your body, {users[user_key]["equipment"]["legs"]} on your legs, and {users[user_key]["equipment"]["feet"]} on your feet.")

    
    while True:
        user_choice = input("\nDo you want to update your equipment for your feet, legs, body, or head? (type leave to leave): ").strip().lower()


        if user_choice == "leave":
            return users


        elif user_choice == "feet":
            shoes_found = False
            possible_shoes = []

            print("\nPossible equipment for feet:")
            for item in users[user_key]["items"]:
                if "shoes" in item:
                    print(item)
                    possible_shoes.append(item)
                    shoes_found = True
            
            if shoes_found == False:
                print("You have no shoes")
                continue

            while True:
                equipment_choice = input("\nWhat shoes do you want to wear? (type leave to not change): ").strip().lower()
                equipment_found = False

                if equipment_choice == "leave":
                    break

                for item in possible_shoes:
                    if item == equipment_choice:
                        users[user_key]["equipment"]["feet"] = item
                        equipment_found = True
                        print(f"{item} has been equiped")
                
                if equipment_found == False:
                    print("You do not have those shoes")
                    continue

                break
        

        elif user_choice == "legs":
            pants_found = False
            possible_pants = []

            print("\nPossible equipment for pants:")
            for item in users[user_key]["items"]:
                if "pants" in item:
                    print(item)
                    possible_pants.append(item)
                    pants_found = True
            
            if pants_found == False:
                print("You have no pants")
                continue

            while True:
                equipment_choice = input("\nWhat pants do you want to wear? (type leave to not change): ").strip().lower()
                equipment_found = False

                if equipment_choice == "leave":
                    break

                for item in possible_pants:
                    if item == equipment_choice:
                        users[user_key]["equipment"]["legs"] = item
                        equipment_found = True
                        print(f"{item} has been equiped")
                
                if equipment_found == False:
                    print("You do not have those pants")
                    continue

                break
        

        elif user_choice == "body":
            chestplate_found = False
            possible_chestplate = []

            print("\nPossible equipment for chestplate:")
            for item in users[user_key]["items"]:
                if "chestplate" in item:
                    print(item)
                    possible_chestplate.append(item)
                    chestplate_found = True
            
            if chestplate_found == False:
                print("You have no chestplates")
                continue

            while True:
                equipment_choice = input("\nWhat chestplate do you want to wear? (type leave to not change): ").strip().lower()
                equipment_found = False

                if equipment_choice == "leave":
                    break

                for item in possible_chestplate:
                    if item == equipment_choice:
                        users[user_key]["equipment"]["body"] = item
                        equipment_found = True
                        print(f"{item} has been equiped")
                
                if equipment_found == False:
                    print("You do not have that chestplate")
                    continue

                break
        

        elif user_choice == "head":
            helmet_found = False
            possible_helmet = []

            print("\nPossible equipment for helmet:")
            for item in users[user_key]["items"]:
                if "helmet" in item:
                    print(item)
                    possible_helmet.append(item)
                    helmet_found = True
            
            if helmet_found == False:
                print("You have no helmets")
                continue

            while True:
                equipment_choice = input("\nWhat helmet do you want to wear? (type leave to not change): ").strip().lower()
                equipment_found = False

                if equipment_choice == "leave":
                    break

                for item in possible_helmet:
                    if item == equipment_choice:
                        users[user_key]["equipment"]["head"] = item
                        equipment_found = True
                        print(f"{item} has been equiped")
                
                if equipment_found == False:
                    print("You do not have that helmet")
                    continue

                break
            

        