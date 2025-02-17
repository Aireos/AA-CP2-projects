import csv

# Function to read the movie data and store it in a dictionary
def movies_maker():
    movie_dictionary = {}

    with open("Personal Projects/Movie Recommender/Movies list.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            movie = {
                "director": row[1],
                "genre": row[2],
                "rating": row[3],
                "length": row[4],
                "actors": row[5]
            }
            movie_name = row[0]
            movie_dictionary[movie_name] = movie

    return movie_dictionary

# Function to create a list of all available movie names
def filtered_movies_maker(movie_dictionary):
    filtered_movies = []
    for movie_name, details in movie_dictionary.items():
        filtered_movies.append(movie_name)
    return filtered_movies

# Function to print out all movies with details
def movies_printer(movie_dictionary):
    print("Here is a list of all the available movies:")
    print("-------------------------------------------------------")
    for movie_name, details in movie_dictionary.items():
        print(f"Name: {movie_name}")
        print(f"Director: {details['director']}")
        print(f"Genre: {details['genre']}")
        print(f"Rating: {details['rating']}")
        print(f"Length in minutes: {details['length']}")
        print(f"Actors: {details['actors']}")
        print("-------------------------------------------------------")

# Filter movies based on length
def filter_one(filtered_movies, movie_dictionary):
    filter_input_one = input("What is the range you want your movie length to be in? (write like this: 100-120): ")
    filter_one_movies = []
    sanitized_one = filter_input_one.split("-")
    sanitized_one_min = int(sanitized_one[0])
    sanitized_one_max = int(sanitized_one[1]) + 1
    for number in range(sanitized_one_min, sanitized_one_max):
        for movie_name, details in movie_dictionary.items():
            if number == int(details["length"]):
                if movie_name in filtered_movies:
                    filter_one_movies.append(movie_name)
    return filter_one_movies

# Filter movies based on rating
def filter_two(filtered_movies, movie_dictionary):
    filter_two_movies = []
    filter_input_two = input("What is the rating of the movie you want to find? (R, PG-13, or PG): ")
    for item in filtered_movies:
        if movie_dictionary[item]["rating"] == filter_input_two:
            filter_two_movies.append(item)
    return filter_two_movies

# Filter movies based on director
def filter_three(filtered_movies, movie_dictionary):
    filter_three_movies = []
    filter_input_three = input("What is the name of the director you want to find?: ")
    for movie_name, details in movie_dictionary.items():
        if filter_input_three.lower() in details["director"].lower():
            filter_three_movies.append(movie_name)
    return filter_three_movies

# Filter movies based on actor
def filter_four(filtered_movies, movie_dictionary):
    filter_four_movies = []
    filter_input_four = input("What actor's movies do you want to find?: ")
    for movie_name, details in movie_dictionary.items():
        actors = details["actors"].split(", ")
        if filter_input_four.lower() in [actor.lower() for actor in actors]:
            filter_four_movies.append(movie_name)
    return filter_four_movies

# Print out the filtered movies with details
def print_filtered(filtered_movies, movie_dictionary):
    print("Here is a list of all the movies that fit your needs:")
    print("-------------------------------------------------------")
    for movie_name, details in movie_dictionary.items():
        if movie_name in filtered_movies:
            print(f"Name: {movie_name}")
            print(f"Director: {details['director']}")
            print(f"Genre: {details['genre']}")
            print(f"Rating: {details['rating']}")
            print(f"Length in minutes: {details['length']}")
            print(f"Actors: {details['actors']}")
            print("-------------------------------------------------------")

# Function to display the filter choices
def filter_choice(filtered_movies, movie_dictionary):
    print("Choose the filters you would like to apply:")
    print("1. Filter by Length")
    print("2. Filter by Rating")
    print("3. Filter by Director")
    print("4. Filter by Actor")
    print("5. Print All Movies")

    filter_choices = input("Enter the numbers of the two filters you want to use (separate with a comma, e.g., 1,3) or '5' to print all movies: ")
    
    # If they choose to see all movies without filtering
    if filter_choices == '5':
        print_filtered(filtered_movies, movie_dictionary)
        return

    filters = filter_choices.split(",")
    
    # Apply filters
    if '1' in filters:
        filtered_movies = filter_one(filtered_movies, movie_dictionary)
    if '2' in filters:
        filtered_movies = filter_two(filtered_movies, movie_dictionary)
    if '3' in filters:
        filtered_movies = filter_three(filtered_movies, movie_dictionary)
    if '4' in filters:
        filtered_movies = filter_four(filtered_movies, movie_dictionary)
    
    print_filtered(filtered_movies, movie_dictionary)

# Main function to tie everything together
def main():
    movie_dictionary = movies_maker()
    filtered_movies = filtered_movies_maker(movie_dictionary)
    filter_choice(filtered_movies, movie_dictionary)

# Run the program
main()
