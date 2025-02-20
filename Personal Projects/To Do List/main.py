#Alexander Anderson To Do List

import csv

def adder():
    with open('Personal Projects/To Do List/tasks.txt', 'r', newline='') as file:
        while True:
            identical_found = False
            task_name = input("What is the name of the task you wish to add?(type 'leave' if you want to leave): ")
            if task_name == "leave":
                break
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                if row[0] == task_name:
                    print("You can not have two identical tasks!")
                    identical_found = True
                    break
            if identical_found == True:
                continue
            break

    with open('Personal Projects/To Do List/tasks.txt', 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([task_name, "no"])

def remover():
    while True:
        task_name = input("What is the name of the task you wish to remove? (type 'leave' if you want to leave): ")
        
        if task_name.lower() == "leave":
            break

        with open('Personal Projects/To Do List/tasks.txt', 'r', newline='') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            tasks = list(csv_reader)
        
        updated_tasks = [task for task in tasks if task and task[0] != task_name]

        if len(updated_tasks) == len(tasks):
            print("Task not found. Try again.")
            continue

        else:
            print("Task Found and Removed!")

        with open('Personal Projects/To Do List/tasks.txt', 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(updated_tasks)
        break

adder()
remover()
