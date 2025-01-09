def interest_calc(interest_amount, interest, month_number):
    interest_amount = ((interest_amount*interest)+interest_amount)
    month_number += 1
    print("After", month_number, "month you will have:", interest_amount)
    return interest_amount, month_number

While true:
    print("1= Goal Tester, 2= Compound Interest Calculator, 3= Budget Allocator, 4= Sale Price Calculator, 5= Tip Calculator, 6= exit")
    choice_input = int(input("what would you like to do?: "))
    
    if choice_input == 1:
        week_or_monthly = int(input("would you like to base it on weekly or monthly deposits?(type 1 for weekly and type 2 for monthly): "))
    
        if week_or_monthly == 1:
            deposit = int(input("How much are you planning on depositing every week?: "))
            goal = int(input("What is your goal?: "))
            Goal_Timeline = int(goal/deposit)
            print("It will take you", Goal_Timeline, "week(s) to get to your goal.")
    
        if week_or_monthly == 2:
            deposit = int(input("How much are you planning on depositing every month?: "))
            goal = int(input("What is your goal?: "))
            goal_timeline = int(goal/deposit)
            print("It will take you", goal_timeline, "month(s) to get to your goal.")
    
    if choice_input == 2:
        month_number = 0
        interest_amount = int(input("How much money is having interest?: "))
        interest = int(input("What is the interest percentage?: "))
        interest = interest/100
        while month_number < 10:
            interest_amount, month_number = interest_calc(interest_amount, interest, month_number)
    
    if choice_input == 3:
        allocations_list = []
        budget = input("How much money are you allocating?: ")
        if budget.contains(".")
            budget = float(budget)
        else:
            budget = int(budget)
        allocations = int(input("How many things are you allocating to?: "))
        while allocations > 0:
            allocations -= 1
            allocation_name = input("what is the name for this allocation?: ")
            allocation_percentage = int(input("What percentage are you putting into this allocation?: "))
            allocation_percentage = allocation_percentage/100
            allocation_list = [allocation_name, allocation_percentage]
            allocations_list += allocation_list
        for list in allocations_list:
            percentage_total += list(1)
        if percentage_total > 1:
            print("you can't have over 100%!")
            continue
        for list in allocations_list:
            allocation_amount = (list(1)*budget)
            list += allocation_amount
        for list in allocations_list:
            print("You will be putting", list(2), "in", list(0))
            
    if choice_input == 4:
        original_price = input("What is the original price for the item?: ")
        if orginal_price.contains("."):
            original_price = float(original_price)
        else:
            original_price = int(original_price)
        discount_percentage = 
        
        
        
