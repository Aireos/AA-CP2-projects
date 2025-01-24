#Alex Anderson, Random Password Generator

#importing random to make randomized passwords and making lists for all the different types of charecters or numbers
import random
special_charecters = ["@", "#", "$", "%", "&", "!"]
uppercase_charecters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase_charecters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9"]


#used for finding the number of uppercase letters and adding uppercase letters to the password
def uppercase_finder_amount(type, password, uppercase):
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


#used for finding the number of lowercase letters and adding lowercase letters to the password
def lowercase_finder_amount(type, password, lowercase):
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

#used for finding the number of numbers and adding numbers to the password
def number_finder_amount(type, password, number_amount):
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
    
#used for finding the number of special charecters and adding special charecters to the password
def special_finder_amount(type, password, special):
    if type == 0:
        while True:
            try: 
                special = int(input("How many special charecters do you want?: "))
                break
            except: 
                print("invalid input")
                continue
        return special
    
    elif type == 1:
        special -= 1
        password += special_charecters[random.randint(0,5)]
        return password, special

#used for randomizing what the next charecter is and making sure to use the correct amounts
def password_generator(uppercase, lowercase, number_amount, special, password):
    password = ""
    while True:
        next_charecter = random.randint(0,3)
        if uppercase != 0 and next_charecter == 0:
            password, uppercase = uppercase_finder_amount(1,password, uppercase)
        elif lowercase != 0 and next_charecter == 1:
            password, lowercase = lowercase_finder_amount(1,password, lowercase)
        elif number_amount != 0 and next_charecter == 2:
            password, number_amount = number_finder_amount(1,password, number_amount)
        elif special != 0 and next_charecter == 3:
            password, special = special_finder_amount(1,password, special)
        if uppercase == 0 and lowercase == 0 and number_amount == 0 and special == 0:
            return password
        else:
            continue

#has all the stuff that the user can see and what will be the end of the program when done
def main():
    while True:
        leave = input("Do you want to leave? (yes or no): ")
        if leave == "yes":
            break
        password = ""
        uppercase = 0
        lowercase = 0
        special = 0
        number_amount = 0

        while True:

            try: length = int(input("What is the total length of the password?: "))
            except: 
                print("invalid input")
                continue

            uppercase = uppercase_finder_amount(0,password, uppercase)
            lowercase = lowercase_finder_amount(0,password, lowercase)
            special = special_finder_amount(0,password, special)
            number_amount = number_finder_amount(0, password, number_amount)

            if uppercase + lowercase + special + number_amount == length:
                break
            else:
                print("You can't have more or less charecters than total length!")
                continue

        uppercase_one = uppercase
        uppercase_two = uppercase
        uppercase_three = uppercase
        lowercase_one = lowercase
        lowercase_two = lowercase
        lowercase_three = lowercase
        number_amount_one = number_amount
        number_amount_two = number_amount
        number_amount_three = number_amount
        special_one = special
        special_two = special
        special_three = special

        password = password_generator(uppercase, lowercase, number_amount, special, password)
        print()
        print("Your first password is:", password)
        print()

        password = password_generator(uppercase_one, lowercase_one, number_amount_one, special_one, password)
        print("Your second password is:", password)
        print()

        password = password_generator(uppercase_two, lowercase_two, number_amount_two, special_two, password)
        print("Your third password is:", password)
        print()

        password = password_generator(uppercase_three, lowercase_three, number_amount_three, special_three, password)
        print("Your fourth password is:", password)

#runs main
main()

#just some stuff to blank screen and say have a good day in center
for number in range(30):
    print()

print("Have a good day!")

for number in range(15):
    print()
