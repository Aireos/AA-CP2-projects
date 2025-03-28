#Alex Anderson, Coin Change Problem, coin calculator

def coin_amounts(denominations, amount):
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
    
    named_used = needed_amounts(denominations, amount)
    return named_used