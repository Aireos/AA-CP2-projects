#Alex Anderson Financial Calculator

#needed throught the program to change numbers from intigers to floats and from floats to intigers
def type_fixer(text):
    try:
        if "." in text:
            text = float(text)
            return text
        else:
            text = int(text)
            return text
    except:
        print("Invalid input")
        return False

#used in 2(Compound Interest Calculator)        
def interest_calc(interest_amount, interest, month_number):
    interest_amount = (interest_amount*interest)+interest_amount
    interest_amount = "{0:.2f}".format(interest_amount)
    interest_amount = type_fixer(interest_amount)
    month_number += 1
    print("After", month_number, "month(s) you will have:", interest_amount)
    return interest_amount, month_number

def goal_tester():
    week_month = int(input("Would you like to base it on weekly or monthly deposits?(type 1 for weekly and type 2 for monthly): "))        
    if week_month == 1:
        deposit = type_fixer((input("How much are you planning on depositing every week?: ")))
        if deposit == False: 
            return
        goal = type_fixer((input("What is your goal?: ")))
        if goal == False: 
            return                  
        Goal_Timeline = int(goal/deposit)
        print("It will take you", Goal_Timeline, "week(s) to get to your goal.")
        return
    if week_month == 2:
        deposit = type_fixer((input("How much are you planning on depositing every month?: ")))
        if deposit == False: 
            return
        goal = type_fixer((input("What is your goal?: ")))
        if goal == False: 
            return         
        goal_timeline = int(goal/deposit)
        print("It will take you", goal_timeline, "month(s) to get to your goal.")

def Compound_Interest_Calculator():
    month_number = 0
    interest_amount = type_fixer(input("How much money is having interest?: "))
    if interest_amount == False: 
        return
    interest = type_fixer(input("What is the interest percentage?: "))
    if interest == False: 
        return                
    interest = interest/100
    while month_number < 10:
        interest_amount, month_number = interest_calc(interest_amount, interest, month_number)
    return

def Budget_allocator():
    hundred_p = False
    allocations_list = []
    precentage_total = 0
    budget = type_fixer(input("How much money are you allocating?: "))
    if budget == False: 
        return
    allocations = int(input("How many things are you allocating to?: "))        
    if allocations == 1:
        print("Just put that much money into it!")
        return
                
    while allocations > 0 and hundred_p == False:
        allocations -= 1
        allocation_name = input("What is the name for this allocation?: ")
        percentage = int(input("What percentage are you putting into this allocation?: "))
        if percentage == 100:
            print("Just put that much money into it!")
            hundred_p = True
            return
        print()
        percentage = percentage/100
        allocation_list = [allocation_name, percentage]
        allocations_list.append(allocation_list)
    if hundred_p == True:
        return
    for list in allocations_list:
        precentage_total += list[1]       
    if precentage_total > 1:
        print("You can't have over 100%!")
        return
    elif precentage_total < 1:
        print("You can't have under 100%!")
        return
                
    for list in allocations_list:
        allocation_amount = list[1]*budget
        list = list.append(allocation_amount)
                
    for list in allocations_list:
        print("You will be putting", type_fixer(list[2]), "in", type_fixer(list[0]))
    return

def Sale_Price_Calculator():
    original_price = type_fixer(input("What is the original price for the item?: "))
    if original_price == False: 
        return
    discount = type_fixer(input("What is your total percentage off?: "))
    if discount == False:
        return                
    discount = discount/100
    final_price = original_price - (original_price*discount)
    print("The price of the product is", final_price)
    return

def Tip_calculator():

def main():
    while True:
        #direction choice
        print("1= Goal Tester, 2= Compound Interest Calculator, 3= Budget Allocator, 4= Sale Price Calculator, 5= Tip Calculator, 6= exit")
        choice_input = int(input("What would you like to do?: "))

        #goal tester

        if choice_input == 1:
            goal_tester()
        
        #Compound Interest Calculator
        elif choice_input == 2:
            Compound_Interest_Calculator()

        #Budget allocator
        elif choice_input == 3:
            Budget_allocator()

        #Sale Price Calculator
        elif choice_input == 4:
            Sale_Price_Calculator()

        #Tip Calculator
        elif choice_input == 5:
            before_tip = type_fixer(input("What was the orginal price?: "))
            if before_tip == False: 
                continue
            tip = type_fixer(input("What is the precentage you want to tip?: "))
            if tip == False: 
                continue                
            tip = tip/100
            after_tip = before_tip + (tip*before_tip)
            print("The final price will be", after_tip)
            continue

        #break statement
        elif choice_input == 6:
            print("Thanks for using my financial calculator, and have a good day!")
            break

        #in case they don't enter 1-6
        else:
            print("Invalid input.")
            continue
main()
        
        
        
        
