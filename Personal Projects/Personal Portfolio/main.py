#Alex Anderson, Personal Portfolio

from morse_trans import morse_trans
from battle_sim import battle_sim
from finance_calc import finance_calc
from movie_recommender import movie_recommender
from personal_library import personal_library
from to_do import to_do

def main():
    print("This is my profolio of my top 6 favorite projects I have made by 4/6/2025.")
    print("I will ask you which one you want to view and it will tell you a short spiel on it and then let you try it out.")

    while True:
        print("\n1. battle simulator \n2. financial calculator \n3. movie recommender \n4. morse code translator \n5. to do list maker \n6. personal song library")

        try:
            choice = int(input("Choice: "))
        except:
            print("That was not a number")
            continue
        
        if choice not in [1,2,3,4,5,6]:
            print("You can only chose from 1-6")
            continue

        if choice == 1:
            print("The battle simulator starts by asking you if you want to add a character, view current characters, battle with the characters, or exit and then does whatever you picked")
            print("programming procces?")
            print("I learned how to use f-string more and how to organize data and save it in a clean manner.")
            print()


main()