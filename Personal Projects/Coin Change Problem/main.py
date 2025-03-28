#Alex Anderson, Coin Change Problom

from info import *
from calculator import *

def main():
    print("Welcome to the coin change machiene!")

    countrys = ["Usa", "Europe", "Japan", "England"]
    while True:
        country = input("What country's currency are you using (Usa, Europe, Japan, or England): ").strip().capitalize()
        if country not in countrys:
            print("that is not a valid country, please choose from the list of countrys.")
            continue
        break

    denominations = info_pull(country)
    while True:
        try: 
            amount = int(input("What is the amount of money you need?(type without the decimal point, (example: instead of 10.75 do 1075): "))
            break
        except:
            print("please follow the guide for what to type")
            continue
        
    used = coin_amounts(denominations, amount)
    
    for i in used:
        print("You need to have",i,used[i])

main()