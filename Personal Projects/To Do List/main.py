#Alex Anderson, To Do List

import csv


#Function to add a task
def adder():
    try:
        with open('Personal Projects/To Do List/tasks.txt', 'r', newline='') as file:
            csv_reader = csv.reader(file)
            try:
                next(csv_reader)

            except StopIteration:
                pass

            tasks = list(csv_reader)

    except FileNotFoundError:
        tasks = []
    
    while True:
        identical_found = False
        task_name = input("What is the name of the task you wish to add? (type 'leave' if you want to leave): ").strip()

        if task_name.lower() == "leave":
            break
        
        if not task_name:
            print("Task name cannot be empty.")
            continue

        for row in tasks:
            if row and row[0] == task_name:
                print("You can not have two identical tasks!")
                identical_found = True
                break

        if identical_found:
            continue
        break

    with open('Personal Projects/To Do List/tasks.txt', 'a', newline='') as file:
        csv_writer = csv.writer(file)

        if not tasks:
            csv_writer.writerow(["Task", "Completed"])

        csv_writer.writerow([task_name, "no"])


#Function to remove a task
def remover():
    try:
        with open('Personal Projects/To Do List/tasks.txt', 'r', newline='') as file:
            csv_reader = csv.reader(file)

            try:
                next(csv_reader)

            except StopIteration:
                print("No tasks to remove.")
                return
            
            tasks = list(csv_reader)

    except FileNotFoundError:
        print("No tasks file found.")
        return
    
    if not tasks:
        print("No tasks available to mark as done.")
        return
    
    while True:
        task_name = input("What is the name of the task you wish to remove? (type 'leave' if you want to leave): ").strip()

        if task_name.lower() == "leave":
            break

        updated_tasks = [task for task in tasks if task and task[0] != task_name]

        if len(updated_tasks) == len(tasks):
            print("Task not found. Try again.")
            continue

        print("Task Found and Removed!")

        with open('Personal Projects/To Do List/tasks.txt', 'w', newline='') as file:
            csv_writer = csv.writer(file)

            if updated_tasks:
                csv_writer.writerow(["Task", "Completed"])
                csv_writer.writerows(updated_tasks)

            else:
                file.truncate()
        break


#Function to mark a task as completed
def mark_as_done():
    try:
        with open('Personal Projects/To Do List/tasks.txt', 'r', newline='') as file:
            csv_reader = csv.reader(file)

            try:
                next(csv_reader)

            except StopIteration:
                print("No tasks to mark as done.")
                return
            
            tasks = list(csv_reader)

    except FileNotFoundError:
        print("No tasks file found.")
        return
    
    if not tasks:
        print("No tasks available to mark as done.")
        return
    
    while True:
        task_name = input("What is the name of the task you wish to mark as done? (type 'leave' if you want to leave): ").strip()

        if task_name.lower() == "leave":
            break
        
        found = False

        for task in tasks:
            if task and task[0] == task_name:
                task[1] = "yes"
                found = True
                break

        if not found:
            print("Task not found. Try again.")
            continue

        with open('Personal Projects/To Do List/tasks.txt', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["Task", "Completed"])
            csv_writer.writerows(tasks)

        print("Task Marked as Done!")
        break


#function to view all the tasks and if they are complete
def view_tasks():
    try:
        with open('Personal Projects/To Do List/tasks.txt', 'r', newline='') as file:
            csv_reader = csv.reader(file)
            tasks = list(csv_reader)

            if len(tasks) <= 1:
                print("No tasks available.")
                return
            
            print("\nTasks:")

            for task in tasks[1:]:
                part_one = task[0]

                if task[1] == "no":
                    part_two = "Not completed"

                elif task[1] == "yes":
                    part_two = "Completed"

                print(part_one + ",", part_two)

    except FileNotFoundError:
        print("No tasks file found.")
        return
    
    
#Combines all the parts with a choice input
def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as done")
        print("4. View all tasks")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            adder()
        elif choice == "2":
            remover()
        elif choice == "3":
            mark_as_done()
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


main()