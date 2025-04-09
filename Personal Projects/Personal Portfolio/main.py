#Alex Anderson, Personal Portfolio

from morse_trans import morse_trans
from battle_sim import battle_sim
from finance_calc import finance_calc
from movie_recommender import movie_recommender
from personal_library import personal_library
from simple_quiz import simple_quiz

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
morse_alphabet = ["._","_...","_._.","_..",".",".._.","__.","....","..",".___","_._","._..","__","_.","___",".__.","__._","._.","...","_",".._","..._",".__","_.._","_.__","__..",""]

#main function for user inputs
def main():
    print("This is my portfolio of my top 6 favorite projects I have made by 4/6/2025.")
    print("I will ask you which one you want to view, and it will tell you a short spiel on it and then let you try it out.")

    while True:
        print("\n1. Battle Simulator\n2. Financial Calculator\n3. Movie Recommender\n4. Morse Code Translator")
        print("5. Simple Quiz\n6. Personal Library\n7. Exit")

        try:
            choice = int(input("Choice: "))
            print("\n")
        except ValueError:
            print("That was not a number. Please enter a valid option.")
            continue

        if choice not in range(1, 8):
            print("You can only choose from 1-7.")
            continue

        #battle simulater info
        if choice == 1:
            print("The Battle Simulator allows you to manage characters and engage in battles.")
            print("I started by creating the necessary files, focusing on character management.")
            print("Then, I implemented battles and organized the project structure.")
            print("I learned a lot from this project including how to use csv files and how to orginize and keep data in a simple way.")
            print("Here is the project:\n")
            battle_sim()

        #financial calculator info
        elif choice == 2:
            print("It lets you test financial goals, calculate compound interest, allocate budgets, and compute tips.")
            print("I began with a type fixer function and developed features for budgeting and pricing.")
            print("Then, I added functionalities for calculating interest.")
            print("I learned how to deal with user inputs better and how to use more math stuff in programming.")
            print("Here is the project:\n")
            finance_calc()

        #movie recommender info
        elif choice == 3:
            print("The Movie Recommender suggests films based on user preferences.")
            print("I created a function to read movie data into a dictionary for easy access.")
            print("I learned about CSV handling and creating an interactive user experience.")
            print("Here is the project:\n")
            movie_recommender()

        #morse code translator info
        elif choice == 4:
            print("The Morse Code Translator converts text to Morse code and vice versa.")
            print("I developed functions to handle conversions between English and Morse code.")
            print("I learned about string manipulation and error handling for user input.")
            print("Here is the project:\n")
            morse_trans(alphabet, morse_alphabet)

        #simple quiz info
        elif choice == 5:
            print("The Simple Quiz tests users' math skills with various questions.")
            print("I created a function to ask questions and check user answers.")
            print("I learned about control flow and user input management.")
            print("Here is the project:\n")
            simple_quiz()

        #personal library info
        elif choice == 6:
            print("The Personal Library helps users manage their song collections.")
            print("I created functions to add, remove, find, and update songs.")
            print("I learned about data structures and creating an interactive library.")
            print("Here is the project:\n")
            personal_library()

        elif choice == 7:
            print("Thank you for exploring my projects. Goodbye!")
            break


main()
