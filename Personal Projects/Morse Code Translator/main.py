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
        placement = alphabet.index(item)
        morse_charecters += morse_alphabet[placement]
    
    if morse_charecters[1] == ' ':
        print()

english_morse(alphabet, morse_alphabet)