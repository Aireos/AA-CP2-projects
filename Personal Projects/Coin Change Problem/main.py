#Alex Anderson, Coin Change Problom

from info import *
from calculator import *

#main user interface
def main():
    #telling the user what it is
    print("Welcome to the coin change machiene!")

    while True:
        #having them select which countrys currency they want to use
        countrys = ["Usa", "Europe", "Japan", "England"]
        while True:
            country = input("What country's currency are you using (Usa, Europe, Japan, or England): ").strip().capitalize()
            if country not in countrys:
                print("that is not a valid country, please choose from the list of countrys.")
                continue
            break

        #having them select the amount of money they need
        denominations = info_pull(country)
        while True:
            try: 
                amount = int(input("What is the amount of money you need?(type without the decimal point, (example: instead of 10.75 do 1075): "))
                break
            except:
                print("please follow the guide for what to type")
                continue

        #finds how much of each coin they need
        used = coin_amounts(denominations, amount)
        
        #prints how much of each coin they need
        for i in used:
            print("You need to have",used[i],i)
        
        #asks if the user wants to do it again
        again = input("Type yes if you want to run it again: ").strip().lower()

        if again == "yes":
            continue

        else:
            break
main()