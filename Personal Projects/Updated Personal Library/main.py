#Alex Anderson Update Personal Library

# Function to find song details and return song
def making():
    song_name = input("What is the name of the song?: ")
    song_composer = input("Who wrote the song?: ")
    song_album = input("What is the album that the song is in?: ")

    while True:
        try:
            song_length = int(input("What is the length in seconds of the song?: "))
        except:
            print("Invalid input")
            continue
        break

    while True:
        try:
            song_age = int(input("When was the song made?: "))
        except:
            print("Invalid input")
            continue
        break

    # Creating a dictionary for the song
    song = {
        "composer": song_composer,
        "length": song_length,
        "album": song_album,
        "year": song_age
    }

    return song_name, song


# Adds the song to the song dictionary
def adding(song_name, song, song_dictionary):
    song_dictionary[song_name] = song  # Add the song to the dictionary
    return song_dictionary


# Removes a song from the song dictionary
def removing(song_name, song_dictionary):
    if song_name in song_dictionary:
        song_dictionary.pop(song_name)
        print(f"'{song_name}' has been removed.")
    else:
        print("Song not found.")
    return song_dictionary


# Finds if the song exists in the dictionary
def finding(song_name, song_dictionary):
    if song_name in song_dictionary:
        return True
    else:
        print("That song is not in your playlist.")
        return False


# Displays all songs in the playlist
def display(song_dictionary):
    while True:
        try:
            display_input = int(input("Would you like to display all details(1) or just the name and composer(2)?: "))
        except:
            print("invalid input")
            continue

        if display_input == 1:
            print("Here is a list of all the songs and details in your playlist:")
            for song_name, details in song_dictionary.items():
                print(f"Song: {song_name}")
                print(f"Composer: {details['composer']}")
                print(f"Album: {details['album']}")
                print(f"Length in seconds: {details['length']}")
                print(f"Year made: {details['year']}")
                print()
        
        elif display_input == 2:
            print("Here is a list of all the songs and their composers in your playlist:")
            for song_name, details in song_dictionary.items():
                print(f"Song: {song_name}")
                print(f"Composer: {details['composer']}")
                print()
        
        elif display_input != 1 and display_input != 2:
            print("invalid input")
            continue

        break


# Code to update information for a song
def update(song_dictionary):
    print("Songs:")
    for key in song_dictionary:
        print(key)
    song_name = input("What song do you want to update?: ")

    if song_name in song_dictionary:
        print(f"Updating details for: {song_name}")
        song = song_dictionary[song_name]
        
        #Updates song details
        song['composer'] = input(f"Update composer (current: {song['composer']}): ") or song['composer']
        song['album'] = input(f"Update album (current: {song['album']}): ") or song['album']
        while True:
            try:
                song['length'] = int(input(f"Update length in seconds (current: {song['length']}): ") or song['length'])
                break
            except:
                print("Invalid input, please enter a valid number.")
        while True:
            try:
                song['year'] = int(input(f"Update year (current: {song['year']}): ") or song['year'])
                break
            except:
                print("Invalid input, please enter a valid year.")
        
        print(f"Details for '{song_name}' have been updated.")
    else:
        print("Song not found.")


# Main function
def main():
    song_dictionary = {}

    while True:
        print()
        to_do = input("Would you like to add, remove, find, display, update, or leave?: ")

        if to_do == "add":
            song_name, song = making()
            song_dictionary = adding(song_name, song, song_dictionary)

        elif to_do == "remove":
            song_name = input("What is the name of the song you want to remove?: ")
            song_dictionary = removing(song_name, song_dictionary)
        
        elif to_do == "find":
            song_name = input("What is the name of the song you want to find?: ")
            found = finding(song_name, song_dictionary)
            if found:
                song = song_dictionary.get(song_name)
                print(f"Composer: {song['composer']}")
                print(f"Album: {song['album']}")
                print(f"Length in seconds: {song['length']}")
                print(f"Year the song was made: {song['year']}")

        elif to_do == "display":
            display(song_dictionary)

        elif to_do == "update":
            update(song_dictionary)
        
        elif to_do == "leave":
            print("Have a good day!")
            break

        else:
            print("Invalid input, please try again.")


# Runs the main function
main()
