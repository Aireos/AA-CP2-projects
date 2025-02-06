#Alex Anderson Update Personal Library

#used before every other function to have the function know what the song is they are trying to add, remove, etc.
def making():
    song_name = input("what is the name of the song?: ")
    song_composer = input("who wrote the song?: ")
    song_album = input("What is the album that the song is in?: ")

    while True:
        try:
            song_length = int(input("What is the length in seconds of the song?: "))
        except:
            print("invalid input")
            continue
        break

    while True:
        try:
            song_age = int(input("when was the song made?: "))
        except:
            print("invalid input")
            continue
        break

    song = song_name[song_composer, song_length, song_album, song_age]
    return song

#pretty straight forward, just adds the song to the list of all of their songs.
def adding(song,song_dictionary):
    song_dictionary.add(song)
    return song_dictionary


#makes sure the song is in the song_dictionary and then removes it if it is.
def removing(song,song_dictionary):
    if song in song_dictionary:
        song_dictionary.remove(song)
        return song_dictionary
    
    else:
        print("invalid song")
        return song_dictionary


#also straight forward, just checks if the song is in the song_dictionary and returns false if it is not and returns true if it is.
def finding(song,song_dictionary):
    if song in song_dictionary:
        return True
    
    else:
        print("that song is not in your playlist")
        return False


#just prints the facts for every song in their playlist
def display(song_dictionary):
    print("here is a list of all the songs in your playlist:")
    for item in song_dictionary:
        print()
        print(item[0], "by", item[1], "made in", item[2])

#Code to update information for each song
def update(song_dictionary):
    print("songs:")
    for item in song_dictionary:
      print(item[0])
    song_to_update = input("What song do you want to update?: ")


#the main function that has the most user inputs and has the input to find what they want to do.
def main():
    song_dictionary = {

    }
    while True:
        print()
        to_do = input("would you like to add, remove, find, display, update, or leave?: ")

        if to_do == "add":
            song = making()
            song_dictionary = adding(song,song_dictionary)

        elif to_do == "remove":
            song = making()
            song_dictionary = removing(song,song_dictionary)
        
        elif to_do == "find":
            song = making()
            found = finding(song,song_dictionary)
            if found == True:
                print(song[0], "by", song[1], "made in", song[2], "is in your playlist.")
        
        elif to_do == "display":
            display(song_dictionary)

        elif to_do == "update":
            update(song_dictionary)
        
        elif to_do == "leave":
            break


#runs the main function
main()
print("Bye!")
