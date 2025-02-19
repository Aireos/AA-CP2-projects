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
        writer = csv.writer(file)
        next(writer)
        writer.writerow([task_name, "no"])
        

adder()
