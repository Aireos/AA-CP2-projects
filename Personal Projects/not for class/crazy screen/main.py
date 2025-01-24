import random
special_charecters = ["@", "#", "$", "%", "&", "!"]
uppercase_charecters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase_charecters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9"]

while True:
    password = ""
    while True:
        next_charecter = random.randint(0,3)
        if next_charecter == 0:
            password += special_charecters[random.randint(0,5)]
        if next_charecter == 1:
            password += numbers[random.randint(0,8)]
        if next_charecter == 2:
            password += lowercase_charecters[random.randint(0,25)]
        if next_charecter == 3:
            password += uppercase_charecters[random.randint(0,25)]
        charecter_amount = 0
        for charecter in password:
            charecter_amount += 1
        if charecter_amount == 287:
            break
    print(password)