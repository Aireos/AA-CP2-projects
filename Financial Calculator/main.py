#Alex Anderson Financial Calculator


def interest_calc(interest_amount, interest, month_number):
    interest_amount = ((interest_amount*interest)+interest_amount)
    month_number += 1
    print("After", month_number, "month you will have:", interest_amount)
    return interest_amount, month_number

def type_fixer(text):
    try:
        if "." in text:
            text = float(text)
        else:
            text = int(text)
        return text
    except:
        print("Invalid input.")
        return False
        
def main():
    while True:
    
        print("1= Goal Tester, 2= Compound Interest Calculator, 3= Budget Allocator, 4= Sale Price Calculator, 5= Tip Calculator, 6= exit")
        choice_input = int(input("What would you like to do?: "))
        
        if choice_input == 1:
            week_or_monthly = int(input("Would you like to base it on weekly or monthly deposits?(type 1 for weekly and type 2 for monthly): "))
        
            if week_or_monthly == 1:
                deposit = type_fixer((input("How much are you planning on depositing every week?: ")))
                if deposit == False: continue
                goal = type_fixer((input("What is your goal?: ")))
                if goal == False: continue
                    
                Goal_Timeline = int(goal/deposit)
                print("It will take you", Goal_Timeline, "week(s) to get to your goal.")
        
            if week_or_monthly == 2:
                deposit = type_fixer((input("How much are you planning on depositing every month?: ")))
                if deposit == False: continue
                goal = type_fixer((input("What is your goal?: ")))
                if goal == False: continue
                    
                goal_timeline = int(goal/deposit)
                print("It will take you", goal_timeline, "month(s) to get to your goal.")

        
        if choice_input == 2:
            month_number = 0
            interest_amount = type_fixer(input("How much money is having interest?: "))
            if interest_amount == False: continue
            interest = type_fixer((input("What is the interest percentage?: ")))
            if interest == False: continue
                
            interest = interest/100
            while month_number < 10:
                interest_amount, month_number = interest_calc(interest_amount, interest, month_number)

        
        if choice_input == 3:
            allocations_list = []
            precentage_total = 0
            budget = type_fixer(input("How much money are you allocating?: "))
            if budget == False: continue
            allocations = int(input("How many things are you allocating to?: "))
            
            if allocations == 1:
                print("Just put that much money into it!")
                continue
                
            while allocations > 0:
                allocations -= 1
                allocation_name = input("What is the name for this allocation?: ")
                allocation_percentage = int(input("What percentage are you putting into this allocation?: "))
                print()
                allocation_percentage = allocation_percentage/100
                allocation_list = [allocation_name, allocation_percentage]
                allocations_list.append(allocation_list)
                
            for list in allocations_list:
                print(list[1])
                precentage_total += list[1]
                
            if precentage_total > 1:
                print("You can't have over 100%!")
                continue
                
            for list in allocations_list:
                allocation_amount = list[1]*budget
                list += allocation_amount
                
            for list in allocations_list:
                print("You will be putting", list[2], "in", list[0] + ".")

        
        if choice_input == 4:
            original_price = type_fixer(input("What is the original price for the item?: "))
            if original_price == False: continue
            discount_percentage = type_fixer(input("What is your total percentage off?: "))
            if discount_percentage == False: continue
                
            discount_percentage = discount_percentage/100
            final_price = original_price*discount_percentage
            print("The price of the product is", final_price + "$.")

        
        if choice_input == 5:
            before_tip = type_fixer(input("What was the orginal price?: "))
            if before_tip == False: continue
            tip_percentage = type_fixer(input("What is the precentage you want to tip?: "))
            if tip_percentage == False: continue
                
            tip_percentage = tip_percentage/100
            after_tip = tip_percentage*before_tip
            print("The final price will be", afer_tip + ".")

        
        if choice_input == 6:
            print("Thanks for using my financial calculator, and have a good day!")
            break

        
        else:
            print("Invalid input.")
            continue
main()
        
        
        
        
