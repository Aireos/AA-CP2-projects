#Alexander Anderson Simple Morse Code Translator

#the two lists for the normal alphabet and the morse alphabet translation
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
morse_alphabet = ["._","_...","_._.","_..",".",".._.","__.","....","..",".___","_._","._..","__","_.","___",".__.","__._","._.","...","_",".._","..._",".__","_.._","_.__","__..",""]


#english to morse code function that asks what they want to change to morse code and prints it in morse code
def english_to_morse(alphabet, morse_alphabet):
    english_charecters = []
    morse_charecters = []
    english = input("What do you want to change to morse code: ")
    
    #makes the list of english letters
    for item in english:
        english_charecters += item

    #makes it into a list of morse code charecters
    for item in english_charecters:
        try:
            placement = alphabet.index(item)
        except:
            print("invalid charecter used")
            return
            
        morse_charecters += morse_alphabet[placement]
        morse_charecters += " "
    
    #joins morse code charecters into correct format
    morse = ''.join(morse_charecters)

    #prints the morse code
    print("In morse:", morse)


#morse code to english function that asks what they want to change to english and prints it in english
def morse_to_english(alphabet, morse_alphabet):
    english_charecters = []
    morse = input("What do you want to change to english: ")

    #splits morse code back into morse code charecters
    morse_charecters = morse.split(' ')

    #makes it into a list of english letters
    for item in morse_charecters:
        try:
            placement = morse_alphabet.index(item)
        except:
            print("|" + item + "|")
            print("invalid charecter used")
            return
        
        english_charecters += alphabet[placement]
    
    #joins english letters into correct format
    english = ''.join(english_charecters)

    #prints the english words
    print("In english:", english)


#function that combines all the other functions with a choice of what they want to do
def main(alphabet, morse_alphabet):
    while True:
        try:
            choice = int(input("1 = english to morse, 2 = morse to english, 3 = leave: "))
        except:
            print("invalid input")
            continue

        #makes sure they inputed 1, 2 or 3    
        if choice != 1 and choice != 2 and choice != 3:
            print("invalid input")
            continue
            
        #does choice 1 / does the english to morse code function
        if choice == 1:
            english_to_morse(alphabet, morse_alphabet)

        #does choice 2 / does the morse code to english function
        if choice == 2:
            morse_to_english(alphabet, morse_alphabet)

        #does choice 3 / leaves program
        if choice == 3:
            print("Have a good day!")
            break


#Runs program            
main(alphabet, morse_alphabet)
