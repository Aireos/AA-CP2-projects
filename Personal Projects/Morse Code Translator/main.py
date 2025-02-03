#Alexander Anderson Simple Morse Code Translator

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
morse_alphabet = ["._","_...","_._.","_..",".",".._.","__.","....","..",".___","_._","._..","__","_.","___",".__.","__._","._.","...","_",".._","..._",".__","_.._","_.__","__.."," "]

def english_morse(alphabet, morse_alphabet):
    english_charecters = []
    morse_charecters = []
    english = input("What do you want to change to morse code: ")
    
    for item in english:
        english_charecters += item
        english_charecters += " "

    for item in english_charecters:
        try:
            placement = alphabet.index(item)
        except:
            print("invalid charecter used")
            continue
            
        morse_charecters += morse_alphabet[placement]
    
    morse = ' '.join(morse_charecters)
    print("In morse:", morse)

def morse_english(alphabet, morse_alphabet):
    english_charecters = []
    morse_charecters = []
    morse = input("What do you want to change to morse code: ")
    
    for item in morse:
        morse_charecters += item
        morse_charecters += " "

    for item in morse_charecters:
        try:
            placement = morse_alphabet.index(item)
        except:
            print("invalid charecter used")
            continue
            
        english_charecters += alphabet[placement]
    
    english = ' '.join(morse_charecters)
    print("In english:", english)

def main(alphabet, morse_alphabet):
    while True:
        try:
            choice = int(input("1 = english to morse, 2 = morse to english, 3 = leave"))
        except:
            print("invalid input")
            continue
            
        if choice != 1 and choice != 2 and choice != 3:
            print("invalid input")
            continue
            
        if choice == 1:
            english_morse()

        if choice == 2:
            morse_english()

        if choice == 3:
            print("Have a good day!")
            break
            
main(alphabet, morse_alphabet)
