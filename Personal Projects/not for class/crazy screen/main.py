import random
characters = ["*","-","_","+","=","`","~","@", "#", "$", "%", "&", "!", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9"]

number = -1
for character in characters:
    number += 1

while True:
    password = ""

    while True:
        password += characters[random.randint(0,number)]
        charecter_amount = 0
        for charecter in password:
            charecter_amount += 1
        if charecter_amount == 287:
            break

    print(password)