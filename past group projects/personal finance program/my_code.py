import csv

# function that reads the data and returns it as a list
def read_info():
    with open("info.csv", "r") as file:
        reader = csv.reader(file)
        row = next(reader)
        return row

# function that writes the updated data back into info.csv
def save_info(row):
    with open("info.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

# function to safely read the csv file and return data
def safe_read_info():
    try:
        return read_info()
    except Exception as e:
        print("Error reading info.csv:", e)
        return ["", "", "[]", "[]"]

# function to convert a string to a list of dictionaries
def string_to_list_of_dicts(s):
    s = s.strip()[1:-1]
    items = s.split('},')
    result = []
    
    for item in items:
        item = item.strip().strip('{}') 
        if item:
            kv_pairs = item.split(',')  #split by commas between pairs
            d = {}
            for pair in kv_pairs:
                key, value = pair.split(':')
                d[key.strip().strip('"')] = value.strip().strip('"')
            result.append(d)
    
    return result

# function to convert a list of dictionaries to a string
def list_of_dicts_to_string(lst):
    result = "["
    for d in lst:
        result += "{"
        for key, value in d.items():
            result += f'"{key}": "{value}", '
        result = result.rstrip(', ')
        result += "}, "
    result = result.rstrip(', ')
    result += "]"
    return result

# function to add expense entries (date, amount, category)
def expense_entry():
    row = safe_read_info()
    try:
        expense_list = string_to_list_of_dicts(row[2])
    except:
        print("Error: Malformed expense data.")
        expense_list = []

    while True:
        try:
            count = int(input("How many expense entries do you want to add?: "))
            break
        except:
            print("That is not a valid number.")
            continue

    for i in range(count):
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the expense category: ")
        while True:
            try:
                amount = float(input("Enter the expense amount: "))
                break
            except:
                print("That is not a valid number.")
                continue

        # create expense dictionary and add it to the list
        expense = {
            "date": date,
            "category": category,
            "amount": amount
        }

        expense_list.append(expense)

    row[2] = list_of_dicts_to_string(expense_list)
    save_info(row)
    return expense_list


# function to set up or update a budget limit for a category
def set_budget():
    row = safe_read_info()
    try:
        expense_list = string_to_list_of_dicts(row[2])
    except:
        print("Error: Malformed expense data.")
        expense_list = []

    category = input("Enter the category you want to set a budget for: ")
    while True:
        try:
            budget_limit = float(input("Enter the budget limit: "))
            break
        except:
            print("That is not a valid number.")
            continue

    # set the budget for the category
    for expense in expense_list:
        if expense["category"] == category:
            expense["budget_limit"] = budget_limit
            print("Budget limit for", category, "set to", budget_limit)

    row[2] = list_of_dicts_to_string(expense_list)
    save_info(row)
    return expense_list


# function to add income entries (date, amount, source)
def income_entry():
    row = safe_read_info()
    try:
        income_list = string_to_list_of_dicts(row[1])
    except:
        print("Error: Malformed income data.")
        income_list = []

    while True:
        try:
            count = int(input("How many income entries do you want to add?: "))
            break
        except:
            print("That is not a valid number.")
            continue

    for i in range(count):
        date = input("Enter the date (YYYY-MM-DD): ")
        source = input("Enter the income source: ")
        while True:
            try:
                amount = float(input("Enter the income amount: "))
                break
            except:
                print("That is not a valid number.")
                continue

        # create income dictionary and add it to the list
        income = {
            "date": date,
            "source": source,
            "amount": amount
        }

        income_list.append(income)

    row[1] = list_of_dicts_to_string(income_list)
    save_info(row)
    return income_list


#function that sets new goals or adds to previos goals
def goals_tracker(goals):
    current_goals = []

    # if there are existing goals, load them
    if goals is not None:
        current_goals.extend(goals)
    else:
        goals = {}

    if current_goals:
        choice = input("Do you want to 1(make new goals) or 2(add to previous goals): ")
        if choice == "1":
            # make a new goal
            goal_name = input("Enter the goal name: ")
            while True:
                try:
                    goal_amount = float(input("Enter the goal amount: "))
                    break
                except:
                    print("That is not a valid number.")
                    continue
            while True:
                try:
                    earned = float(input("Enter the amount earned towards the goal: "))
                    break
                except:
                    print("That is not a valid number.")
                    continue
            current_goals.append({
                'goal_name': goal_name,
                'goal_amount': goal_amount,
                'earned': earned
            })
            print("New goal", goal_name, "added with a target of", goal_amount, "and earned", earned)

        elif choice == "2":
            # add to an existing goal
            print("Existing goals:")
            for i in range(len(current_goals)):
                print(i + 1, ".", current_goals[i]['goal_name'], "- Target:", current_goals[i]['goal_amount'], "- Earned:", current_goals[i]['earned'])

            goal_choice = int(input("Enter the number of the goal you want to add to: ")) - 1

            if 0 <= goal_choice < len(current_goals):
                while True:
                    try:
                        additional_earned = float(input("Enter the additional amount earned: "))
                        break
                    except:
                        print("That is not a valid number.")
                        continue
                current_goals[goal_choice]['earned'] += additional_earned
                print("Added", additional_earned, "to goal", current_goals[goal_choice]['goal_name'])
            else:
                print("Invalid goal number.")

    else:
        print("no existing goals, creating a new goal")
        goal_name = input("Enter the goal name: ")
        while True:
            try:
                goal_amount = float(input("Enter the goal amount: "))
                break
            except:
                print("That is not a valid number.")
                continue
        while True:
            try:
                earned = float(input("Enter the amount earned towards the goal: "))
                break
            except:
                print("That is not a valid number.")
                continue
        current_goals.append({
            'goal_name': goal_name,
            'goal_amount': goal_amount,
            'earned': earned
        })

    # saves the updated goals back to the csv
    row = safe_read_info()
    row[3] = list_of_dicts_to_string(current_goals)
    save_info(row)
    return current_goals


# function to convert currencys
def convert_currency():
    while True:
        try:
            amount = float(input("Enter the amount to convert in dollars: "))
            break
        except:
            print("That is not a valid number.")
            continue

    currency = input("Enter the currency to convert to (yen, euros, or pounds): ")

    if currency == "yen":
        print("Amount in yen:", amount * 148.41)
    elif currency == "euros":
        print("Amount in euros:", amount * 0.92)
    elif currency == "pounds":
        print("Amount in pounds:", amount * 0.77)
    else:
        print("Invalid currency choice.")