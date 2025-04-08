
def simple_quiz():
    correct = False

    N_O_C = 0

    def C_O_I(user_answer, answer):

        correct = False

        if user_answer == answer:
            print()
            print("You got it right!")
            print()
            correct = True
            return correct

        else:
            print()
            print("You got it wrong.")
            print()
            correct = False
            return correct
        
    print()
    print("math quiz time!")
    print()


    #first question
    user_answer = int(input("What is 2+1 (1, 2, 3 or 4): "))
    answer = 3
    correct = C_O_I(user_answer, answer)

    while True:
        #second question hard
        if correct == True:
            N_O_C += 1
            user_answer = int(input("What is 2-1 (1, 2, 3 or 4): "))
            answer = 1
            correct = C_O_I(user_answer, answer)
            break

        #second question easy
        elif correct == False:
            user_answer = int(input("What is 1+1 (1, 2, 3 or 4): "))
            answer = 2
            correct = C_O_I(user_answer, answer)
            break

    while True:
        #third question hard
        if correct == True:
            N_O_C += 1
            user_answer = int(input("What is 4/2 (1, 2, 3 or 4): "))
            answer = 2
            correct = C_O_I(user_answer, answer)
            break

        #third question easy
        elif correct == False:
            user_answer = int(input("What is 4-2 (1, 2, 3 or 4): "))
            answer = 2
            correct = C_O_I(user_answer, answer)
            break

    while True:
        #fourth question hard
        if correct == True:
            N_O_C += 1
            user_answer = int(input("What is 2*2 (1, 2, 3 or 4): "))
            answer = 4
            correct = C_O_I(user_answer, answer)
            break

        #fourth question easy
        elif correct == False:
            user_answer = int(input("What is 2/2 (1, 2, 3 or 4): "))
            answer = 1
            correct = C_O_I(user_answer, answer)
            break

    while True:
        #fith question hard
        if correct == True:
            N_O_C += 1
            user_answer = int(input("What is (1.50000015*3.333333)-1 (1, 2, 3 or 4): "))
            answer = 4
            correct = C_O_I(user_answer, answer)
            if correct == True:
                N_O_C += 1
            break

        #fith question easy
        elif correct == False:
            user_answer = int(input("What is 5/5 (1, 2, 3 or 4): "))
            answer = 1
            correct = C_O_I(user_answer, answer)
            if correct == True:
                N_O_C += 1
            break

    print("You got:", N_O_C, "/ 5 correct.")
