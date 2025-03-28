#Alex Anderson, Coin Change Problom

from info import *
from calculator import *

def main():
    print("Welcome to the coin change machiene!")
    country = input("What country's currency are you using (Usa, Europe, Japan, or England): ").strip().capitalize()
    denominations = info_pull(country)
    amount = int(input("What is the amount of money you need?(type without the decimal point, (example: instead of 10.75 do 1075): "))
    used = coin_amounts(denominations, amount)
    
    for i in used:
        print("You need to have",i,used[i])

main()