#Alex Anderson, Coin Change Problem, info puller

import csv

def info_pull(country):
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
    
    denominations = pull_denominations(country)
    return denominations