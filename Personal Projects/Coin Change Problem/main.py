#Alex Anderson, Coin Change Problom

import csv

def pull_denominations(country):
    denominations = {}

    with open("Personal Projects/Coin Change Problem/coin_denominations.csv", "r", newline='') as file:
        reader = csv.reader(file)
        lines = []
        for line in reader:
            lines.append(line)

        if country == 'Usa':
            for item in lines[0]:
                item_list = item.split("-")
                denomination_name = item_list[0] 
                denomination_worth = int(item_list[1])
                denominations[denomination_name] = denomination_worth
        
        elif country == 'Europe':
            for item in lines[1]:
                item_list = item.split("-")
                denomination_name = item_list[0] 
                denomination_worth = int(item_list[1])
                denominations[denomination_name] = denomination_worth
        
        elif country == 'Japan':
            for item in lines[2]:
                item_list = item.split("-")
                denomination_name = item_list[0] 
                denomination_worth = int(item_list[1])
                denominations[denomination_name] = denomination_worth
        
        elif country == 'England':
            for item in lines[3]:
                item_list = item.split("-")
                denomination_name = item_list[0] 
                denomination_worth = int(item_list[1])
                denominations[denomination_name] = denomination_worth
        
        return denominations


def needed_amounts(denominations, amount):
    amounts = []
    number_of_items = -1
    used = []
    named_used = {}

    for item in denominations:
        named_used[item] = 0

    for item in denominations:
        number_of_items += 1
        amounts.append(denominations[item])

    sorted_amounts = sorted(amounts, reverse=True)

    for item in sorted_amounts:

        while True:
            if amount >= item:
                used.append(item)
                amount -= item
                continue

            else:
                break

    for item in used:
        for i in denominations:
            if item == denominations[i]:
                named_used[i] += 1
    
    return(named_used)

def main():
    print("Welcome to the coin change machiene!")
    country = input("What country's currency are you using (Usa, Europe, Japan, or England): ").strip().capitalize()
    denominations = pull_denominations(country)
    amount = int(input("What is the amount of money you need?: "))
    amount = amount*100
    used = needed_amounts(denominations, amount)
    
    for i in used:
        print("You need to have",i,used[i])

main()