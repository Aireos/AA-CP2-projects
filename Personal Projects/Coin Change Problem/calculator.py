#Alex Anderson, Coin Change Problem, coin calculator

#function to find the amount of each coin that they need
def coin_amounts(denominations, amount):
    def needed_amounts(denominations, amount):
        #defining varaibles
        amounts = []
        number_of_items = -1
        used = []
        named_used = {}

        #making list of possible used coins
        for item in denominations:
            named_used[item] = 0

        for item in denominations:
            number_of_items += 1
            amounts.append(denominations[item])

        #sorting possible coins from highest to lowest
        sorted_amounts = sorted(amounts, reverse=True)

        #finding the used coins
        for item in sorted_amounts:
            while True:
                if amount >= item:
                    used.append(item)
                    amount -= item
                    continue

                else:
                    break

        #changing the coins from money form to name form
        for item in used:
            for i in denominations:
                if item == denominations[i]:
                    named_used[i] += 1
        
        return(named_used)
    
    named_used = needed_amounts(denominations, amount)
    return named_used