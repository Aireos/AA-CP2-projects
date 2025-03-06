def equip_items(user_key, users):
    print(f"You have a {users[user_key]["equipment"]["head"]} on your head, {users[user_key]["equipment"]["body"]} on your body, {users[user_key]["equipment"]["legs"]} on your legs, and {users[user_key]["equipment"]["feet"]} on your feet.")

    shoes_found = False
    print("\nPossible equipment for feet:")
    for item in users[user_key]["items"]:
        if "shoes" in item:
            print(item)
            shoes_found = True
        
        if shoes_found == False:
            print("You have no shoes")

    pants_found = False
    print("\nPossible equipment for legs:")
    for item in users[user_key]["items"]:
        if "pants" in item:
            print(item)
            
        
        if pants_found == False:
            print("You have no shoes")

    print("\nPossible equipment for body:")
    for item in users[user_key]["items"]:
        if "chestplate" in item:
            print(item)
    
    print("\nPossible equipment for head:")
    for item in users[user_key]["items"]:
        if "helmet" in item:
            print(item)