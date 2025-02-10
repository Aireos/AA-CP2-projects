#Alex Anderson, Reading files notes

# import csv



# how to open files in your program

# with open('Notes/Reading Files/text.txt', "r") as file:
#     content = file.read()
#     index = content.find("Hello")
#     print(content[index:index+1])
#     print(content[index:index+5])



# how to alter text to work as data in a program

# with open("Notes/Reading Files/Class CSV sample - Sheet1.csv", "r") as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     print("----------------------------------------------")
#     for row in csv_reader:
#         print(f'username: {row[0]}')
#         print(f'favorite color: {row[1]}')
#         print("----------------------------------------------")



#how to pull information from a csv into a dictionary

# users = {}

# with open("Notes/Reading Files/Class CSV sample - Sheet1.csv", "r") as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     for row in csv_reader:
#         users.update({row[0]:row[1]})

# print(users)



#A CSV file is a file that has text inside of it in rows



#They are used in programing for storing large amounts of information and text