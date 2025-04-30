#Alex Anderson, Somthing to do if I am bored

import random

classes = ["","","",""]
#
classes_info = [[],[],[],[]]
races = ["","","",""]
#
races_info = [[],[],[],[]]

def class_choice(classes, classes_info):
    while True:
        number = 0
        for class_ in classes:
            number += 1
            print(f"{number}. {class_}")
        chosen_class = int(input("What class do you want to be? (just type the number):"))
        try:
            if chosen_class > number:
                print("That is not a valid choice number.")
                continue
        except:
            print("That was not a number!")
            continue
        number -= 1
        class_ = classes[number]
        class_info = classes_info[number]
        return(class_, class_info)

def race_choice(races, races_info):
    while True:
        number = 0
        for race in races:
            number += 1
            print(f"{number}. {race}")
        chosen_race = int(input("What race do you want to be? (just type the number):"))
        try:
            if chosen_race > number:
                print("That is not a valid choice number.")
                continue
        except:
            print("That was not a number!")
            continue
        number -= 1
        race = races[number]
        race_info = races_info[number]
        return(race, race_info)

def d_six():
    return(random.randint(1, 6))

def stat_decider():
    stat_list = []
    for number in range(6):
        stat_1 = d_six()
        stat_2 = d_six()
        stat_3 = d_six()
        stat_4 = d_six()
        top_three = (sorted([stat_1, stat_2, stat_3, stat_4]))[:3]
        stat = 0
        for item in top_three:
            stat += item
        stat_list.append(stat)
    return stat_list
        
        




def main():
    while True:
        print("Welcome to the automatic dnd character creator!")
        stat_list = stat_decider()
        print(stat_list)
        return
        

main()