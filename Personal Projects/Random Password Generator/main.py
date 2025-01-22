#Alex Anderson, Random Password Generator

import random
special_charecters = ["@", "#", "$", "%", "&", "!"]
uppercase_charecters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase_charecters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","8","9"]
password = ""


def uppercase_finder_amount(type, password):
    if type == 0:
        while True:
            try: 
                uppercase = int(input("How many uppercase letters do you want?: "))
                break
            except: 
                print("invalid input")
                continue
        return uppercase
    
    elif type == 1:
        uppercase -= 1
        password += uppercase_charecters[random.randint(0,25)]
        return password, uppercase

def lowercase_finder_amount(type, password):
    if type == 0:
        while True:
            try: 
                lowercase = int(input("How many lowercase letters do you want?: "))
                break
            except: 
                print("invalid input")
                continue
        return lowercase
    
    elif type == 1:
        lowercase -= 1
        password += lowercase_charecters[random.randint(0,25)]
        return password, lowercase

def number_finder_amount(type, password):
    if type == 0:
        while True:
            try: 
                number_amount = int(input("How many numbers do you want?: "))
                break
            except: 
                print("invalid input")
                continue
        return number_amount
    
    elif type == 1:
        number_amount -= 1
        password += numbers[random.randint(0,8)]
        return password, number_amount
    
def special_finder_amount(type, password):
    if type == 0:
        while True:
            try: 
                special = int(input("How many numbers do you want?: "))
                break
            except: 
                print("invalid input")
                continue
        return special
    
    elif type == 1:
        special -= 1
        password += special_charecters[random.randint(0,8)]
        return password, special


while True:

    try: length = int(input("What is the total length of the password?: "))
    except: 
        print("invalid input")
        continue

    uppercase = uppercase_finder_amount(0,password)
    lowercase = lowercase_finder_amount(0,password)
    special = special_finder_amount(0,password)
    number_amount = number_finder_amount(0, password)

    if uppercase + lowercase + special + number_amount == length:
        break
    else:
        print("You can't have more charecters than total length!")
        continue

while True:
    next_charecter = random.randint(0,3)
    if uppercase != 0 and next_charecter == 0:
        password, uppercase = uppercase_finder_amount(1,password)
    
