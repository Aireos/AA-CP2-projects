#Alex Anderson Update Personal Library

#used before every other function to have the function know what the song is they are trying to add, remove, etc.
def making():
    song_name = input("what is the name of the song?: ")
    song_auther = input("who wrote the song?: ")

    while True:
        try:
            song_age = int(input("when was the song made?: "))
        except:
            print("invalid input")
            continue
        break

    song = (song_name,song_auther,song_age)
    return song


#pretty straight forward, just adds the song to the list of all of their songs.
def adding(song,song_list):
    song_list.add(song)
    return song_list


#makes sure the song is in the song_list and then removes it if it is.
def removing(song,song_list):
    if song in song_list:
        song_list.remove(song)
        return song_list
    
    else:
        print("invalid song")
        return song_list


#also straight forward, just checks if the song is in the song_list and returns false if it is not and returns true if it is.
def finding(song,song_list):
    if song in song_list:
        return True
    
    else:
        print("that song is not in your playlist")
        return False


#just prints the facts for every song in their playlist
def display(song_list):
    print("here is a list of all the songs in your playlist:")
    for item in song_list:
        print()
        print(item[0], "by", item[1], "made in", item[2])

#Code to update information for each song
def update(song_list):
    print("songs:")
    for item in song_list:
      print(item[0])
    song_to_update = input("What song do you want to update?: ")


#the main function that has the most user inputs and has the input to find what they want to do.
def main():
    song_list = set()
    while True:
        print()
        to_do = input("would you like to add, remove, find, display, update, or leave?: ")

        if to_do == "add":
            song = making()
            song_list = adding(song,song_list)

        elif to_do == "remove":
            song = making()
            song_list = removing(song,song_list)
        
        elif to_do == "find":
            song = making()
            found = finding(song,song_list)
            if found == True:
                print(song[0], "by", song[1], "made in", song[2], "is in your playlist.")
        
        elif to_do == "display":
            display(song_list)

        elif to_do == "update":
            update(song_list)
        
        elif to_do == "leave":
            break


#runs the main function
main()
print("Bye!")
