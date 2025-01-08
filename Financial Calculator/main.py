
choice_input = int(input("1= Goal Tester, 2= Compound Interest Calculator, 3= Budget Allocator, 4= Sale Price Calculator, 5= Tip Calculator"))

if choice_input == 1:
    week_or_monthly = int(input("would you like to base it on weekly or monthly deposits?(type 1 for weekly and type 2 for monthly): "))
    if week_or_monthly == 1:
        deposit = int(input("How much are you planning on depositing every week?: "))
        goal = int(input("What is your goal?: "))
        Goal_Timeline = int(goal/deposit)
        print("It will take you", Goal_Timeline, "weeks to get to your goal.")